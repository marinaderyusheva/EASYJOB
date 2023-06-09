# Generated by Django 4.2 on 2023-04-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_freelance', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname_freelance', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age_freelance', models.IntegerField(verbose_name='Возраст')),
                ('sphere', models.CharField(max_length=20, verbose_name='Сфера')),
                ('about_freelance', models.TextField(blank=True, default='', verbose_name='О себе')),
                ('time_create', models.DateField(verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Фрилансер',
                'verbose_name_plural': 'Фрилансеры',
            },
        ),
    ]
