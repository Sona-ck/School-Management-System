from django.urls import path
from work import views

urlpatterns=[
    path('work/',views.wrkpst),
    path('view/',views.vw_wk_parent.as_view())
    # url('vwtach/',views.vwteachnoti),
]