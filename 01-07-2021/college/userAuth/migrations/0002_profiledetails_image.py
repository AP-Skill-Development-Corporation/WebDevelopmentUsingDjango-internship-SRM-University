# Generated by Django 2.2.2 on 2021-07-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='image',
            field=models.ImageField(default='default.png', upload_to='users/'),
        ),
    ]