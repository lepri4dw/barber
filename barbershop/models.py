from django.db import models


class Barber(models.Model):
    photo = models.ImageField(upload_to='barbers/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Application(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    desired_time = models.TimeField()
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.barber.name} - {self.service.name} - {self.date} - {self.phone_number}"
