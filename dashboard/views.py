from django.shortcuts import render
from accounts.decorators import admin_required


# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html')

@admin_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin.html')