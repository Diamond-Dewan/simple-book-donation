from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserBooks, UserWishList

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','email', 'phone')
    list_display_links = ('username',)
    search_fields = ('username',)

admin.site.register(User, UsersAdmin)
admin.site.register(UserBooks)
admin.site.register(UserWishList)
