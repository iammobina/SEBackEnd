# Generated by Django 2.2.2 on 2019-11-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0015_auto_20191108_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/profile/profile.jpg', upload_to='profile'),
        ),
    ]
