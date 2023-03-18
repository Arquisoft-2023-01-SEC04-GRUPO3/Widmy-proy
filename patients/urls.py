from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patientList'),
    path('patientcreate/', csrf_exempt(views.patient_create), name='patientCreate'),
]