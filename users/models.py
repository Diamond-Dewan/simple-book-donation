from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/users/%Y/%m/%d')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    books_received = models.PositiveSmallIntegerField()
    books_donated = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name