from django.shortcuts import render
from common.models import *
from blog.models import *


def categories_page(request):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()

    categories = Category.objects.all()

    context = {
        "title": 'Категории',
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        "footer": footer,
        "bottom": bottom,
        'references': references,
        'links': links,
        'categories': categories
    }

    return render(request, "pages/categories.html", context)


def subcategories_page(request, category_id):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()

    subcategories = Subcategory.objects.filter(category=category_id)

    context = {
        "title": f'Подкатегории: {Category.objects.get(id=category_id)}',
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        "footer": footer,
        "bottom": bottom,
        'references': references,
        'links': links,
        'subcategories': subcategories
    }

    return render(request, "pages/subcategories.html", context)


def subcategory_page(request, subcategory_id):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()

    posts = Article.objects.filter(subcategory=subcategory_id)

    context = {
        "title": f'{Subcategory.objects.get(id=subcategory_id)}',
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        "footer": footer,
        "bottom": bottom,
        'references': references,
        'links': links,
        'posts': posts
    }

    return render(request, "pages/subcategory.html", context)


def article_page(request, article_id):

    footer = FooterCaption.objects.get()
    bottom = BottomMainPart.objects.get()
    about_us = AboutUs.objects.get()
    contact_about_us = ContactsAboutUs.objects.all()
    references = ReferencesInFooter.objects.all()
    links = Links.objects.all()

    article = Article.objects.get(id=article_id)

    context = {
        "title": f'{article.headline}',
        "about_us": about_us,
        'contact_about_us': contact_about_us,
        "footer": footer,
        "bottom": bottom,
        'references': references,
        'links': links,
        'article': article
    }

    return render(request, "pages/post.html", context)
