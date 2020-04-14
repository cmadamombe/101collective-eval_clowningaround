'''
API Views
These API functions are for CRUD Operations:
– appointment_list(): GET list of appointments, POST a new appointment, DELETE all appointments
– appointment_detail(): GET / PUT / DELETE appointment by ‘id’
'''

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from clowning_around.appointments.models import Appointment
from clowning_around.appointments.serializers import AppointmentSerializer
from rest_framework.decorators import api_view

#Retrieve all appointments/ find appointments by appointments status from the database:
@api_view(['GET', 'POST', 'DELETE'])
def appointment_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()

        appointment_status = request.GET.get('title', None)
        if appointment_status is not None:
            appointments = appointments.filter(Appointment_Status__Description=appointment_status)

        tutorials_serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    #Create and Save a new Appointment into the database (create a new object):
    elif request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        appointment_serializer = AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete all appointments from the database:
    elif request.method == 'DELETE':
        count = Appointment.objects.all().delete()
        return JsonResponse({'message': '{} Appointments were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

#Find a single appointment with an id:
@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        appointment_serializer = AppointmentSerializer(appointment)
        return JsonResponse(appointment_serializer.data)

#Update an appointment by the id in the request
    elif request.method == 'PUT':
        appointment_data = JSONParser().parse(request)
        appointment_serializer = AppointmentSerializer(appointment, data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data)
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete an appointment with the specified id:
    elif request.method == 'DELETE':
        appointment.delete()
        return JsonResponse({'message': 'Appointment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

