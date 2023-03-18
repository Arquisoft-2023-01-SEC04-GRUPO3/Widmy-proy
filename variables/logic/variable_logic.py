from ..models import Patient

def get_patients():
    queryset = Patient.objects.all()
    return (queryset)

def create_patient(form):
    measurement = form.save()
    measurement.save()
    return ()