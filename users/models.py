from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(verbose_name='Почта', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    is_verificated = models.BooleanField(default=False, verbose_name='Подтверждение почты')

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
