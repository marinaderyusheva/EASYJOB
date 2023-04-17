from django.db import models

class Vaсancii(models.Model):
    title_vacancii = models.CharField(max_length=50, verbose_name='Наименование')
    sphere = models.CharField(max_length=20, verbose_name='Сфера')
    about_vacancii = models.TextField(blank=True, verbose_name='О вакансии')
    time_create = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title_vacancii

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
