# Generated by Django 5.1 on 2024-09-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]