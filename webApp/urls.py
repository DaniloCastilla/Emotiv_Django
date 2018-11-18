from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^terapeuta/$', views.homeTherapist, name='home_therapist'),
	url(r'^registro_t/$', views.registerTherapist, name='register_therapist'),
	url(r'^paciente/$', views.searchPatient, name='search_patient'),
	url(r'^registro_p/$', views.registerPatient, name='register_patient'),
	url(r'^registro_tp/$', views.registerPatientMedInfo, name='register_patient_medInfo'),
	url(r'^terapias/$', views.searchTherapy, name='search_therapy'),
	url(r'^terapia_s/$', views.registerTherapy, name='register_therapy'),
]
