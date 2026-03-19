from django.urls import path
from exam import views

urlpatterns = [
    path('view_parent_exm/', views.view_exam.as_view()),
    path('add/', views.add_exam),
]