# Generated by Django 3.1 on 2020-08-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20200819_1338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SidebarEntry',
            new_name='Sentry',
        ),
    ]