from django.contrib import admin
from blog.models import *


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline']


@admin.register(ContactsAboutUs)
class ContactsAboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline']
    search_fields = ['headline']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline']
    search_fields = ['headline']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'author', 'interview_date']
    search_fields = ['author', 'headline']
