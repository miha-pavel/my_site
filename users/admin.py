from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')

admin.site.register(User, UserAdmin)
