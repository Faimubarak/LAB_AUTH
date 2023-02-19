from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import User,Clinic,Appointment
from django.contrib.auth.models import User




# Create your views here.

def home_page(request :HttpRequest):
    Clinics = Clinic.objects.all()
    
    return render(request , 'main/home.html' ,{'Clinics':Clinics} )

def search(request : HttpRequest):
  if request.method=="POST":
        user_input= request.POST['user_input'] 
        clinic =Clinic.objects.filter(name__contains=user_input)
        return render(request, "hospital/search.html", {'clinic':clinic})
    

    

def addClinec (request : HttpRequest):
    if request.user.is_staff:
        if request.method == 'POST':
            new_clinec = Clinic(name = request.POST['name'] , feature_image = request.FILES['feature_image'],description = request.POST['description'] , departments = request.POST['departments'] ,established_at = request.POST['established_at'])
            new_clinec.save()
            return redirect('main:home')
        return render(request , 'main/addCL.html')
    return redirect('patient:signin')  


def upadateclinec(request :HttpRequest , clinec_id):
    if request.user.is_staff:
        updated_clinec=Clinic.objects.get(id = clinec_id)
        updated_clinec.established_at=updated_clinec.established_at.isoformat() 
        if request.method == 'POST':
            updated_clinec.name = request.POST['name'],
            updated_clinec.description=request.POST['description'],
            updated_clinec.departments=request.POST['departments'],
            if "feature_image" in request.FILES:
                updated_clinec.feature_image = request.FILES["feature_image"]
            if "established_at" in request.POST:
                updated_clinec.established_at=request.POST['established_at']   
            updated_clinec.save()
            return redirect('main:allcl')
        return render(request , 'main/updateCl.html',{'updated_clinec':updated_clinec})    
    return redirect('patient:signin')


def deletclinec(request :HttpRequest , clinec_id):
    if request.user.is_staff:
        deleted_clinec = Clinic.objects.get(id=clinec_id)
        deleted_clinec.delete()
        return redirect('main:home')


def show_all_clinec(request:HttpRequest):
    if request.user.is_authenticated:
        if 'search' in request.GET:
            all_clinec = Clinic.objects.filter(name__contains=request.GET["search"])
        else:
            all_clinec = Clinic.objects.all()
        
        return render(request , 'main/controlCL.html' , {'all_clinec':all_clinec})
    return redirect('patient:signin')





def bookForClinec(request :HttpRequest , clinec_id):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
             
            clinec_selected = Clinic.objects.get(id=clinec_id)
            new_appointments = Appointment(appointmentUser = request.user , apclinec = clinec_selected ,case_description=request.POST['case_description'], patient_age = request.POST['patient_age'],appointment_datetime = request.POST['appointment_datetime'] )
            check_dateTime = Appointment.objects.filter(appointment_datetime = request.POST['appointment_datetime'])
            
            if check_dateTime :
                messages.success(request , 'soory chose another date and time')

            else:      
                new_appointments.save()
                return redirect('main:home')
        return render(request,'main/BookAppiontment.html')
    
    

def showUserbook(request : HttpRequest ):
    if request.user.is_authenticated:
        name_of_patient = request.user.get_username    
        show_booked = Appointment.objects.filter(appointmentUser = request.user.id)
        return render(request , 'main/showbook.html', {'show_booked':show_booked , 'name_of_patient':name_of_patient})
    return redirect('patient:signin')
        

    

def veiw_appointmentin_clinec(request : HttpRequest , clinec_id):
    if request.user.is_staff:
        name_of_clinec = Clinic.objects.get(id = clinec_id)
        all_appointment_for_one_clinec = Appointment.objects.filter(apclinec = clinec_id)
        return render (request , 'main/all_appointmentfor_one_CL.html',{'all_appointment_for_one_clinec':all_appointment_for_one_clinec , 'name_of_clinec':name_of_clinec})
    return redirect('main:home')



def control_one_appontment_for_clinec(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        
        slected_appintment = Appointment.objects.get(id = appointment_id)
        
        return render(request,'main/control_appintment_for_patient.html',{'slected_appintment':slected_appintment })
    return redirect('main:home')    



def delete_userappointment_by_admin(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        deleted_appointment = Appointment.objects.get(id = appointment_id)
        deleted_appointment.delete()
        return redirect('main:home')
    

    
def add_appointments_by_admin(request :HttpRequest ):
    user_assigend = User.objects.all()
    clinec_assiend = Clinic.objects.all()
    if request.method == 'POST':
        user = User.objects.get(id = request.POST['appointmentUser'])
        clinec = Clinic.objects.get(id = request.POST['apclinec'])
    
        new_appontment = Appointment(appointmentUser = user ,apclinec = clinec , case_description = request.POST['case_description'] ,patient_age = request.POST['patient_age'],appointment_datetime = request.POST['appointment_datetime'])

        new_appontment.save()
        return redirect('main:home')
    return render(request , 'main/add_appontment_by_admin.html',{'user_assigend':user_assigend , 'clinec_assiend':clinec_assiend})


def update_appointment_by_admin(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        updated_appointment = Appointment.objects.get(id = appointment_id)
        updated_appointment.appointment_datetime=updated_appointment.appointment_datetime.isoformat()
        if request.method == 'POST':
            updated_appointment.case_description=request.POST['case_description'],
            updated_appointment.patient_age = request.POST['patient_age']
            
            updated_appointment.appointment_datetime=request.POST['appointment_datetime']
               
            updated_appointment.is_attended=request.POST['is_attended']
            updated_appointment.save()
            return redirect('main:home') 
        return render(request , 'main/update_appointment_byadmin.html' , {'updated_appointment':updated_appointment}) 