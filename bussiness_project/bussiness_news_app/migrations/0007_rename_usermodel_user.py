# Generated by Django 3.2.12 on 2022-03-31 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_news_app', '0006_alter_usermodel_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='User',
        ),
    ]
