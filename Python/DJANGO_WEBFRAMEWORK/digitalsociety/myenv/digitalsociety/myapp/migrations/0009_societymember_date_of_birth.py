# Generated by Django 4.2.4 on 2023-10-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_vahical_no_societymember_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='societymember',
            name='date_of_birth',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
