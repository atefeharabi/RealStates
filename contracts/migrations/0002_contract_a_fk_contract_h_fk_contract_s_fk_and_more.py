# Generated by Django 4.1.4 on 2022-12-30 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='A_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.apartment', verbose_name='Apartment ID'),
        ),
        migrations.AddField(
            model_name='contract',
            name='h_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.house', verbose_name='House ID'),
        ),
        migrations.AddField(
            model_name='contract',
            name='s_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.shop', verbose_name='Shop ID'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='expire',
            field=models.DateField(null=True, verbose_name='Expire Date'),
        ),
    ]