from django.urls import path

from blog.views import *

urlpatterns = [
    path('categories/', categories_page, name='categories_page'),
    path('category/<int:category_id>/', subcategories_page, name='subcategories_page'),
    path('subcategory/<int:subcategory_id>/', subcategory_page, name='subcategory_page'),
    path('post<int:article_id>/', article_page, name='article_page'),
]