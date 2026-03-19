"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('attendance/', include('attendance.urls')),
    path('clubactivity/', include('clubactivity.urls')),
    path('exam/', include('exam.urls')),
    path('Leave/', include('Leave.urls')),
    path('login/', include('login.urls')),
    path('notification/', include('notification.urls')),
    path('parent/', include('parent.urls')),
    path('result/', include('result.urls')),
    path('scholarship/', include('scholarship.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('timetable/', include('timetable.urls')),
    path('transport/', include('transport.urls')),
    path('work/', include('work.urls')),

    path('', include('temp.urls')),
]
