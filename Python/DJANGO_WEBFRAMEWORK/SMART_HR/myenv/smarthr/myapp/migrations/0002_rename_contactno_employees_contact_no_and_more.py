# Generated by Django 4.2.4 on 2023-09-22 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='contactno',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='hr',
            old_name='contactno',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='hr',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='hr',
            old_name='lastname',
            new_name='last_name',
        ),
    ]