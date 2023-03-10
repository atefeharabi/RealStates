# Generated by Django 4.1.4 on 2022-12-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_apartment_mortgage_price_alter_apartment_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='image',
            field=models.ImageField(blank=True, default='images/apartments/default.jpg', null=True, upload_to='images/apartments', verbose_name='Apartment Image'),
        ),
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='images/houses/default.jpg', null=True, upload_to='images/houses', verbose_name='House Image'),
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, default='images/shops/default.jpg', null=True, upload_to='images/shops', verbose_name='Shop Image'),
        ),
    ]
