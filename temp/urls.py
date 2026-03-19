from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('teacher/', views.teacher, name='teacher'),
    path('admin-page/', views.admin_page, name='admin_page'),

    path('about/', views.about, name='about'),

]