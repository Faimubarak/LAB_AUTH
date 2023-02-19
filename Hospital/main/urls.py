from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('',views.home_page, name='home'),
    path("search/", views.search, name="search" ),
    path('addclinec/', views.addClinec , name='addclinec'),
    path('showall/',views.show_all_clinec,name='allcl'),
    path('update/<clinec_id>' ,views.upadateclinec,name='update'),
    path('delete/<clinec_id>' , views.deletclinec , name='delete'),
    path('addapontment/<clinec_id>' , views.bookForClinec, name='booking'),
    path('showbook/' , views.showUserbook , name="showbook"),
    path('allapointment/<clinec_id>',views.veiw_appointmentin_clinec,name='all_appointment'),
    path('CMapoontmentForClinec/<appointment_id>',views.control_one_appontment_for_clinec,name='cmappontment'),
    path('deleteAppointmentByAdmin/<appointment_id>' , views.delete_userappointment_by_admin,name='deleteappointmentByAdmin'),
    path('addappontmentbyAdmin/' , views.add_appointments_by_admin , name = 'addapontmentbyadmin'),
    path('updateappointmentbyadmin/<appointment_id>' , views.update_appointment_by_admin , name='updateappointmentByAdmin'),
    


    
]