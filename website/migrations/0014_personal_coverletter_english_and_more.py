# Generated by Django 4.2.6 on 2023-10-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='coverletter_english',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='coverletter_turkish',
            field=models.TextField(blank=True),
        ),
    ]