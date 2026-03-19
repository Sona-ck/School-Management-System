# transport/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Add a new transport entry
    path('add/', views.trans, name='add_transport'),

    # View all transport entries
    path('view/', views.view, name='view_transport'),

    # View transport fees for a specific student by ID
    path('parent/<int:student_id>/', views.parent_transport_fees, name='parent_transport_fees'),
]