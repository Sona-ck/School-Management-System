from django.urls import path
from . import views
from .views import view_scholarships  # import the new scholarship view

urlpatterns = [
    # Teacher authentication
    path('techreg/', views.teacher_register, name='teacher_register'),
    path('techlogin/', views.teacher_login, name='teacher_login'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('logout/', views.teacher_logout, name='teacher_logout'),

    # Teacher management
    path('view_teach/', views.manage_teachers, name='view_teachers'),
    path('dlt/<int:idd>/', views.delete_teacher, name='delete_teacher'),  # idd matches views.py
    path('updd/<int:idd>/', views.update_teacher, name='update_teacher'),

    # Attendance & results
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('add-result/', views.add_result, name='add_result'),

    # Leave management
    path('view_leaves/', views.view_leaves, name='view_leaves'),
    path('approve_leave/<int:id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:id>/', views.reject_leave, name='reject_leave'),

    # Notifications
    path('add_notification/', views.add_notification, name='add_notification'),

    # Scholarship
    path('upload-scholarship/', views.ScholarshipCreateView.as_view(), name='upload_scholarship'),
    path('view-scholarships/', view_scholarships, name='view_scholarships'),  # new view
]