from django.urls import path

from common.views import *

urlpatterns = [
    path('', home_page, name='home_page'),

    path('about_us/', about_us_page, name='about_us_page'),
    path('contacts/', contacts_page, name='contacts_page'),
]