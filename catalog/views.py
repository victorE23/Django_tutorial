from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts for genres and books that contain a particular word (case insensitive)
    num_genre_word = Genre.objects.filter(
        name__contains='aventure').count()
    num_books_word = Book.objects.filter(title__contains='soledad').count()


    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre_word': num_genre_word,
        'num_books_word': num_books_word
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
