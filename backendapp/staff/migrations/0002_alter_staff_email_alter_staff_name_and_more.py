# Generated by Django 4.1.4 on 2022-12-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='staff',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]