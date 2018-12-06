from django.conf.urls import url
from django.urls import path
from . import views, forms


urlpatterns = [
	path('schoolprofile/step-two', views.schoolprofile2, name='schoolprofile2'),
	path('schoolprofile/step-one', views.schoolprofile1, name = 'schoolprofile1'),
	path('schoolprofile/add-user', views.add_user, name= 'add_user'),
	#path('schoolprofile', views.add_school, name='add_school'),
	path('', views.index, name = 'index'),
	path(r'ContactUs', views.Contact, name = 'Contact'),
]
