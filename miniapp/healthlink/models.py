from django.db import models


# Doctor model
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Patient model
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# MessageBox model
class MessageBox(models.Model):
    sender_id = models.IntegerField()  # Foreign Key to Doctor or Patient (customize as needed)
    recipient_id = models.IntegerField()  # Foreign Key to Doctor or Patient (customize as needed)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender_id} to {self.recipient_id}'

# Medicine model
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.patient_id.name}'

# Appointment model
class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'Appointment with {self.doctor_id.name}'

