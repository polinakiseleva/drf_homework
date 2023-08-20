# Generated by Django 4.2.4 on 2023-08-19 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Сумма оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Метод оплаты'),
        ),
    ]