from django.contrib import admin

# Register your models here.
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ('name',)}


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'firstName', 'lastName',
                    'photo', 'is_active', 'is_staff')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'name')
    list_editable = ('is_staff',)
    list_filter = ('email', 'is_staff')
    # prepopulated_fields = {"slug": ('title',)}


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
