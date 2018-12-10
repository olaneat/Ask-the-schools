from django.contrib import admin
from .models import Schools, ParentsRemark
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('School_name','Motto', 'Badge', 'Level' ,  'Advantage', 'Address',\
	 'School_type', 'Fees_range', 'Email', 'Phone', 'Video', 'Town', 'State', \
	 'Curriculum', 'Extra_curriculum',  'Awards', 'Direction', 'Sports', 'Website')


@admin.register(ParentsRemark)
class parents_remark(admin.ModelAdmin):
	list_display =('full_name', 'school_name', 'comment')
