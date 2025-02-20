# Generated by Django 4.2.19 on 2025-02-20 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
        ('documentation', '0004_appsettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppSettings',
            new_name='DocumentationSettings',
        ),
        migrations.RenameField(
            model_name='documentationsettings',
            old_name='app_logo',
            new_name='doc_logo',
        ),
    ]
