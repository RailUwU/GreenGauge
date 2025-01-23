from django.shortcuts import render

# Create your views here.
def home_dashboard(request):
    return render(request, 'home/dashboard.html')