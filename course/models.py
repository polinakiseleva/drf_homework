from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Модель курса"""
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='course_preview/', verbose_name='Превью', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lesson_preview/', verbose_name='Превью', **NULLABLE)
    video_link = models.TextField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='lessons',
                               verbose_name='Курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
