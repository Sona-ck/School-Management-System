from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView

from .models import Teacher
from .forms import TeacherRegistrationForm, TeacherLoginForm, ScholarshipForm
from student.models import Student
from Leave.models import Leave
from attendance.models import Attendance
from result.models import Result
from notification.models import Notification
from work.models import Work
from scholarship.models import Scholarship

# ------------------ TEACHER REGISTRATION ------------------
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('teacher_login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher/register.html', {'form': form})

# ------------------ TEACHER LOGIN ------------------
def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('teacher_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = TeacherLoginForm()
    return render(request, 'teacher/login.html', {'form': form})

# ------------------ TEACHER DASHBOARD ------------------
@login_required(login_url='teacher_login')
def teacher_dashboard(request):
    teacher = request.user
    return render(request, 'teacher/dashboard.html', {'teacher': teacher})

# ------------------ TEACHER LOGOUT ------------------
@login_required(login_url='teacher_login')
def teacher_logout(request):
    logout(request)
    return redirect('teacher_login')

# ------------------ MANAGE TEACHERS ------------------
@login_required(login_url='teacher_login')
def manage_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/view_teacher.html', {'teachers': teachers})

# ------------------ DELETE TEACHER ------------------
@login_required(login_url='teacher_login')
def delete_teacher(request, idd):
    teacher = get_object_or_404(Teacher, id=idd)
    teacher.delete()
    messages.success(request, "Teacher deleted successfully!")
    return redirect('view_teachers')

# ------------------ UPDATE TEACHER ------------------
@login_required(login_url='teacher_login')
def update_teacher(request, idd):
    teacher = get_object_or_404(Teacher, id=idd)
    if request.method == "POST":
        teacher.phone = request.POST.get('phone', teacher.phone)
        teacher.qualification = request.POST.get('qualification', teacher.qualification)
        teacher.save()
        messages.success(request, "Teacher updated successfully!")
        return redirect('view_teachers')
    return render(request, 'teacher/update.html', {'teacher': teacher})

# ------------------ VIEW TEACHERS (ADMIN) ------------------
@login_required(login_url='teacher_login')
def view_teachers_admin(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/view_teachers_admin.html', {'teachers': teachers})

# ------------------ ATTENDANCE ------------------
@login_required(login_url='teacher_login')
def add_attendance(request):
    students = Student.objects.all()
    if request.method == "POST":
        student_id = request.POST.get('student')
        date = request.POST.get('date')
        status = request.POST.get('status')
        student = get_object_or_404(Student, id=student_id)
        Attendance.objects.create(student=student, date=date, status=status)
        messages.success(request, "Attendance added successfully!")
        return redirect('add_attendance')
    return render(request, 'teacher/add_attendance.html', {'students': students})

# ------------------ RESULTS ------------------
@login_required(login_url='teacher_login')
def add_result(request):
    students = Student.objects.all()
    if request.method == "POST":
        student_id = request.POST.get('student')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')
        student = get_object_or_404(Student, id=student_id)
        Result.objects.create(student=student, subject=subject, marks=marks)
        messages.success(request, "Result added successfully!")
        return redirect('add_result')
    return render(request, 'teacher/add_result.html', {'students': students})

# ------------------ LEAVE MANAGEMENT ------------------
@login_required(login_url='teacher_login')
def view_leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'teacher/manage_leave.html', {'leaves': leaves})

@login_required(login_url='teacher_login')
def approve_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    leave.status = "Approved"
    leave.save()
    messages.success(request, "Leave approved successfully!")
    return redirect('view_leaves')

@login_required(login_url='teacher_login')
def reject_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    leave.status = "Rejected"
    leave.save()
    messages.success(request, "Leave rejected successfully!")
    return redirect('view_leaves')

# ------------------ NOTIFICATIONS ------------------
@login_required(login_url='teacher_login')
def add_notification(request):
    if request.method == "POST":
        title = request.POST.get('title')
        message = request.POST.get('message')
        priority = request.POST.get('priority')
        Notification.objects.create(notification=title, message=message, priority=priority)
        messages.success(request, "Notification added successfully!")
        return redirect('add_notification')
    return render(request, 'teacher/add_notification.html')

# ------------------ SCHOLARSHIP UPLOAD (CBV) ------------------
class ScholarshipCreateView(CreateView):
    model = Scholarship
    form_class = ScholarshipForm
    template_name = 'teacher/upload_scholarship.html'
    success_url = '/teacher/upload-scholarship/'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

# ------------------ VIEW SCHOLARSHIPS ------------------
@login_required(login_url='teacher_login')
def view_scholarships(request):
    scholarships = Scholarship.objects.all().order_by('-created_at')
    return render(request, 'teacher/view_scholarships.html', {'scholarships': scholarships})