from django.db import models
from django.urls import reverse_lazy

class Human(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Имя')
    Last_name = models.TextField(blank=True, verbose_name='Портфолио')
    age = models.CharField(max_length=150, verbose_name='Телефон')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')
    biography = models.TextField(blank=True, verbose_name='Специализация')

    def get_absolute_url(self):
        return reverse_lazy('Human_1', kwargs={'pk': self.pk})
    class Meta:
        verbose_name='людей'
        verbose_name_plural='Люди'
        ordering = ['id']

class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')
    price = models.TextField(blank=True, verbose_name='Цена')

    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['id']

class Review(models.Model):
    title = models.TextField(blank=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def get_absolute_url(self):
        return reverse_lazy('Review', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']

