from django.shortcuts import render

# Create your views here.
from timetable.models import Timetable

def timtab(request):
    if request.method=="POST":
        ab=Timetable()
        ab.subject=request.POST.get('sub')
        ab.date=request.POST.get('date')
        ab.time=request.POST.get('time')
        ab.division = request.POST.get('div')
        ab.timetable = request.POST.get('tt')
        ab.save()
    return render(request,'timetable/timetable.html')


from rest_framework.views import APIView,Response
from timetable.serializers import android_serialiser
class view_tt_parent(APIView):
    def get(self,request):
        ob = Timetable.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)