from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Barber(models.Model):
    photo = models.ImageField(upload_to='barbers/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    barber = models.ForeignKey(Barber, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Review for {self.barber.name} {self.comment}"


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


