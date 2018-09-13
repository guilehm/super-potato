from django.shortcuts import render

from people.models import Patient


def index(request):
    return render(request, 'core/index.html')


def patient_list(request):
    # TODO: Implement filter by entity
    patients = Patient.objects.all()
    return render(request, 'core/assistance/patient_list.html', {
        'patients': patients,
    })
