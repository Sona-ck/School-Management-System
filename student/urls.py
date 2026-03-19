from django.urls import path
from student import views

urlpatterns = [
    path('stdreg/', views.stdreg),
    path('delstd/<int:idd>/', views.delstd),
    path('mngstd/', views.mngstd),
    path('admin/', views.admin),
    path('abc/', views.parent_vw.as_view()),
    path('bbb/', views.leave.as_view()),
]