# Generated by Django 4.1.4 on 2022-12-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='alley',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Alley'),
        ),
        migrations.AlterField(
            model_name='address',
            name='floor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Floor'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='No'),
        ),
        migrations.AlterField(
            model_name='address',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Unit'),
        ),
    ]
