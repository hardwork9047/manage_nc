# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-room/', views.add_room, name='add_room'),
    path('select-tables/', views.select_tables, name='select_tables'),
]
