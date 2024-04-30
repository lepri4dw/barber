from django.contrib import admin

from barbershop.models import Barber, Service, Application

admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(Application)