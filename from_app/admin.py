from django.contrib import admin

from .models import *


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'image', 'created_at']
    list_filter = ['id', 'name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'image', 'category', 'created_at']
    search_fields = ['name']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['year', 'name', 'body', 'image', 'created_at']
    search_fields = ['name']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job', 'image', 'tw_link', 'fb_link', 'in_link']
    search_fields = ['name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'number',  'created_at']
    search_fields = ['name']


admin.site.register(Services, ServicesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
