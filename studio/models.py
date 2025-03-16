from django.contrib.auth.models import User
from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_hour = models.IntegerField()

    def __str__(self):
        return self.name

class Rent(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateTimeField()
    rent_hours = models.IntegerField()
    total_price = models.IntegerField()
    def save(self, *args, **kwargs):
        self.total_price = self.studio.price_per_hour * self.rent_hours
        super(Rent, self).save(*args, **kwargs)

    def __str__(self):
        return (f"{self.studio.name} "
                f"Арендовано на {self.rent_date}. Время записи: {self.rent_hours} Оплата {self.total_price}")
