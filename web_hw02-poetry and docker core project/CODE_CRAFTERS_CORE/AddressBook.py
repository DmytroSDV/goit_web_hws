from Record import Record
from RecordData import *
from collections import UserList
from tabulate import tabulate
from emoji import emojize
import pickle

class AddressBook(UserList):
    id_counter = 1 
    def __init__(self):
        super().__init__()               
                                       
    def save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}💾 Contacts added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")

    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading contacts from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            return pickle.load(file)
        
    def generate_id(self):
        current_id = self.id_counter
        self.id_counter += 1
        return current_id
                
