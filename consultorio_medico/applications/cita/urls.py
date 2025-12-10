from django.urls import path, re_path, include

from . import views

app_name = 'citas_app'

urlpatterns = [
    path('new-cita', views.CreateCitaApiView.as_view(), name='new_cita'),
]