# Generated by Django 4.2.4 on 2023-12-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acapp', '0002_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
