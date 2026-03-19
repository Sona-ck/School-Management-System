from django.urls import path
from attendance import views

urlpatterns = [
    path('atte/', views.attendance),
    path('vwat/', views.vwteachnoti),
]