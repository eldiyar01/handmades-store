# Generated by Django 4.0.4 on 2022-05-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='photo',
            new_name='avatar',
        ),
    ]