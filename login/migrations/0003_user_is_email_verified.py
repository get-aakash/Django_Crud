# Generated by Django 3.2.4 on 2021-07-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]