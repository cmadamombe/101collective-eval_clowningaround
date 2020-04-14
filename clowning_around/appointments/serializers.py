from rest_framework import serializers
from clowning_around.appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer): #class that will manage serialization and deserialization from JSON.
    class Meta:
        model = Appointment
        fields = "__all__"