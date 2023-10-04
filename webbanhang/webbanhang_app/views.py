from django.shortcuts import render
from django.http import HTTPResponse

def my_view(request):
    return render(request, 'index.html')