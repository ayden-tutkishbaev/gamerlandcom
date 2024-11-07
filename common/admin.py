from django.contrib import admin

from common.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file_type']
    list_filter = ['file_type']


@admin.register(FooterCaption)
class FooterCaptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption1', 'copyright']


@admin.register(BottomMainPart)
class BottomMainPartAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption']


@admin.register(ReferencesInFooter)
class ReferencesInFooterAdmin(admin.ModelAdmin):
    list_display = ['id', 'reference']


@admin.register(Links)
class LinksPartAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id']