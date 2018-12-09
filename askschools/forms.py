from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Schools, ContactUs, Sports, Club
from . constant import sex

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
  School_name = forms.CharField(
    widget = forms.TextInput(
	  attrs ={
	  	'title': 'School Name',
		'class': 'special',
		   }
	 )
		)

  Motto = forms.CharField(
	widget = forms.TextInput(
	  attrs ={
	    'placeholder': "School motto...."
		  }
	 	 )
		)

  Email = forms.CharField(
    widget = forms.TextInput(
	  attrs ={
	    'placeholder': "Offical School email  ...."
		  }
	    )
	  )

  Phone = forms.CharField(
	widget = forms.TextInput(
      attrs ={
	    'placeholder': "Offical School Phone Number  ...."
			}
	      )
		)

  Gender = forms.ChoiceField(label =" SCHOOL GENDER",
    choices = sex,
	widget = forms.RadioSelect())



  class Meta:
    model = Schools
    fields = ['School_name', 'Motto', 'Badge', 'School_type', \
     	'Level', 'Advantage', 'Email', 'Phone', 'Fees_range',\
        'Address', 'Town', 'State', ]


class SchoolDataForm(ModelForm):
  Extra_curriculum_activities  = forms.ModelMultipleChoiceField(
  	queryset = Club.objects.all(),
	required = False,
	widget = forms.CheckboxSelectMultiple,)

  Sport_activities = forms.ModelMultipleChoiceField(
	queryset=Sports.objects.all(),
	widget=forms.CheckboxSelectMultiple)



  class Meta:
  	model = Schools
  	fields = ['Curriculum', 'Awards', 'Sport_activities','Extra_curriculum_activities',\
     'Website', 'Video', 'Direction',  ]


class ContactUsForm(ModelForm):
  class Meta:
    model = ContactUs
    fields = ['full_name', 'email',  'message']
