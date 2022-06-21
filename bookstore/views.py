from django.shortcuts import render

# Create your views here.
books = [{'id': 1, 'title': 'Fluent Python','released_year': 2015, 'description': 'Python’s simplicity lets you '
                                                                                  'become productive quickly, '
                                                                                  'but this often means you aren’t '
                                                                                  'using everything it has to offer. '
                                                                                  'With this hands-on guide, '
                                                                                  'you’ll learn how to write '
                                                                                  'effective, idiomatic Python code '
                                                                                  'by leveraging its best—and '
                                                                                  'possibly most neglected—features. '
                                                                                  'Author Luciano Ramalho takes you '
                                                                                  'through Python’s core language '
                                                                                  'features and libraries, '
                                                                                  'and shows you how to make your '
                                                                                  'code shorter, faster, '
                                                                                  'and more readable at the same '
                                                                                  'time.', 'author_id': 1},
                                                                                  {'id': 2,
                                                                                   'title': 'My title - Python',
                                                                                   'released_year': 2022,
                                                                                   'description': 'My description',
                                                                                    'author_id': 2},
                                                                                    {
                                                                                    'id': 3,
                                                                                    'title': 'Learn django',
                                                                                    'released_year': 2022,
                                                                                    'description': 'Django - pro', 'author_id': 1}]
authors = [{'id': 1, 'first_name': "Luciano", 'last_name': 'Ramalho', 'age': 51},
           {'id': 2, 'first_name': 'Puchino', 'last_name': 'Alpachino', 'age': 22}]


def list_books(request):
    return render(request, 'bookstore/list_books.html', context={'books': books})

def book_description(request,title):
    for i in books:
        if i['title'] == title:
            full_description = i
    return render(request, 'bookstore/book_description.html', context={'full_description': full_description})

def infobook(request, title):
    for i in books:
        if i['title'] == title:
            for author in authors:
                if i['author_id'] == author['id']:
                    return render(request, 'bookstore/infobook.html', context={'author': author, 'book': i})


def infoauthor(request,index):
    book_list = []
    for i in authors:
        for book in books:
            if i['id'] == book['author_id'] and i['id'] == index:
                book_list.append(book)
                author = i
    return render(request, 'bookstore/infoauthor.html', context={'book_list': book_list, 'author': author})



