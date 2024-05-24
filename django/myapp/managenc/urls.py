# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-room/', views.add_room, name='add_room'),
    path('select-tables/', views.select_tables, name='select_tables'),
    path('update-ready-to-work/', views.update_ready_to_work, name='update_ready_to_work'),
    path('update-work-to-done/', views.update_work_to_done, name='update_work_to_done'),
    path('update-status-to-ready/', views.update_status_to_ready, name='update_status_to_ready'),
    path('update-status-to-clear/', views.update_status_to_clear, name='update_status_to_clear'),
]
