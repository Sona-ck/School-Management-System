from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from scholarship.models import Scholarship

def sch(request):
    if request.method=="POST":
        ab=Scholarship()
        ab.scholarship=request.POST.get('schl')
        ab.details=request.POST.get('dst')
        ab.status='pending'
        ab.sc_status='pending'
        ab.atype=request.POST.get('cat')
        ab.publish_date = request.POST.get('publish_date')
        ab.end_date=request.POST.get('end_date')
        ab.save()
    return render(request,'scholarship/scholarship.html')


def vwsch(request):
    ab=Scholarship.objects.all()
    context={
        'a':ab
    }
    return render(request,'scholarship/viewsch.html',context)

def manage(request):
    ab=Scholarship.objects.all()
    context={
        'a':ab
    }
    return render(request,'scholarship/view_application.html',context)

from django.http import HttpResponseRedirect
def edit(request,idd):
    ab=Scholarship.objects.get(scholar_id=idd)
    context={
        'sc':ab,
    }

    if request.method=="POST":
        ab.scholarship = request.POST.get('schl')
        ab.details = request.POST.get('dst')
        ab.status = 'pending'
        ab.sc_status = 'pending'
        ab.atype = request.POST.get('cat')
        ab.publish_date = request.POST.get('publish_date')
        ab.end_date = request.POST.get('end_date')
        ab.save()
        return HttpResponseRedirect('/scholarship/manage/')


    return render(request, 'scholarship/scholarship.html',context)
    # obj.sc_status='Accepted'
    # obj.save()

    # return manage(request)
def delete(request,idd):
    ab=Scholarship.objects.get(scholar_id=idd)
    context={
        'sc':ab,
    }

    if request.method=="POST":
        ab.delete()
        return HttpResponseRedirect('/scholarship/manage/')


    return render(request, 'scholarship/scholarship.html',context)
    # obj.sc_status='Accepted'
    # obj.save()

    # return manage(request)

def accepted(request,idd):
    obj=Scholarship.objects.get(scholar_id=idd)
    obj.sc_status='Accepted'
    obj.save()
    return manage(request)

def reject(request,idd):
    obj=Scholarship.objects.get(scholar_id=idd)
    obj.sc_status='Rejected'
    obj.save()
    return manage(request)


from rest_framework.views import APIView,Response
from scholarship.serializers import android_serialiser
class view_sch_par(APIView):
    def get(self,request):
        ob = Scholarship.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)


class aprv(APIView):
    def post(self,request):
        ab=Scholarship.objects.get(scholar_id=request.data['scid'])
        ab.status="Applied"
        ab.save()
        return HttpResponse("yess")