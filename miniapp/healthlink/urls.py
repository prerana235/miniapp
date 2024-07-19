from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('doc_login/', views.doc_login, name = "doc_login"),
    path('doc_signup/', views.doc_signup, name = "doc_signup"),
    path('doc_home/', views.doc_home, name = "doc_home"),
    path('logout/', views.doc_logout, name='doc_logout'),
     path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_signup/', views.patient_signup, name='patient_signup'),
    path('patient_home/', views.patient_home, name='patient_home'),
    path('patient_logout/', views.patient_logout, name='patient_logout'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
]
