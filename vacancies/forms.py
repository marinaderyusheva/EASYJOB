from .models import Vaсancii
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class VacanciiForm(ModelForm):
    class Meta:
        model = Vaсancii
        fields=['title_vacancii', 'sphere', 'about_vacancii', 'time_create']

        widgets = {
            "title_vacancii": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "sphere": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сфера'
            }),
            "time_create": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "about_vacancii": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О вакансии'
            }),

        }