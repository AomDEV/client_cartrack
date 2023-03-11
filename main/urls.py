from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('dropzone-files', views.dropzone_files, name="dropzone-files"),
]