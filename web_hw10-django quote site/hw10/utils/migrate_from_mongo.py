import os
import django

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")
django.setup()

from quotes.models import Quote, Tag, Author

from pymongo import MongoClient


client = MongoClient("mongodb://localhost")

db = client.hw10

authors = db.authors.find()

for author in authors:
    if author['fullname'] == "Alexandre Dumas-fils":
        author["fullname"] = "Alexandre Dumas fils"

    Author.objects.get_or_create(
        fullname = author["fullname"],
        born_date = author["born_date"],
        born_location = author["born_location"],
        description = author["description"]
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
        
    flag = bool(len(Quote.objects.filter(quote=quote["quote"])))
    
    if not flag:
        author = db.authors.find_one({"_id": quote["author"]})
        a = Author.objects.get(fullname=author["fullname"])
        q = Quote.objects.create(
            quote = quote["quote"],
            author = a,
        )
        for tag in tags:
            q.tags.add(tag)