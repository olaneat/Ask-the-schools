from django.conf.urls import url
from django.urls import path
from . import views, forms


urlpatterns = [
	path('', views.index, name = 'index'),
	path('schoolprofile/step-two', views.schoolprofile2, name='schoolprofile2'),
	path('schoolprofile/step-one', views.schoolprofile1, name = 'schoolprofile1'),
	path('schoolprofile/add-user', views.add_user, name= 'add_user'),
	#path(r'ProfileYourSchool', add_School.as_view([profileForm, SchoolsForm, schoolDataForm]), name = 'add_Schools'),
	path(r'ContactUs', views.Contact, name = 'Contact'),
]