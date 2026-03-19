from django.urls import path
from clubactivity import views

urlpatterns = [
    path('clb/', views.clb),
    path('vcl/', views.vw),
    path('view/', views.view_club_parent.as_view()),
]