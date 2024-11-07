# Generated by Django 5.1 on 2024-09-08 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_audio_alter_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='link',
            field=models.CharField(default=1, max_length=200, validators=[django.core.validators.RegexValidator('\\b((?:https?://|www\\d{0,3}[.]|[a-z0-9.\\-]+[.][a-z]{2,4}/)(?:[^\\s()<>]+|\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\))+(?:\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\)|[^\\s`!()\\[\\]{};:\\\'".,<>?«»“”‘’]))')], verbose_name='Link'),
            preserve_default=False,
        ),
    ]