# Generated by Django 4.0.3 on 2022-03-24 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortalApp', '0002_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]