# Generated by Django 4.2.6 on 2023-10-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_project_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image5',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
