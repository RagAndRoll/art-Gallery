# Generated by Django 3.2.3 on 2021-05-30 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='art',
            new_name='product',
        ),
    ]
