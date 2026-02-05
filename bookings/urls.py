from django.urls import path
from .views import create_booking, my_bookings

urlpatterns = [
    path('create/', create_booking, name='create_booking'),
    path('my/', my_bookings, name='my_bookings'),

]