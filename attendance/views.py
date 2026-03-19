from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from attendance.models import Attendance
from teacher.models import Teacher


def attendance(request):

    teacher_id = request.session.get("u_id")

    if not teacher_id:
        return HttpResponse("Session Expired. Please login again.")

    try:
        teacher = Teacher.objects.get(teacher_id=teacher_id)
    except Teacher.DoesNotExist:
        return HttpResponse("Teacher not found.")

    if request.method == 'POST' and 'search' in request.POST:

        cl = request.POST.get("cls")
        div = request.POST.get("divi")

        request.session['cl'] = cl
        request.session['div'] = div

        students = Student.objects.filter(class_field=cl, division=div)

        return render(request, 'attendance/postattend.html', {'std': students})

    if request.method == 'POST' and 'submit' in request.POST:

        cl = request.session.get('cl')
        div = request.session.get('div')
        date = request.POST.get("dat")

        if not cl or not div:
            return HttpResponse("Please search class first.")

        if not date:
            return HttpResponse("Please select a date.")

        students = Student.objects.filter(class_field=cl, division=div)

        for student in students:

            checkbox_value = request.POST.get("ch" + str(student.student_id))

            status = "Present" if checkbox_value else "Absent"

            exists = Attendance.objects.filter(
                student=student,
                date=date
            ).exists()

            if not exists:
                Attendance.objects.create(
                    student=student,
                    status=status,
                    date=date,
                    teacher=teacher   # optional if exists
                )

        return render(request, 'attendance/postattend.html', {
            'std': students,
            'message': 'Attendance Saved Successfully'
        })

    return render(request, 'attendance/postattend.html')


def vwteachnoti(request):

    attendance_records = Attendance.objects.select_related('student').all().order_by('-date')

    return render(request, 'attendance/vwatte.html', {
        'a': attendance_records
    })