from django.shortcuts import render, redirect
from notification.models import Notification
# -----------------------------
# Post Notification (Admin)
# -----------------------------
def noti(request):

    if request.method == "POST":

        title = request.POST.get('notification')
        message = request.POST.get('message')
        priority = request.POST.get('priority')

        if title and message:

            Notification.objects.create(
                notification=title,
                message=message,
                priority=priority
            )

            return redirect('/notification/noti/')

    return render(request, 'notification/postnoti.html')


# -----------------------------
# View Notifications (Teacher Web)
# -----------------------------
def vwteachnoti(request):

    notifications = Notification.objects.all().order_by('-date_posted')

    context = {
        'notifications': notifications
    }

    return render(request, 'notification/viewnotireacher.html', context)


# -----------------------------
# API for Flutter Parent App
# -----------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from notification.serializers import android_serialiser


class ViewParent(APIView):

    def get(self, request):

        notifications = Notification.objects.all().order_by('-date_posted')

        serializer = android_serialiser(notifications, many=True)

        return Response(serializer.data)