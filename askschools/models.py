from django.db import models
from . constant import level, sex, clubs, sport, school_fees, state, school_type, curriculum


class Sports(models.Model):
  sport = models.CharField(max_length = 150, choices = sport )

  def __str__(self):
    return self.spot


class Club(models.Model):
  club = models.CharField(max_length = 300, choices = clubs)

  def __str__(self):
    return self.club


class Schools(models.Model):
  School_name = models.CharField(max_length = 300, )
  Motto = models.CharField( max_length = 200, )
  Badge = models.ImageField(upload_to = "media/images", blank= True,\
   help_text = "upload a jpg file ")
  Level = models.CharField( blank=True, max_length = 20, choices =level )
  Advantage = models.TextField(blank = True, max_length = 1000,\
   help_text = '''what do parents tend to benefit  by entrusting their children
	in your school not more than 1000 characters'''  )
  Gender = models.CharField( max_length = 7, choices = sex)
  Address = models.CharField( max_length  = 250 )
  Town = models.CharField( max_length = 100,\
   help_text = 'enter the Local Government Area')
  State = models.CharField( max_length = 4, choices = state)
  Curriculum = models.CharField(max_length =20, null = True, choices = curriculum )
  Website = models.URLField(max_length = 100, blank = True )
  Extra_curriculum = models.CharField(max_length = 20, null = True )
  Awards = models.CharField( max_length = 150, blank = True,\
    help_text ='kindly list the schools Awards')
  Sport_activities = models.ManyToManyField(Sports)
  Direction = models.CharField(max_length = 100, null = True,\
   help_text ='give a brief description to your school ' )
  Video = models.FileField(upload_to = 'media/video', blank= True,\
   help_text = "upload a video file, mp4, " )
  School_type = models.CharField( max_length = 20, choices = school_type)
  Fees_range = models.CharField(max_length = 70,  choices = school_fees  )
  Email = models.EmailField(blank = True, max_length = 50, )
  Phone = models.CharField(blank = True, max_length = 15)
  Extra_curriculum_activities = models.ManyToManyField(Club)

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
