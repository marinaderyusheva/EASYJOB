from django.urls import path
from . import views

urlpatterns = [
    path('', views.freelancers_home, name='freelancers_home'),
    path('add_freelancer/', views.add_freelancer, name='add_freelancer'),
]