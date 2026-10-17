from django.conf import settings
from django.db import models
from django.utils import timezone

class Donation(models.Model):
    donator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    donationMessage = models.TextField(blank=True, null=True)
    donationAmount = models.DecimalField(max_digits=9, decimal_places=2)
    donationDate = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):
        return f"${self.donationAmount} by {self.donator}"

#class User(models.Model):