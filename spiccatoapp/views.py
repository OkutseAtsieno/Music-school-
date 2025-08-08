from django.shortcuts import render, redirect
from .models import Enrollment
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request, 'courses.html')

def base(request):
    return render(request,'base.html')

def apply(request):
    return render(request,'apply.html')

def enroll(request):
    return render(request,'enroll.html')


def Gallery(request):
    return render(request, 'Gallery.html')

def enroll_success(request):
    return render(request, 'enroll_success.html')

def video_gallery(request):
    return render(request, 'video_gallery.html')

def home_final(request):
    return render(request, 'home_final.html')

from django.core.mail import send_mail
from django.conf import settings

def enroll_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        guardians_phone_number = request.POST.get('guardians_phone_number')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mode = request.POST.get('mode')
        instrument = request.POST.get('instrument')
        guitar_type = request.POST.get('guitar_type') or 'N/A'
        schedule = request.POST.get('schedule')

        # Send email notification
        subject = 'New Enrollment Submission'
        message = f"""
A new student has enrolled:

Name: {full_name}
Age: {age}
Email: {email}
Phone: {phone}
Guardian's Phone: {guardians_phone_number}
Mode: {mode}
Instrument: {instrument}
Guitar Type: {guitar_type}
Schedule: {schedule}
        """
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # From email
            ['maryokutse@gmail.com'],  
            fail_silently=False,
        )

        # Optionally save the data to the database
        # Enrollment.objects.create(...)

        # Redirect or render success message
        return redirect('enrol_success')


    return render(request, 'apply.html')


def enroll_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        guardians_phone_number = request.POST.get('guardians_phone_number')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mode = request.POST.get('mode')
        instrument = request.POST.get('instrument')
        guitar_type = request.POST.get('guitar_type') or 'N/A'
        schedule = request.POST.get('schedule')

        # Save to database
        Enrollment.objects.create(
            full_name=full_name,
            guardians_phone_number=guardians_phone_number,
            age=age,
            email=email,
            phone=phone,
            mode=mode,
            instrument=instrument,
            guitar_type=guitar_type,
            schedule=schedule,
        )

        # Compose email
        subject = 'New Enrollment Submission'
        body = f"""
Dear Duncan,

A new student has enrolled:

Name: {full_name}
Age: {age}
Email: {email}
Phone: {phone}
Guardian's Phone: {guardians_phone_number}
Mode: {mode}
Instrument: {instrument}
Guitar Type: {guitar_type}
Schedule: {schedule}

Regards,  
Spiccatto Tunes Website
        """

        # Send the email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['musunguduncan9@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Enrollment submitted successfully.")
        return redirect('enroll_success')  

    return render(request, 'apply.html')
