# Generated by Django 4.0.3 on 2022-03-28 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortalApp', '0005_alter_comment_options_alter_post_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='NewsPortalApp.post'),
        ),
    ]