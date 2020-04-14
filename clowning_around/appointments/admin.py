from django.contrib import admin
from .models import Appointment_Status, Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('appointment_name', 'appointment_date', 'appointment_status', 'clown', 'client', 'report_issue', 'request_client_contacts', 'request_reason', 'client_rate_appointment')
    list_filter = ('appointment_status', 'clown',
                   'client')  # The list_filter option
    ordering = ('appointment_date',)
    search_fields = (
    'appointment_name', 'appointment_status')  # sets the default search fields.

admin.site.register(Appointment_Status)

