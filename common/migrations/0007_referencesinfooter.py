# Generated by Django 5.1 on 2024-09-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_bottommainpart_back_image_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferencesInFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=300, verbose_name='Reference')),
            ],
            options={
                'verbose_name': 'Reference',
                'verbose_name_plural': 'References',
            },
        ),
    ]
