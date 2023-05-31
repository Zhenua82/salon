from django.db import models
from django.urls import reverse_lazy

class Human(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Имя')
    Last_name = models.CharField(blank=True, max_length=150, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')
    biography = models.TextField(blank=True, verbose_name='Биография')

    def get_absolute_url(self):
        # return reverse_lazy('Human_1', kwargs={'human_id': self.pk})
        return reverse_lazy('Human_1', kwargs={'pk': self.pk})
    class Meta:
        verbose_name='людей'
        verbose_name_plural='Люди'
        ordering = ['id']

class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['id']


