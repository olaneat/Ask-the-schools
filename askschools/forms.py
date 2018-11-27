from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Schools, ContactUs, Sports
from . constant import sex, clubs, sport


class profileForm(UserCreationForm):
  class Meta:
  	model = User
  	fields = ['email', 	'first_name', 'last_name', 'username','password1', 'password2']


#	def save(self, commit = True):
#		user  = super(profileForm, self).save (commit =  False)
#		user.first_name =  self.cleaned_data['first_name']
#		user.last_name =  self.cleaned_data['last_name']
#		user.email =  self.cleaned_data['email']
#
#		if commit:
#			user.save()
#
#		return user

		



class SchoolsForm(ModelForm):
  SCHOOL_NAME = forms.CharField(
    widget = forms.TextInput(
	  attrs ={
	  	'title': 'School Name',
		'class': 'special',
		   }
	 )
		)

  MOTTO = forms.CharField(
	widget = forms.TextInput(
	  attrs ={
	    'placeholder': "School motto...."
		  }
	 	 )
		)

  EMAIL = forms.CharField(
    widget = forms.TextInput(
	  attrs ={
	    'placeholder': "Offical School email  ...."
		  }
	    )
	  )

  PHONE = forms.CharField(
	widget = forms.TextInput(
      attrs ={
	    'placeholder': "Offical School Phone Number  ...."
			}
	      )
		)

  GENDER = forms.ChoiceField(label =" SCHOOL GENDER",
    choices = sex, 
	widget = forms.RadioSelect(),
	  )


  class Meta:
    model = Schools
    fields = ['SCHOOL_NAME', 'MOTTO', 'BADGE', 'SCHOOL_TYPE', \
     	'LEVEL', 'ADVANTAGE', 'EMAIL', 'PHONE', 'ADDRESS',\
     	 'TOWN', 'STATE', ]

	
class SchoolDataForm(ModelForm):
  EXTRA_CURRICULUM = forms.MultipleChoiceField(
	label = 'CLUB ACTIVITIES',
	required = False,
	widget = forms.CheckboxSelectMultiple,
	choices = clubs )

  SPORT = forms.MultipleChoiceField(
	widget=forms.CheckboxSelectMultiple,
	queryset=Sports.objects.all(),)


  class Meta:
  	model = Schools
  	fields = ['CURRICULUM', 'AWARDS', 'SPORTS', 'WEBSITE',\
  	 'FEES_RANGE', 'VIDEO', 'DIRECTION', ]


class ContactUsForm(ModelForm):
  class Meta:
    model = ContactUs
    fields = ['full_name', 'email',  'message']



		