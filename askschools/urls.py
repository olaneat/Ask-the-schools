from django.conf.urls import url
from django.urls import path
from . import views
from . forms import profileForm, SchoolsForm, schoolDataForm
from . views import add_School, Contact 

urlpatterns = [
	path('', views.index, name = 'index'),
	path(r'ProfileYourSchool', add_School.as_view([profileForm, SchoolsForm, schoolDataForm]), name = 'add_Schools'),
	path(r'ContactUs', views.Contact, name = 'Contact'),
]