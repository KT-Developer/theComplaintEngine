# Generated by Django 5.0.4 on 2024-04-13 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complainroom',
            old_name='name',
            new_name='subject',
        ),
    ]
