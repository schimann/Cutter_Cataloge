from django.urls import path
from . import views


urlpatterns = [
    path('', views.cutter_list, name='cutter_list'),
]
