from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Barber, Service, Application
from .forms import ApplicationForm


def application_form(request):
    barbers = Barber.objects.all()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'barbers': barbers,  'form': form})


def index_view(request):
    barbers = Barber.objects.all()
    services = Service.objects.all()
    return render(request, 'index.html', {'barbers': barbers, 'services': services})


def thanks_view(request):
    return render(request, 'thanks.html')
