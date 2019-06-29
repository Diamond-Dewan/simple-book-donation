from django.contrib import admin
from .models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', 'bio')
    list_display_links = ('name',)

admin.site.register(Author, AuthorAdmin)