# Generated by Django 2.2 on 2019-05-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='topic',
            new_name='name',
        ),
    ]
