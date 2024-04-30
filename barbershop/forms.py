import datetime
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
            'desired_time': forms.TimeInput(attrs={'type': 'time', 'step': '1800'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^(\+996)?\d{9}$', phone_number):
            raise ValidationError('Введите корректный номер телефона. Например, +996555555555.')
        return phone_number

    def clean_desired_time(self):
        desired_time = self.cleaned_data['desired_time']
        if desired_time.hour < 9 or desired_time.hour > 20:
            raise ValidationError('Выберите время с 9 утра до 8 вечера.')
        return desired_time

    def clean_date(self):
        date = self.cleaned_data['date']
        if date == datetime.date.today() and datetime.datetime.now().hour >= 20:
            raise ValidationError('Выберите дату позже, если сегодня уже после 20:00.')
        elif date < datetime.date.today():
            raise ValidationError('Выберите дату позже сегодняшней.')
        return date
