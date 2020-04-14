from django.conf.urls import url
from clowning_around.appointments import views

'''When a client sends request for an endpoint using HTTP request (GET, POST, PUT, DELETE), 
we need to determine how the server will response by defining the routes.
These are our routes:
/api/appointments: GET, POST, DELETE
/api/appointments/:id: GET, PUT, DELETE
'''
app_name = "appointments"

urlpatterns = [
    url(r'^api/appointments$', views.appointment_list),
    url(r'^api/appointments/(?P<pk>[0-9]+)$', views.appointment_detail),
]
