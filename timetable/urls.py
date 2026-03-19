from django.urls import path
from timetable import views

urlpatterns=[
    path('tt/',views.timtab),
    path('view_tt_par/',views.view_tt_parent.as_view())
    # url('vwsch/',views.vwsch),
# ]]
]