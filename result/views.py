from django.shortcuts import render
from django.http import HttpResponse
from result.models import Result
from student.models import Student


def resul(request):

    students = Student.objects.all()

    if request.method == "POST":

        student_id = request.POST.get('std')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')

        try:
            student = Student.objects.get(student_id=student_id)  # ✅ FIXED

            Result.objects.create(
                student=student,
                subject=subject,
                marks=marks
            )

            return render(request, 'result/resultp.html', {
                'a': students,
                'message': 'Result Added Successfully'
            })

        except Student.DoesNotExist:
            return HttpResponse("Student not found")

    return render(request, 'result/resultp.html', {
        'a': students
    })