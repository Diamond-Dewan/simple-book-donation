from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username


class UserBooks(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    bookId = models.ManyToManyField(Book, related_name="user_books")

    def __str__(self):
        return self.userId.username


class UserWishList(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    bookId = models.ManyToManyField(Book, related_name="user_wish_list")

    def __str__(self):
        return self.userId.username