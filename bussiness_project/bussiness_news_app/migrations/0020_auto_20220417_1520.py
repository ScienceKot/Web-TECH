# Generated by Django 3.2.12 on 2022-04-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_news_app', '0019_auto_20220407_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='article_permission',
            field=models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE')], default='public', max_length=35),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(default='Hot News', max_length=100),
        ),
    ]
