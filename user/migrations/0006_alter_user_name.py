# Generated by Django 3.2.4 on 2021-06-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(error_messages={'required': 'This is the required field'}, max_length=40),
        ),
    ]
