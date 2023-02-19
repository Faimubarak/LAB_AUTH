from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=512)
    feature_image=models.ImageField(upload_to="images/")
    description = models.TextField()
    
    HeartCenter = 'HC'
    NeuroscienceCenter = 'NC'
    ObesityCenter = 'OC'
    EyeCenter = 'EC'
    OrthopedicCenter = 'OcC'
    PediatricCenter='PC'
    not_assigen = 'NL'
    departments = [
        (HeartCenter, 'HeartCenter'),
        (NeuroscienceCenter, 'NeuroscienceCenter'),
        (ObesityCenter, 'ObesityCenter'),
        (EyeCenter, 'EyeCenter'),
        (OrthopedicCenter, 'OrthopedicCenter'),
    ]
    departments = models.CharField(
        max_length=3,
        choices=departments,
        default=not_assigen,
    )

    established_at=models.DateField()



class Appointment(models.Model):
    appointmentUser = models.ForeignKey(User,on_delete=models.CASCADE)
    apclinec = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    case_description=models.TextField()
    patient_age=models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)
    