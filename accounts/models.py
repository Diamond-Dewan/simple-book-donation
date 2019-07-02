from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class UserProfile(models.Model):
    '''
        User details info
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # connect to django User
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/users/%Y/%m/%d')


class UserBooks(models.Model):
    '''
        Books that one user have 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # connect to django User
    user_books = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    book_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.user

class UserWishList(models.Model):
    '''
        Books A user wish to receive
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # connect to django User
    wish_books = models.ManyToManyField(Book, related_name="user_wish_books")
    # book_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.user