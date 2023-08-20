# Generated by Django 4.2.4 on 2023-08-19 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_remove_course_lesson_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата оплаты')),
                ('paid_course_or_lesson', models.CharField(max_length=250, verbose_name='Оплаченный курс или урок')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма оплаты')),
                ('payment_method', models.CharField(max_length=20, verbose_name='Метод оплаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
