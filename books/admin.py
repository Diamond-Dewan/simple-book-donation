from django.contrib import admin
from .models import Category, Book

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'edition')
    list_display_links = ('title',)
    list_filter = ('author',)
    search_fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
