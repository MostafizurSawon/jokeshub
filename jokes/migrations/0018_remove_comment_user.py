# Generated by Django 5.0.1 on 2024-03-11 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0017_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
