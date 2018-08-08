from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_clients(request):
    return HttpResponse('Hello, from Django!')
