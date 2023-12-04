from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def inicio_ml(request):
    return render(request, 'inicioml.html')