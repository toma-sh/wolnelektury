from requests import get

def get_authors(search: str = None):
    authors = []
    query = get('https://wolnelektury.pl/api/authors/')

    for author_id, author in enumerate(query.json(), start=1):
        if search is not None or search.upper() in author['name'].upper():
            authors.append({
                'author_id': author_id,
                'name': author.get('name'),
                'api_books_url': author.get('href') + 'books'
            })

        return authors

authors = get_authors('Adam')

for author in authors:
    print(f"{author.get('author_id')}. {author.get('name')}")
