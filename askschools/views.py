from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views import View
from . forms import SchoolsForm, schoolDataForm
from django.http import HttpResponse
from django.utils.decorators import classonlymethod
from django.shortcuts import render
import re
from django.utils import timezone
from . forms import ContactUsForm
from collections import OrderedDict
from django import forms
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView, WizardView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Schools, school_data, parents_remark
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.views import generic




# Create your views here.
def index(request):
	return render (request, 'index.html')



class add_School(SessionWizardView):
	template_name =  'schoolprofile.html'
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,\
	 'images', 'videos'))

	def done(self, form_list, form_dict, **kwargs):
		form_data = process_form_data(form_list)
		return render('index.html',  { 'form_data':form_data})
	


def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	form = form_data
	data = [' User', 'Schools', 'school_data']
	#send_mail(
		#form_data[0]['Schools'],
		#form_data[1]['school_data']
		#['tosinayoola0@gmail.com', ], fail_silently = False)
	#	)

def Contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form} 
           
            return redirect('contactus.html')
    else:
        form = ContactUsForm()

    return render(request,  'contactus.html', {'form': form})

def send_mail():
	send_mail(
		'Subject here',
	'Here is the message',
		'tosinayoola0@gmail.com',
		['tosinayoola0@gmail.com', '']
		)


def add_school(request):
	user_form  = UserCreationForm(request.POST or None)
	school_form1 = Schools(request.POST or None)
	school_form2 = school_data(request.POST or None)
	if request.method == 'POST' and \
			all([user_form.is_valid(), \
				school_form1.is_valid(), school_form2.is_valid()]):
		user_form.save()
		schoolprofile1.save()
		schoolprofile2.save()
		return redirect(reverse('index')) 


def add_user(request):
	create_user = UserCreationForm(request.POST or None)
	if request.method == 'POST' and create_user.is_valid():
		create_user.save()
		return redirect('add_school_step_one')

def schoolprofile1(request):
	school_info = SchoolsForm(request.POST )
	if request.method == 'POST' and school_info.is_valid():
		request.session['SchoolsForm'] = school_info.cleaned_data
		return redirect('add_school_step_two')

	return render(request, 'schoolprofile1.html',
		{'school_info': school_info,})

def schoolprofile2(request):
	school_data = school_dataForm(request.POST)
	if request.method == 'POST' and school_data.is_valid():
		complete_school_data = {
		**request.session['school_data'],
		**schoolprofile2.cleaned_data
		} 
		request.session['schoolDataForm'] = school_data.cleaned_data
		return redirect()

