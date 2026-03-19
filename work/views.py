from django.shortcuts import render

# Create your views here.
from work.models import Work

def wrkpst(request):
    if request.method=="POST":
        ab=Work()
        ab.work=request.POST.get('work')
        ab.publish_date = request.POST.get('publish_date')
        ab.end_date = request.POST.get('end_date')
        ab.subject=request.POST.get('subj')
        ab.teach_id=1
        ab.save()
    return render(request,'work/work.html')


from rest_framework.views import APIView,Response
from work.serializers import android_serialiser
class vw_wk_parent(APIView):
    def get(self,request):
        ob = Work.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)