from django.shortcuts import render, redirect, get_object_or_404
from .models import TransportFee, Transport
from student.models import Student

# ------------------ Add Transport Fee ------------------
def trans(request):
    if request.method == "POST":
        # Get data from form
        student_id = request.POST.get('student_id')
        transport_id = request.POST.get('transport_id')
        month = request.POST.get('month')  # format: 'YYYY-MM-DD', first day of month
        amount = request.POST.get('amount')
        status = request.POST.get('status', 'Pending')

        # Get corresponding Student and Transport objects
        student = get_object_or_404(Student, id=student_id)
        transport = get_object_or_404(Transport, id=transport_id)

        # Create and save TransportFee
        fee = TransportFee(
            student=student,
            transport=transport,
            month=month,
            amount=amount,
            status=status
        )
        fee.save()
        return redirect('view_transport_fees')  # Replace with your actual URL name for viewing all fees

    # For GET request, send students and transports to template
    students = Student.objects.all()
    transports = Transport.objects.all()
    return render(request, 'transport/transp.html', {
        'students': students,
        'transports': transports
    })


# ------------------ View All Transport Fees ------------------
def view(request):
    fees = TransportFee.objects.all()
    return render(request, 'transport/view.html', {
        'fees': fees
    })


# ------------------ Parent View: Transport Fees ------------------
def parent_transport_fees(request, student_id):
    # Get all transport fees for this student
    fees = TransportFee.objects.filter(student_id=student_id)

    # Optionally, get all transports assigned to this student
    transports = [fee.transport for fee in fees]

    return render(request, 'transport/parent_transport_fees.html', {
        'fees': fees,
        'transports': transports,
        'student_id': student_id
    })