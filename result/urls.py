from django.urls import path
from result import views

urlpatterns=[
    path('res/',views.resul),
    #path('view_parent/',views.view_res_parent.as_view())
    # url('vwtach/',views.vwteachnoti),
    # url('parvw/',views.vwnotiparent)
]