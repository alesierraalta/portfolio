from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Error: El archivo no es un CSV")

        df = pd.read_csv(csv_file)
        # Aquí puedes procesar tu DataFrame como necesites

        return HttpResponse("Archivo procesado con éxito")
    return HttpResponse("Método no permitido")


def index(request):
    return render(request, 'index.html')

def inicio_ml(request):
    return render(request, 'inicioml.html')