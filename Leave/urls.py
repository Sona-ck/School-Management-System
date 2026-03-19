from django.urls import path
from Leave import views

urlpatterns = [
   path('view/', views.vw_lv_parent.as_view()),
   path('manage/', views.manage),
   path('accept/<str:idd>/', views.accept),
   path('reject/<str:idd>/', views.reject),
   path('admin_vw/', views.view),
]