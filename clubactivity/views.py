from django.shortcuts import render

# Create your views here.
from clubactivity.models import Clubactivity

def clb(request):
    if request.method=="POST":
        abb=Clubactivity()
        abb.club=request.POST.get('Club')
        abb.activity=request.POST.get('Activity')
        abb.save()
    return render(request,'clubactivity/clb.html')


def vw(request):
    ab=Clubactivity.objects.all()
    context={
        'a':ab
    }
    return render(request,'clubactivity/vw.html',context)

from rest_framework.views import APIView,Response
from clubactivity.serializers import android_serialiser
class view_club_parent(APIView):
    def get(self,request):
        ob = Clubactivity.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)