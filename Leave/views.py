from django.http import HttpResponse
from django.shortcuts import render
from Leave.models import Leave
# Create your views here.



from rest_framework.views import APIView,Response
from Leave.serializers import android_serialiser
class vw_lv_parent(APIView):
    def post(self,request):
        ob = Leave()
        ob.student_id=1
        ob.no_of_leave=request.data['no_of_leave']
        ob.reason=request.data['reason']
        ob.parent_id=1
        ob.status='pending'
        return HttpResponse('yes')


def manage(request):
    obj=Leave.objects.all()
    context={
        'x':obj
    }
    return render(request,'Leave/view_manage.html',context)

def view(request):
    obj=Leave.objects.all()
    context={
        'x':obj
    }
    return render(request,'Leave/view.html',context)

def accept(request,idd):
    obj=Leave.objects.get(lv_id=idd)
    obj.status='Accepted'
    obj.save()
    return manage(request)

def reject(request,idd):
    obj=Leave.objects.get(lv_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage(request)