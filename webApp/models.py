from django.db import models
from django.db import connection

# Create your models here.
######################## Gender ########################
class Gender(models.Model):
	id_centers = models.IntegerField()
	name = models.TextField(unique = True)
	description = models.TextField()


######################## HealthEntity ########################
class HealthEntity(models.Model):
	id_entity = models.IntegerField()
	name = models.TextField(unique = True)
	description = models.TextField()


######################## Medical Speciality ########################
class MedicalSpeciality(models.Model):
	id_speciality = models.IntegerField()
	name = models.TextField(unique = True)
	description = models.TextField()


######################## Medical Center ########################
class Center(models.Model):
	id_center = models.IntegerField()	
	name = models.TextField()
	address = models.TextField()
	attention_schedule = models.TextField()
	phone = models.TextField()
	latitude = models.DecimalField(max_digits=12,decimal_places=8)
	longitude = models.DecimalField(max_digits=12,decimal_places=8)


######################## Patient ########################
class Patient(models.Model):
	id_patient = models.IntegerField()
	name  = models.TextField()
	gender_fk = models.ForeignKey(Gender, on_delete = models.CASCADE)
	diagnostic = models.TextField(default = "")
	email = models.TextField()
	phone = models.IntegerField()
	birthday = models.DateTimeField() 
	entity_fk = models.ForeignKey(HealthEntity, on_delete = models.CASCADE)
	address = models.TextField()
	register_date = models.DateTimeField() 


######################## Therapist ########################
class Therapist(models.Model):
	id_therapist = models.IntegerField()
	name = models.TextField()
	register_date = models.DateTimeField() 
	password = models.TextField()
	center_fk = models.ForeignKey(Center, on_delete = models.CASCADE)
	email = models.TextField()
	speciality_fk = models.ForeignKey(MedicalSpeciality, on_delete = models.CASCADE)


######################## Therapy ########################
class Therapy(models.Model):
	id_therapy = models.IntegerField()
	date_therapy = models.DateTimeField() 
	elapsed_time = models.TextField()
	observations = models.TextField()
	therapist_fk = models.ForeignKey(Therapist, on_delete = models.CASCADE)
	center_fk = models.ForeignKey(Center, on_delete = models.CASCADE)







