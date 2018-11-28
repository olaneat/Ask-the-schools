from django.db import models
from django.contrib.auth.models import User
from . constant import level, sex, clubs, sport, school_fees, state, school_type, curriculum
# Create your models here.


class Sports(models.Model):
  sport = models.CharField(max_length = 150)

class gender(models.Model):
  sex = models.CharField(max_length = 15)

class Club(models.Model):
  club = models.CharField(max_length = 300)

class Schools(models.Model):
  SCHOOL_NAME = models.CharField(max_length = 300,  )
  MOTTO = models.CharField( max_length = 200,  )
  BADGE = models.ImageField(upload_to = "media/images", blank= True,\
   help_text = "upload a jpg file ")
  LEVEL = models.CharField( blank=True, max_length = 20, choices =level )
  ADVANTAGE = models.TextField(blank = True, max_length = 1000,\
   help_text = '''what do parents tend to benefit  by entrusting their children
	in your school not more than 1000 characters'''  )
  GENDER = models.BooleanField('complete', default ='True')
  ADDRESS = models.CharField( max_length  = 250 )
  TOWN = models.CharField( max_length = 100,\
   help_text = 'enter the Local Government Area')
  STATE = models.CharField( max_length = 4, choices = state)	
  CURRICULUM = models.CharField(max_length =20, null = True, choices = curriculum )
  WEBSITE = models.URLField(max_length = 100, blank = True )
  EXTRA_CURRICULUM = models.CharField(max_length = 20, null = True )
  AWARDS = models.CharField( max_length = 150, blank = True,\
    help_text ='kindly list the schools Awards')
  SPORTS = models.ManyToManyField(Sports)
  DIRECTION = models.CharField(max_length = 100, null = True,\
   help_text ='give a brief description to your school ' )
  VIDEO = models.FileField(upload_to = 'media/video', blank= True,\
   help_text = "upload a video file, mp4, " )	
  SCHOOL_TYPE = models.CharField( max_length = 20, choices = school_type)
  FEES_RANGE = models.CharField(max_length = 70,  choices = school_fees  )
  EMAIL = models.EmailField(blank = True, max_length = 50, )
  PHONE = models.CharField(blank = True, max_length = 15)
  extra_activities = models.ManyToManyField(Club)
  
  def get_absolute_url(self):
    return reverse('schools:detail', kwargs={'pk': self.pk})



class ParentsRemark(models.Model):
  full_name = models.CharField(max_length = 300,\
    help_text = "fill in your full name" )
  school_name= models.CharField(max_length =100 , null = False  )
  comment = models.TextField(max_length =1000 )
	

class ContactUs(models.Model):
  full_name = models.CharField(max_length = 300 )
  title = models.CharField(max_length = 100, blank = True)
  email= models.EmailField(max_length =100 , null = False )
  message = models.TextField(max_length =1000 )

  def __str__(self):
    return self.comment