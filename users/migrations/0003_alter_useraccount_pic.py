# Generated by Django 5.0.1 on 2024-03-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_useraccount_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='pic',
            field=models.URLField(choices=[(1, 'https://img.freepik.com/free-vector/woman-portrait-wearing-cap-glasses_1308-146040.jpg'), (2, 'https://img.freepik.com/premium-vector/young-man-face-avater-vector-illustration-design_968209-13.jpg'), (3, 'https://img.freepik.com/free-vector/male-teen-cartoon-wearing-hat_1308-153378.jpg'), (4, 'https://img.freepik.com/premium-photo/fun-asian-teenager-animation_183364-30921.jpg'), (5, 'https://img.freepik.com/free-vector/portrait-shorthaired-woman_1308-134103.jpg')], default=3),
        ),
    ]
