from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.convert_currency, name='convert_currency')
]