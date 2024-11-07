from django.shortcuts import render
from common.models import *
from blog.models import *


def home_page(request):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()
    posts = Article.objects.all()

    context = {
        "title": 'Главная страница',
        "footer": footer,
        "bottom": bottom,
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        'references': references,
        'links': links,
        'posts': posts
    }

    return render(request, "pages/index.html", context)


def about_us_page(request):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()

    context = {
        "title": 'О нас',
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        "footer": footer,
        "bottom": bottom,
        'references': references,
        'links': links
    }

    return render(request, "pages/about_us.html", context)


def contacts_page(request):

    return render(request, "pages/contacts.html")
