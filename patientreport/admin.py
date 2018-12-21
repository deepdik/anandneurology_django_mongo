from django.contrib import admin
from . models import *
from django.utils.safestring import mark_safe


class PatientTestReportInline(admin.TabularInline):
	model = PatientTestReport
	extra = 0
	readonly_fields = ['reports_image',]
	
	def reports_image(self, obj):
		if obj.reportimg :
			return mark_safe('<img src="{url}" width="100px" height=100px />'.format(
				url = obj.reportimg.url

				)
		)

class PatientMeetingRecordsInline(admin.TabularInline):
	model = PatientMeetingRecords
	extra = 0

class PatientDetailsAdmin(admin.ModelAdmin):
	
	search_fields = ('name','patientid', 'mobileNo','diseases')
	list_per_page = 25
	inlines = [  PatientTestReportInline, PatientMeetingRecordsInline, ]
	list_filter = ('diseases','gender')
	readonly_fields = ['patient_image',]




	def patient_image(self, obj):

		if obj.patientimg :
			
			return mark_safe(

				'<img src="{url}" width="100px" height=100px />'.format(
				url = obj.patientimg.url
		
				)
		)


	def get_readonly_fields(self, request, obj=None):
		if obj is None:
			return ['patientid']
		else:
		 	return self.readonly_fields + ['patientid',]
		return []
		  
	list_display = ('name','patientid', 'mobileNo','gender', 'patient_image', )


admin.site.register(PatientDetails, PatientDetailsAdmin)
admin.site.register([Disease])






