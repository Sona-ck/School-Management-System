from django.shortcuts import render

# Create your views here.
from student.models import Student

def stdreg(request):
    if request.method=="POST":
        ab=Student()
        ab.name=request.POST.get('name')
        ab.address=request.POST.get('address')
        ab.email=request.POST.get('email')
        ab.class_field=request.POST.get('class')
        ab.division=request.POST.get('div')
        ab.gender=request.POST.get('gender')
        ab.fname=request.POST.get('fname')
        ab.mname=request.POST.get('mname')
        ab.father_occupation=request.POST.get('father_occupation')
        ab.mother_occupation=request.POST.get('mother_occupation')
        ab.dob=request.POST.get('dob')
        ab.aadhar=request.POST.get('aadhar')
        ab.income=request.POST.get('income')
        ab.phone_number= request.POST.get('phone')
        ab.nativity = request.POST.get('nativity')
        ab.ncl_class = request.POST.get('ncl_class')
        ab.caste = request.POST.get('caste')
        ab.save()
    return render(request,'student/stdreg.html')


def mngstd(request):
    ab=Student.objects.all()
    context={
        'a':ab
    }
    return render(request,'student/manageteach.html',context)

def admin(request):
    ab=Student.objects.all()
    context={
        'a':ab
    }
    return render(request,'student/view.html',context)


def delstd(request,idd):
    bb=Student.objects.get(student_id=idd)
    bb.delete()
    return mngstd(request)

from rest_framework.views import APIView,Response
from student.serializers import android_serialiser

class parent_vw(APIView):
    def get(self,request):
        ob = Student.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)

class leave(APIView):
    def get(self,request):
        ob = Student.objects.all()
        ser = android_serialiser(ob,many=True)
        return Response(ser.data)
