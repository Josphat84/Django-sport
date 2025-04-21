
from django.shortcuts import render

def home(request):
    # The 'request' parameter is required by Django views, even if not explicitly used.
    return render(request, "app1/home.html")
