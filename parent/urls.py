from django.urls import path
from . import views
from .views import view_scholarships  # ✅ import the scholarships view

urlpatterns = [
    path('', views.parent_dashboard, name='parent_dashboard'),
    path('register/', views.parent_register, name='parent_register'),
    path('login/', views.parent_login, name='parent_login'),
    path('student/', views.view_student, name='view_student'),
    path('attendance/', views.view_attendance, name='view_attendance'),
    path('result/', views.view_result, name='view_result'),
    path('logout/', views.parent_logout, name='parent_logout'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('view_leave_status/<int:student_id>/', views.view_leave_status, name='view_leave_status'),
    path('view_exams/', views.view_exams, name='view_exams'),
    path('view_notifications/', views.view_notifications, name='view_notifications'),
    path('view_work/', views.view_work, name='view_work'),

    # ------------------ SCHOLARSHIPS ------------------
    path('view-scholarships/', view_scholarships, name='view_scholarships'),
    path('view_transport/', views.view_transport, name='view_transport'),
]