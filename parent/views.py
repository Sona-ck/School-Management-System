from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from parent.models import Parent
from login.models import Login

from result.models import Result
from attendance.models import Attendance
from Leave.models import Leave
from exam.models import Exam
from notification.models import Notification
from work.models import Work
from scholarship.models import Scholarship
from student.models import Student
from transport.models import TransportFee
from django.contrib.auth.decorators import login_required

# ------------------ REGISTER ------------------
def parent_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        sid = request.POST.get('sid')
        password = request.POST.get('password')

        parent = Parent.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            sid=sid,
            password=password
        )

        Login.objects.create(
            username=email,
            password=password,
            type='parent',
            u_id=parent.id
        )

        return redirect('/parent/login/')

    return render(request, 'parent/register.html')


# ------------------ LOGIN ------------------
def parent_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        login_obj = Login.objects.filter(
            username=username,
            password=password,
            type='parent'
        ).first()

        if login_obj:
            request.session['u_id'] = login_obj.u_id
            request.session['user_type'] = 'parent'
            return redirect('/parent/')
        else:
            return render(request, 'parent/login.html', {
                'msg': 'Invalid Email or Password'
            })

    return render(request, 'parent/login.html')


# ------------------ DASHBOARD ------------------
def parent_dashboard(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    return render(request, 'parent/dashboard.html', {
        'parent': parent,
        'student': student
    })


# ------------------ STUDENT VIEW ------------------
def view_student(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    results = Result.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student).order_by('-date')
    leaves = Leave.objects.filter(student=student)

    return render(request, 'parent/student.html', {
        'parent': parent,
        'student': student,
        'results': results,
        'attendance': attendance,
        'leaves': leaves
    })


# ------------------ APPLY LEAVE ------------------
def apply_leave(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    if request.method == "POST":
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        no_of_leave = request.POST.get('no_of_leave')

        Leave.objects.create(
            student=student,
            parent=parent,
            date=date,
            reason=reason,
            no_of_leave=no_of_leave,
            status="Pending"
        )

        return redirect('/parent/student/')

    return render(request, 'parent/apply_leave.html')


# ------------------ VIEW LEAVE STATUS ------------------
def view_leave_status(request, student_id):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    student = Student.objects.get(student_id=student_id)
    leaves = Leave.objects.filter(student=student)

    return render(request, 'parent/view_leave_status.html', {
        'student': student,
        'leaves': leaves
    })


# ------------------ ATTENDANCE ------------------
def view_attendance(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    attendance = Attendance.objects.filter(student=student).order_by('-date')

    return render(request, 'parent/attendance.html', {
        'student': student,
        'attendance': attendance
    })


# ------------------ RESULT ------------------
def view_result(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    results = Result.objects.filter(student=student)

    return render(request, 'parent/result.html', {
        'student': student,
        'results': results
    })


# ------------------ EXAMS ------------------
def view_exams(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    exams = Exam.objects.all().order_by('date')

    return render(request, 'parent/view_exams.html', {
        'exams': exams
    })


# ------------------ NOTIFICATIONS ------------------
def view_notifications(request):
    notifications = Notification.objects.all().order_by('-date_posted')

    return render(request, 'parent/view_notifications.html', {
        'notifications': notifications
    })


# ------------------ WORK ------------------
def view_work(request):
    works = Work.objects.all().order_by('-created_at')

    return render(request, 'parent/view_work.html', {
        'works': works
    })


# ------------------ SCHOLARSHIPS ------------------
def view_scholarships(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    scholarships = Scholarship.objects.all().order_by('-created_at')

    # Example eligibility logic (customize as needed)
    eligible_scholarships = []
    for s in scholarships:
        if hasattr(s, 'eligibility_criteria'):
            if f"grade {student.grade}" in s.eligibility_criteria.lower():
                eligible_scholarships.append(s)

    return render(request, 'parent/view_scholarships.html', {
        'parent': parent,
        'scholarships': scholarships,
        'eligible_scholarships': eligible_scholarships
    })


# ------------------ TRANSPORT ------------------
def view_transport(request):
    if 'u_id' not in request.session:
        return redirect('/login/login/')

    parent = Parent.objects.get(id=request.session['u_id'])
    student = Student.objects.get(student_id=parent.sid)

    # Fetch all transport fees for this student
    fees = TransportFee.objects.filter(student=student)

    # Get transport info from those fees
    transports = [fee.transport for fee in fees]

    return render(request, 'parent/view_transport.html', {
        'student': student,
        'fees': fees,
        'transports': transports
    })


# ------------------ LOGOUT ------------------
def parent_logout(request):
    request.session.flush()
    return redirect('/login/login/')