from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio-ml/', views.inicio_ml, name='inicioml'),
    path('upload-file/', views.upload_file, name='upload_file'),

]
