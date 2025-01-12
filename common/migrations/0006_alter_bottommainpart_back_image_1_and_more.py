# Generated by Django 5.1 on 2024-09-08 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_links_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottommainpart',
            name='back_image_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_image_1', to='common.media', verbose_name='Right back image'),
        ),
        migrations.AlterField(
            model_name='bottommainpart',
            name='back_image_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_image_2', to='common.media', verbose_name='Left back image'),
        ),
    ]
