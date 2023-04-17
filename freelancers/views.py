from django.shortcuts import render, redirect
from .models import Freelancers
from .forms import FreelanceForm


def freelancers_home(request):
    freelancers = Freelancers.objects.all()
    return render(request, 'freelancers/freelancers.html', {'freelancers': freelancers})


def add_freelancer(request):
    error = ''
    #проверка данных на сервере
    if request.method == 'POST':
        form = FreelanceForm(request.POST)
        if form.is_valid():
            form.save()
            #после заполнения формы переадресация на страницу фрилансеров
            return redirect('freelancers_home')
        else:
            error = 'Форма неверна'

    form = FreelanceForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'freelancers/add_freelancer.html', data)