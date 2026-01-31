from accounts.decorators import admin_required
from django.shortcuts import render

# Create your views here.
@admin_required
def admin_booking_list(request):
    return render(request, 'bookings/admin_list.html')