# Generated by Django 4.1.4 on 2023-01-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_contract_a_fk_contract_h_fk_contract_s_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='expire',
            field=models.DateField(default=None, verbose_name='Expire Date'),
        ),
    ]
