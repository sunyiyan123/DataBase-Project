# Generated by Django 2.0.3 on 2018-05-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='unread_count',
            field=models.IntegerField(default=10),
        ),
    ]
