from django.urls import path
from notification import views

urlpatterns = [
    path('noti/', views.noti),
    path('view/', views.vwteachnoti),
    path('parvw/', views.ViewParent.as_view()),
]