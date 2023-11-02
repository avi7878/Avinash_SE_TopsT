# Generated by Django 4.2.4 on 2023-10-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_hr_converted_date_alter_hr_date_of_join_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='converted_date',
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_of_join',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='institut_complate_date',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='institut_start_date',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='date_of_birth',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='date_of_join',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='institut_complate_date',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='institut_start_date',
            field=models.TextField(max_length=30, null=True),
        ),
    ]