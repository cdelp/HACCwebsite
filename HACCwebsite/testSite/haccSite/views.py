from django.shortcuts import render

def index(request):
    return render(request, 'haccSite/home.html')

# Create your views here.
