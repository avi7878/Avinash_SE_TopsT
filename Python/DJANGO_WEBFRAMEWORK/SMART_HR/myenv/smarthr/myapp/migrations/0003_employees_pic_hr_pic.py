# Generated by Django 4.2.4 on 2023-09-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_contactno_employees_contact_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='pic',
            field=models.FileField(default='media/default.webp', upload_to='media/images'),
        ),
        migrations.AddField(
            model_name='hr',
            name='pic',
            field=models.FileField(default='media/default.webp', upload_to='media/images'),
        ),
    ]
