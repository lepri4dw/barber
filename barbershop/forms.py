import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['barber', 'service', 'date', 'desired_time', 'name', 'phone_number']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'desired_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^(\+996)?\d{9}$', phone_number):
            raise ValidationError('Введите корректный номер телефона. Например, +996555555555.')
        return phone_number
