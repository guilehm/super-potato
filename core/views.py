from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from people.models import Patient


def index(request):
    return render(request, 'core/index.html')


def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            login(request, authenticated_user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Olá, {}, seu login foi efetuado com sucesso'.format(request.user)
            )
            return redirect('core:index')
    return render(request, 'core/accounts/login.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('core:index')


@login_required
def patient_list(request):
    # TODO: Implement filter by entity
    patients = Patient.objects.filter(entity=request.user.entity)
    return render(request, 'core/assistance/patient_list.html', {
        'patients': patients,
    })
