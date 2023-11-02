# Generated by Django 4.2.4 on 2023-10-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_hr_date_of_join_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='converted_date',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='date_of_join',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='institut_complate_date',
            field=models.DateField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='institut_start_date',
            field=models.DateField(max_length=30, null=True),
        ),
    ]