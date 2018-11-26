from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.views import View, generic
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.utils import timezone
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from . import models
from . forms import ContactUsForm, SchoolsForm, SchoolDataForm
from django.core.mail import send_mail


# Create your views here.

def index(request):
  return render (request, 'index.html')



#class add_School(SessionWizardView):
 # template_name =  'schoolprofile.html'
  #file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,\
	# 'images', 'videos'))
#
 # def done(self, form_list, form_dict, **kwargs):
  #  form_data = process_form_data(form_list)
   # return render('index.html',  { 'form_data':form_data})
	
#def process_form_data(form_list):
 # form_data = [form.cleaned_data for form in form_list]
  #form = form_data
  #data = [' User', 'Schools', 'school_data']
 #send_mail(
 	#form_data[0]['Schools'],
	#form_data[1]['school_data']
	#['tosinayoola0@gmail.com', ], fail_silently = False)
	#)

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
  	['tosinayoola0@gmail.com', ''])


def add_school(request):
  create_user  = UserCreationForm(request.POST or None)
  school_info = SchoolsForm(request.POST or None)
	
  if request.method == 'POST' and \
    all([create_user.is_valid(),school_info.is_valid(),]):
        create_user.save()
        school_info.save()

        return redirect(reverse('index'))

  return render(request, 'create_user_form.html',{
    'school_info': school_info,
	'create_user': create_user}) 


def add_user(request):
  create_user = UserCreationForm(request.POST or None)
  if request.method == 'POST' and create_user.is_valid():
    create_user.save()
    return redirect('schoolprofile1')
	
  return render( request, 'create_user_form.html',
    {'create_user': create_user,})


def schoolprofile1(request):
  school_info = SchoolsForm(request.POST or None)
  if request.method == 'POST' and school_info.is_valid():
    request.session['school_data'] = school_info.cleaned_data
    return redirect('schoolprofile2')

  return render(request, 'schoolprofile1.html', {
    'school_info': school_info,
  })



def schoolprofile2(request):
  school_info_two = SchoolDataForm(request.POST or None)
  if request.method == 'POST' and school_data.is_valid():
    complete_school_data_ = {
	  **request.session['school_data'],
	  **school_info_two.cleaned_data} 
    Schools.object.create(**complete_school_data)	

    return redirect('index')

  return render(request, 'schoolprofile2.html',{
	'school_data':school_info_two,})
