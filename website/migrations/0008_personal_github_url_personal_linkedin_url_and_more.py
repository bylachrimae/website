# Generated by Django 4.2.6 on 2023-10-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_personal_englishcv_alter_personal_turkishcv'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='github_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='linkedin_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='youtube_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
