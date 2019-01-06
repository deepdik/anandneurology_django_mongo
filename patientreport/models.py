from djongo import models
from datetime import datetime as dt
import datetime


from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

GENDER = (('male','Male'),('female','Female'),('unknown','Unknown'))
BLOODGROUP = (('a','A'),('b','B'),('ab','AB'))

class Disease(models.Model):
	name 		= models.CharField(max_length=120)
	des 		= models.TextField('About Disease' ,blank=True)

	def __str__(self):
		return self.name

class PatientDetails(models.Model):
	patientid   =   models.CharField(max_length=120,blank=True, unique=True)
	name 		= 	models.CharField('Patient Name',max_length=120)
	age 		= 	models.PositiveIntegerField()	
	gender 		= 	models.CharField(max_length=12, choices=GENDER)
	mobileNo    =   models.CharField('Mobile Number',max_length=10)
	address		= 	models.TextField(blank=True)
	timestamp 	= 	models.DateTimeField(db_index=True,auto_now_add=True)
	patientimg	=	models.ImageField('Patient photo',blank=True,null=True,upload_to='patientimg')
	bloodgroup	=   models.CharField('Blood Group',max_length=12, choices=BLOODGROUP, blank=True)
	diseases	=	models.ManyToManyField(Disease,blank=True)
	other       =   models.TextField('Other Problems' ,blank=True)


	def __str__(self):
		return self.name		
	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patient Details"
		

class PatientTestReport(models.Model):
	patient    	= 	models.ForeignKey(PatientDetails, on_delete=models.CASCADE, related_name = 'TestReport')
	reportimg	=	models.ImageField('Report Image',upload_to='patientreports/',blank=True,null=True,)
	notes 		=	models.TextField(blank=True)
	timestamp	= 	models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.patient.name
	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patient Test Reports"


class PatientMeetingRecords(models.Model):
	patient    	= models.ForeignKey(PatientDetails, on_delete=models.CASCADE,related_name = 'meetingrecord')
	Date 		= models.DateField(default = datetime.date.today)
	notes 		= models.TextField(blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.patient.name
	class Meta:
		ordering = ('timestamp',)
		verbose_name_plural = "Patient Meeting Records"


@receiver(post_save, sender=PatientDetails)
def create_patientid(sender, instance, created, **kwargs):
	if not instance.patientid:				
		instance.patientid = str(instance.timestamp.year) + '-' + str(instance.id)
		instance.save()