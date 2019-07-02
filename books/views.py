from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Book, Category
from django.contrib import messages, auth
from users.models import UserBooks, Book, UserWishList

# Create your views here.

def index(request):
    books = Book.objects.order_by('-list_date')
    categorys = Category.objects.all()

    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    paged_books = paginator.get_page(page)

    context = {
        'books': paged_books,
        'categorys': categorys
    }
    return render(request, 'books/book_list.html', context)


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id) 
    categories = book.category.all()
    authors = book.author.all()
    context = {
        'book': book,
        'category': categories,
        'author': authors
    } 
    
    return render(request, 'books/book.html', context)


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categorys = Category.objects.all()

    cat = Category.objects.get(pk=category_id)
    books = cat.books.all()

    context = {
        'category': category,
        'categorys': categorys,
        'books': books       
    }

    return render(request, 'books/category.html', context)


def search(request):
    return render(request, 'books/search.html')


def addUserBook(request, book_id):
    book_id = Book.objects.get(pk=book_id)
    user = request.user

    try:
        userBook = UserBooks.objects.get(userId=user)
        userBook.bookId.add(book_id)
    
    except:
        userBook = UserBooks(userId=user)
        userBook.save()
        userBook.bookId.add(book_id)
    else:
        messages.error(request, 'Already Have This Book!!')

    return redirect('dashboard')


def addToWishList(request, book_id):
    book_id = Book.objects.get(pk=book_id)
    user = request.user

    try:
        userBook = UserWishList.objects.get(userId=user)
        userBook.bookId.add(book_id)
    
    except:
        userBook = UserWishList(userId=user)
        userBook.save()
        userBook.bookId.add(book_id)
    else:
        messages.error(request, 'Already added in the Wish List!!')
    finally:
        messages.success(request, 'Added in the Wish List!!')

    return redirect('dashboard')
