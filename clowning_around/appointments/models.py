from django.db import models
from clowning_around.users.models import Clown, Client

# Create your models here.
class Appointment_Status (models.Model):
    Description = models.CharField(max_length=100)
    def __str__(self):
        return self.Description

class Appointment (models.Model):
    appointment_name = models.CharField(max_length=500)
    appointment_date = models.DateTimeField()
    appointment_status = models.ForeignKey(Appointment_Status, on_delete=models.CASCADE)
    clown = models.ForeignKey(Clown, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    report_issue = models.CharField(blank=True, max_length=500)
    request_client_contacts = models.CharField(blank=True, max_length=500)
    request_reason = models.CharField(blank=True, max_length=500)
    client_rate_appointment = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.appointment_name

