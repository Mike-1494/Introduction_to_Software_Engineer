from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return render(request, 'index.html')