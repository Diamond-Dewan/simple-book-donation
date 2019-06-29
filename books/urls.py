from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'booklist'),
    path('<int:book_id>', views.book, name='book'),
    path('category/<int:category_id>', views.category, name='category'),
    path('search', views.search, name='search'),
] 