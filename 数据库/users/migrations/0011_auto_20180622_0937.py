# Generated by Django 2.0.6 on 2018-06-22 09:37

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180607_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile',
            field=imagekit.models.fields.ProcessedImageField(default='user/img/default.jpg', upload_to='user/img'),
        ),
    ]
