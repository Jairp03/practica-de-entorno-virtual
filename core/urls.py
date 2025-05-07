from django.urls import path
from . import views

name_app = 'core'

urlpatterns = [
    path('doctor_list/', views.doctor_list, name='doctor_list'),
]