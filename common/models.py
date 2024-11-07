from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, RegexValidator


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')
        AUDIO = 'audio', _('Audio')
        DOCUMENT = 'document', _('Document')
        GIF = 'gif', _('Gif')
        OTHER = 'other', _('Other')

    file = models.FileField(upload_to='only_medias/', verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'mp3', 'doc', 'docx', 'xls',
                                                                                   'xlsx', 'ppt', 'pptx', 'txt', 'csv',
                                                                                   'zip', 'rar', 'pdf', 'ogg'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"), choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return self.file.name

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov']:
                raise ValidationError(_("Invalid Video File"))
        elif self.file_type == self.FileType.AUDIO:
            if self.file.name.split('.')[-1] not in ['mp3', 'wav', 'ogg']:
                raise ValidationError(_("Invalid Audio File"))


class FooterCaption(models.Model):
    caption1 = models.CharField(max_length=300, verbose_name=_('Caption 1'))
    copyright = models.CharField(max_length=300, verbose_name=_('Copyright'))

    def __str__(self):
        return self.caption1

    class Meta:
        verbose_name = _('Footer caption')
        verbose_name_plural = _('Footer caption')


class ReferencesInFooter(models.Model):
    reference = models.CharField(max_length=300, verbose_name=_('Reference'))

    def __str__(self):
        return self.reference

    class Meta:
        verbose_name = _('Reference')
        verbose_name_plural = _('References')


class BottomMainPart(models.Model):
    back_image_1 = models.ForeignKey(Media, verbose_name='Right back image', on_delete=models.CASCADE,
                                     related_name="back_image_1")
    back_image_2 = models.ForeignKey(Media, verbose_name='Left back image', on_delete=models.CASCADE,
                                     related_name="back_image_2")
    caption = models.CharField(max_length=300, verbose_name=_("Caption"))
    header_image = models.ForeignKey(Media, verbose_name='Header image', on_delete=models.CASCADE,
                                     related_name="header_image")
    category_picture = models.ForeignKey("common.Media", verbose_name='Category image', on_delete=models.CASCADE,
                                     related_name="category_image")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Bottom part')
        verbose_name_plural = _('Bottom part')


class Links(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    link = models.CharField(max_length=200, verbose_name=_("Link"), validators=[RegexValidator(r'\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")


class SocialMedia(models.Model):
    picture = models.ForeignKey(Media, verbose_name='Social media picture', on_delete=models.CASCADE,
                                related_name="social_media_pic")
    link = models.CharField(max_length=200, verbose_name=_("Link"), validators=[RegexValidator(r'\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')])

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = _("Social media")
        verbose_name_plural = _("Social media")