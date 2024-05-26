from django.core.paginator import Paginator
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Barber, Service, Application, Review
from .forms import ApplicationForm, ReviewForm


def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    reviews = barber.reviews.all().order_by('-created_at')
    paginator = Paginator(reviews, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'barber_detail.html', {'barber': barber, 'page_obj': page_obj, 'average_rating': average_rating})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            barber_id = request.POST.get('barber_id')
            barber = get_object_or_404(Barber, pk=barber_id)
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            Review.objects.create(barber=barber, rating=rating, comment=comment)
            return redirect('barber_detail', pk=barber_id)
    return redirect('home')


def application_form(request):
    barbers = Barber.objects.all()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'barbers': barbers, 'form': form})


def index_view(request):
    barbers = Barber.objects.all()
    services = Service.objects.all()
    return render(request, 'index.html', {'barbers': barbers, 'services': services})


def thanks_view(request):
    return render(request, 'thanks.html')
