from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloworld(request):
    return HttpResponse("Helloworld!!!")

def index(request):
    return render(request, 'index.html', context={'hello_message': 'ttt'})