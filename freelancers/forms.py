from .models import Freelancers
from django.forms import ModelForm, TextInput, DateInput, Textarea


class FreelanceForm(ModelForm):
    class Meta:
        model = Freelancers
        fields = ['name_freelance', 'surname_freelance', 'age_freelance', 'sphere', 'about_freelance', 'time_create']

        widgets={
            "name_freelance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            "surname_freelance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            "age_freelance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст',
            }),
            "sphere": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сфера',
            }),
            "about_freelance": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О себе',
            }),
            "time_create": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
            })
        }