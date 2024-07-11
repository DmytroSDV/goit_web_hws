import pickle
from datetime import datetime, timedelta
from typing import Optional

import redis
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt

from source.database.db import get_db
from source.repository import consumers as repository_consumer
from source.config.conf import config


class Auth:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    SECRET_KEY = config.SECRET_KEY_JWT
    ALGORITHM = config.ALGORITHM
    cache = redis.Redis(
        host=config.REDIS_DOMAIN,
        port=config.REDIS_PORT,
        db=0,
        password=config.REDIS_PASSWORD,
    )

    def verify_password(self, plain_password, hashed_password):
        """
        The verify_password function takes a plain-text password and the hashed version of that password,
            and returns True if they match, False otherwise. This is used to verify that the user's login
            credentials are correct.
        
        :param self: Represent the instance of the class
        :param plain_password: Get the password from the user
        :param hashed_password: Check if the password matches with the hashed_password
        :return: A boolean value
        :doc-author: Trelent
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        """
        The get_password_hash function takes a password as input and returns the hash of that password.
            The function uses the pwd_context object to generate a hash from the given password.
        
        :param self: Represent the instance of the class
        :param password: str: Pass the password to be hashed
        :return: A password hash
        :doc-author: Trelent
        """
        return self.pwd_context.hash(password)

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

    async def create_access_token(self, data: dict, expires_delta: Optional[float] = None):
        """
        The create_access_token function creates a new access token for the user.
            
        
        :param self: Represent the instance of a class
        :param data: dict: Pass the data to be encoded in the access token
        :param expires_delta: Optional[float]: Set the time in seconds for which the token is valid
        :return: A string
        :doc-author: Trelent
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire, "scope": "access_token"})
        encoded_access_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_access_token

    async def create_refresh_token(self, data: dict, expires_delta: Optional[float] = None):
        """
        The create_refresh_token function creates a refresh token for the user.
            Args:
                data (dict): A dictionary containing the user's id and username.
                expires_delta (Optional[float]): The number of seconds until the refresh token expires. Defaults to None, which sets it to 7 days from now.
        
        :param self: Represent the instance of a class
        :param data: dict: Pass the data to be encoded
        :param expires_delta: Optional[float]: Set the expiration time of the refresh token
        :return: A refresh token that is encoded with the user's data and a scope of refresh_token
        :doc-author: Trelent
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire, "scope": "refresh_token"})
        encoded_refresh_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_refresh_token

    async def decode_refresh_token(self, refresh_token: str):
        """
        The decode_refresh_token function takes a refresh token and decodes it.
            If the scope is 'refresh_token', then we return the email address of the user.
            Otherwise, we raise an HTTPException with status code 401 (UNAUTHORIZED) and detail message 'Invalid scope for token'.
        
        
        :param self: Represent the instance of the class
        :param refresh_token: str: Pass the refresh token to the function
        :return: The email of the user who is trying to refresh their access token
        :doc-author: Trelent
        """
        try:
            payload = jwt.decode(refresh_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if payload['scope'] == 'refresh_token':
                email = payload['sub']
                return email
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

    async def get_current_user(
        self, token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
    ):
        """
        The get_current_user function is a dependency that will be used in the
            protected endpoints. It takes a token as an argument and returns the user
            object if it exists, otherwise it raises an exception.
        
        :param self: Represent the instance of a class
        :param token: str: Get the token from the request header
        :param db: AsyncSession: Get the database session
        :return: A user object
        :doc-author: Trelent
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            # Decode JWT
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if payload["scope"] == "access_token":
                email = payload["sub"]
                if email is None:
                    raise credentials_exception
            else:
                raise credentials_exception
        except JWTError as e:
            raise credentials_exception

        user_hash = str(email)

        user = self.cache.get(user_hash)

        if user is None:
            print("User from database")
            user = await repository_consumer.get_user_by_email(email, db)
            if user is None:
                raise credentials_exception
            self.cache.set(user_hash, pickle.dumps(user))
            self.cache.expire(user_hash, 300)
        else:
            print("User from cache")
            user = pickle.loads(user)
        return user

    def create_email_token(self, data: dict):
        """
        The create_email_token function takes a dictionary of data and returns a JWT token.
        The token is encoded with the SECRET_KEY and ALGORITHM defined in the class.
        The iat (issued at) claim is set to datetime.utcnow() and exp (expiration time) 
        is set to one day from now.
        
        :param self: Represent the instance of the class
        :param data: dict: Pass the data to be encoded in the token
        :return: A token
        :doc-author: Trelent
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=1)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire})
        token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return token

    async def get_email_from_token(self, token: str):
        """
        The get_email_from_token function takes a token as an argument and returns the email address associated with that token.
        The function uses the jwt library to decode the token, which is then used to retrieve the email address from within it.
        
        :param self: Represent the instance of the class
        :param token: str: Pass in the token that was sent to the user's email address
        :return: The email address associated with the token
        :doc-author: Trelent
        """
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            email = payload["sub"]
            return email
        except JWTError as ex:
            print(ex)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Invalid token for email verification")
    async def get_password_from_token(self, token: str):
        """
        The get_password_from_token function takes a token as an argument and returns the password that was encoded in the token.
        The function uses jwt to decode the token, which is then used to return the password.
        
        :param self: Represent the instance of a class
        :param token: str: Pass in the token that was generated when the user signed up
        :return: The password from the token
        :doc-author: Trelent
        """
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            password = payload["password"]
            return password
        except JWTError as ex:
            print(ex)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Invalid token for password verification")

auth_service = Auth()
