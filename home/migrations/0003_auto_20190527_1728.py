# Generated by Django 2.1.7 on 2019-05-27 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0002_evro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EvRo',
            new_name='SiteSchema',
        ),
    ]