# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Doctor, Appointment, MessageBox, Patient
from django.http import JsonResponse
def home(request):
    return render(request, "home.html")

def doc_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            doctor = Doctor.objects.get(email=email)
            if doctor.password == password:
                # Set session or other login mechanism
                request.session['doctor_id'] = doctor.id
                return redirect('doc_home')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, "Invalid email or password.")
        except Doctor.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    return render(request, 'doc_login.html')

def doc_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        specialization = request.POST['specialization']
        phone_number = request.POST['phone_number']
        
        if not Doctor.objects.filter(email=email).exists():
            Doctor.objects.create(name=name, email=email, password=password, specialization=specialization, phone_number=phone_number)
            messages.success(request, "Account created successfully.")
            return redirect('doc_login')
        else:
            messages.error(request, "Email already exists.")
    return render(request, 'doc_signup.html')

def doc_home(request):
    if 'doctor_id' in request.session:
        doctor_id = request.session['doctor_id']
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor_id=doctor_id)
        messages_received = MessageBox.objects.filter(recipient_id=doctor_id)
        messages_sent = MessageBox.objects.filter(sender_id=doctor_id)
        patients = Patient.objects.all()
        return render(request, "doc_home.html", {
            "doctor": doctor,
            "appointments": appointments,
            "messages_received": messages_received,
            "messages_sent": messages_sent,
            "patients": patients
        })
    return redirect('doc_login')

def doc_logout(request):
    request.session.flush()
    return redirect('doc_login')

def send_message(request):
    if request.method == "POST":
        sender_id = request.session.get('doctor_id') or request.session.get('patient_id')
        recipient_id = request.POST['recipient_id']
        message = request.POST['message']
        
        MessageBox.objects.create(sender_id=sender_id, recipient_id=recipient_id, message=message)
        return HttpResponse("Message sent successfully.")
    
    return HttpResponse("Invalid request.")

def get_messages(request):
    if 'doctor_id' in request.session:
        user_id = request.session['doctor_id']
    elif 'patient_id' in request.session:
        user_id = request.session['patient_id']
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    messages_received = MessageBox.objects.filter(recipient_id=user_id).values()
    messages_sent = MessageBox.objects.filter(sender_id=user_id).values()

    return JsonResponse({
        'messages_received': list(messages_received),
        'messages_sent': list(messages_sent)
    })

def patient_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            patient = Patient.objects.get(email=email)
            if patient.password == password:
                # Set session or other login mechanism
                request.session['patient_id'] = patient.id
                return redirect('patient_home')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, "Invalid email or password.")
        except Patient.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    return render(request, 'patient_login.html')

def patient_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        
        if not Patient.objects.filter(email=email).exists():
            Patient.objects.create(name=name, email=email, password=password, date_of_birth=date_of_birth, phone_number=phone_number)
            messages.success(request, "Account created successfully.")
            return redirect('patient_login')
        else:
            messages.error(request, "Email already exists.")
    return render(request, 'patient_signup.html')

def patient_home(request):
    if 'patient_id' in request.session:
        patient_id = request.session['patient_id']
        patient = Patient.objects.get(id=patient_id)
        doctors = Doctor.objects.all()
        appointments = Appointment.objects.filter(patient_id=patient_id)
        messages_received = MessageBox.objects.filter(recipient_id=patient_id)
        messages_sent = MessageBox.objects.filter(sender_id=patient_id)
        return render(request, "patient_home.html", {
            "patient": patient,
            "doctors": doctors,
            "appointments": appointments,
            "messages_received": messages_received,
            "messages_sent": messages_sent
        })
    return redirect('patient_login')

def patient_logout(request):
    request.session.flush()
    return redirect('patient_login')

def make_appointment(request):
    if request.method == "POST":
        patient_id = request.session['patient_id']
        doctor_id = request.POST['doctor_id']
        date = request.POST['date']
        description = request.POST['description']

        Appointment.objects.create(doctor_id_id=doctor_id, patient_id_id=patient_id, date=date, description=description)
        messages.success(request, "Appointment made successfully.")
        return redirect('patient_home')

