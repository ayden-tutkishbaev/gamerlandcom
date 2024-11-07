from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from mptt.models import MPTTModel, TreeForeignKey


class AboutUs(models.Model):
    headline = models.CharField(max_length=120, verbose_name=_("Headline"))
    text = models.CharField(max_length=120, verbose_name=_("Text"))
    picture = models.ForeignKey("common.Media", verbose_name='About us image', on_delete=models.CASCADE,
                                     related_name="about_us_image")
    link = models.CharField(max_length=200, verbose_name=_("Link"), validators=[RegexValidator(
        r'\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')])

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _('About us')
        verbose_name_plural = _('About us')


class ContactsAboutUs(models.Model):
    emoji = models.CharField(max_length=120, verbose_name=_("Emote"))
    headline = models.CharField(max_length=120, verbose_name=_("Headline"))
    link = models.CharField(max_length=120, verbose_name=_("Link"))

    def __str__(self):
        return self.headline

    def clean(self):
        count = ContactsAboutUs.objects.count()
        max_records = 2

        if count > max_records:
            raise ValidationError(_("No more than three recordings!"))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    headline = models.CharField(_('Headline'), max_length=120)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Subcategory(models.Model):
    headline = models.CharField(_('Headline'), max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  verbose_name=_("Category"),
                                 related_name='category')

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Article(models.Model):
    headline = models.CharField(_('Headline'), max_length=300)
    audio = models.ForeignKey("common.Media", verbose_name='Audio', on_delete=models.CASCADE,
                                related_name="audio_article", blank=True, null=True)
    picture = models.ForeignKey("common.Media", verbose_name='Image', on_delete=models.CASCADE,
                                related_name="picture_article")
    author = models.CharField(_('Headline'), max_length=150)
    author_icon = models.ForeignKey("common.Media", verbose_name="Author's icon", on_delete=models.CASCADE,
                                related_name="author_icon")
    interview_date = models.DateField(verbose_name="The date of interview")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,  verbose_name=_("Subcategory"),
                                    related_name='subcategory')
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class Comment(models.Model):
    likes = models.IntegerField(verbose_name="Likes", default=0)
    dislikes = models.IntegerField(verbose_name="Dislikes", default=0)
    author = models.CharField(verbose_name="Author", max_length=80)
    text = models.CharField(max_length=100, verbose_name=_('Comment text'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.author

    