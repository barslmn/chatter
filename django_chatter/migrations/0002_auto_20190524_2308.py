# Generated by Django 2.0.9 on 2019-05-25 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
    ]
