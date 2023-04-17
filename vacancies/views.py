from django.shortcuts import render, redirect
from .models import Vaсancii
from .forms import VacanciiForm
from django.views.generic import DetailView


def vacancies_home(request):
    vacancii = Vaсancii.objects.all()
    return render(request, 'vacancies/vacancies_home.html', {'vacancii': vacancii})


class VacanciiDetailView(DetailView):
    model = Vaсancii
    template_name ='vacancies/details_view.html'
    context_object_name = 'article'

def add_vacancii(request):
    error = ''
    if request.method == 'POST':
        form = VacanciiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancies_home')
        else:
            error = 'Форма неверна'

    form = VacanciiForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'vacancies/add_vacancii.html', data)
