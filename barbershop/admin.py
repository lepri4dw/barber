from django.contrib import admin

from barbershop.models import Barber, Service, Application, Review

admin.site.register(Barber)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Application)