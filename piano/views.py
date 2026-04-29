from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'piano/pages/index.html')

def about(request):
    return render(request, 'piano/pages/about.html')

def contact(request):
    return render(request, 'piano/pages/contact.html')

def classes(request):
    return render(request, 'piano/pages/classes.html')

def usp(request):
    return render(request, 'piano/pages/usp.html')