from django.shortcuts import render

# Create your views he


def home(request):
    return render(request,'temp/home.html')

def teacher(request):
    return render(request,'temp/teacher.html')

def admin_page(request):
    return render(request,'temp/admin.html')

def about(request):
    return render(request, 'temp/about.html')

def contact(request):
    return render(request,'temp/contact.html')