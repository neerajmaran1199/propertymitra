# Generated by Django 2.2.2 on 2020-04-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200409_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(upload_to='blog_pics'),
        ),
    ]
