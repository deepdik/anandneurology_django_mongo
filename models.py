from django.db import models

# Create your models here.

GENDER = (('male','Male'),('female','Female'),('unknown','Unknown'))

class Disease(models.Model):
	name 		= models.CharField(max_length=120)
	des 		= models.TextField()

	def __str__(self):
		return self.name


class Patient(models.Model):
	name 		= 	models.CharField(max_length=120)
	age 		= 	models.PositiveIntegerField()	
	gender 		= 	models.CharField(max_length=120, choices=GENDER)
	dob			= 	models.DateField(blank=True)
	mobileNo    =   models.CharField(max_length=10)
	address		= 	models.TextField(blank=True)
	timestamp 	= 	models.DateTimeField(auto_now_add=True)
	patientimg	=	models.ImageField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patients"

class PatientReport(models.Model):
	patient    	= models.ForeignKey(Patient, related_name = 'patient')
	Date 		= models.DateField()
	weight  	= models.SmallIntegerField()
	Pblm 		= models.TextField(blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patients"


class MeetingRecord(models.Model):
	patient    	= models.ForeignKey(Patient, related_name = 'patient')
	Date 		= models.DateField()
	weight  	= models.SmallIntegerField()
	Pblm 		= models.TextField(blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patients"


