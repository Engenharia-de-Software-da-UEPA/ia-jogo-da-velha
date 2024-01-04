from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ia', views.action_move, name='action_move'),
]