from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PatientForm
from .logic.patient_logic import get_patients, create_patient

def patient_list(request):
    patients = get_patients()
    context = {
        'patient_list': patients
    }
    return render(request, 'Patient/patients.html', context)

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            create_patient(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created patient')
            return HttpResponseRedirect(reverse('patientCreate'))
        else:
            print(form.errors)
    else:
        form = PatientForm()

    context = {
        'form': form,
    }
    return render(request, 'Patient/patientCreate.html', context)