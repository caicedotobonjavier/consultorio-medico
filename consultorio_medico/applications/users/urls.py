from django.urls import path

from . import views

app_name = 'user_app'

urlpatterns = [
    path('create-user', views.CreateUserApiView.as_view(), name='create'),
    path('activate-user', views.VerficationCodeApiView.as_view(), name='activate'),
]
