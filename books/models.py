from django.db import models
from datetime import datetime
from authors.models import Author

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
        
class Book(models.Model):
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category, related_name='books')
    title = models.CharField(max_length=300)
    edition = models.DecimalField(max_digits=3, decimal_places=2)
    publisher = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    list_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
