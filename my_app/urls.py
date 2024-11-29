from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ia', views.action_move, name='action_move'),
    path('terminal', views.terminal_view, name='terminal_view'),
    path("winner", views.winner_view, name='winner_view'),
]