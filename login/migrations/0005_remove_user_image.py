# Generated by Django 3.2.4 on 2021-07-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
