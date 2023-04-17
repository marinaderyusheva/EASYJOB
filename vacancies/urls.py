from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancies_home, name='vacancies_home'),
    path('add_vacancii/', views.add_vacancii, name='add_vacancii'),
    path('<int:pk>', views.VacanciiDetailView.as_view(), name='vacancii-detail'),
]