# Generated by Django 3.1 on 2020-08-20 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20200820_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entrie'},
        ),
        migrations.AlterModelOptions(
            name='sentry',
            options={'verbose_name': 'Sidebar entrie'},
        ),
        migrations.AlterModelOptions(
            name='sidebar',
            options={'verbose_name': 'Sidebar section'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='entries.section'),
        ),
        migrations.AlterField(
            model_name='sentry',
            name='sidebar_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_entries', to='entries.sidebar'),
        ),
    ]
