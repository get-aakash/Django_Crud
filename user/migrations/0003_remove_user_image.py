# Generated by Django 3.2.4 on 2021-06-22 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
