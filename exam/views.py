from django.shortcuts import render
from exam.models import Exam


def add_exam(request):
    ss = request.session["u_id"]

    if request.method == 'POST':
        obj = Exam()
        obj.subject = request.POST.get('sub')
        obj.teacher_id = ss
        obj.exam_name = request.POST.get('exname')
        obj.schedule = request.POST.get('sch')
        obj.date = request.POST.get('date')
        obj.time = request.POST.get('time')
        obj.save()

    return render(request, 'exam/add_exam.html')

from rest_framework.views import APIView,Response
from exam.serializers import android_serialiser
class view_exam(APIView):
    def get(self,request):
        ob = Exam.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)