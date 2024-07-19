from django.contrib import admin
from .models import Doctor, Patient, MessageBox, Medicine, Order, Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MessageBox)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(Appointment)
