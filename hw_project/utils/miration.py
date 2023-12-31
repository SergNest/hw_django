import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()

from quotes.models import Tag, Autor, Quote  # noqa


client = MongoClient('mongodb://localhost')
db = client.hw


authors = db.authors.find()

for author in authors:
    Autor.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quote.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    # print(tags)
    # print(quote['quote'])
    # print(quote['author'])

    exists_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exists_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Autor.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)

