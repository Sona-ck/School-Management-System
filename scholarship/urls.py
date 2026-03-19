from django.urls import path
from scholarship import views

urlpatterns = [
    path('sch/', views.sch),
    path('v/', views.vwsch),
    path('view_parent/', views.view_sch_par.as_view()),
    path('approve/', views.aprv.as_view()),
    path('manage/', views.manage),

    path('approve/<str:idd>/', views.accepted),
    path('reject/<str:idd>/', views.reject),
    path('edit/<str:idd>/', views.edit),
    path('delete/<str:idd>/', views.delete),
]