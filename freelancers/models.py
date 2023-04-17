from django.db import models


class Freelancers(models.Model):
    name_freelance = models.CharField(max_length=50, verbose_name='Имя')
    surname_freelance = models.CharField(max_length=50, verbose_name='Фамилия')
    age_freelance = models.IntegerField(verbose_name='Возраст')
    sphere = models.CharField(max_length=20, verbose_name='Сфера')
    about_freelance = models.TextField(blank=True, verbose_name='О себе', default='')
    time_create = models.DateField(verbose_name='Дата регистрации')

    def __str__(self):
        return self.name_freelance

    class Meta:
        verbose_name = 'Фрилансер'
        verbose_name_plural = 'Фрилансеры'
