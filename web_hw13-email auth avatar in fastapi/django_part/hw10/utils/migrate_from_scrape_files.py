import os
import django
import json

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")
django.setup()

from quotes.models import Quote, Tag, Author

QUOTES_FILE = os.path.join(os.path.dirname(__file__), "quotes.json")
AUTHORS_FILE = os.path.join(os.path.dirname(__file__), "authors.json")


def fill_database():

    with open(QUOTES_FILE, 'r', encoding="utf-8") as fh:
        quotes = json.load(fh)

    with open(AUTHORS_FILE, 'r', encoding="utf-8") as fh:
        authors = json.load(fh)


    for author in authors:
        if author['fullname'] == "Alexandre Dumas-fils":
            author["fullname"] = "Alexandre Dumas fils"

        Author.objects.get_or_create(
            fullname = author["fullname"],
            born_date = author["born_date"],
            born_location = author["born_location"],
            description = author["description"]
        )

    for quote in quotes:
        tags = []
        for tag in quote["tags"]:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(t)
            
        flag = bool(len(Quote.objects.filter(quote=quote["quote"])))
        
        if not flag:
            a = Author.objects.get(fullname=quote["author"])
            q = Quote.objects.create(
                quote = quote["quote"],
                author = a,
            )
            for tag in tags:
                q.tags.add(tag)


if __name__ == "__main__":
    fill_database()