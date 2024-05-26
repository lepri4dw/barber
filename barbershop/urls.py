from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.application_form, name='application_form'),
    path('thanks/', views.thanks_view, name='thanks'),
    path('', views.index_view, name='home'),
    path('barbers/<int:pk>/', views.barber_detail, name='barber_detail'),
    path('add_review/', views.add_review, name='add_review'),
]