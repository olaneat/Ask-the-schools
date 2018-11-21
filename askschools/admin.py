from django.contrib import admin
from .models import Schools, ParentsRemark
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('SCHOOL_NAME','MOTTO', 'BADGE', 'LEVEL' ,  'ADVANTAGE', 'ADDRESS',\
	 'SCHOOL_TYPE', 'FEES_RANGE', 'EMAIL', 'PHONE', 'VIDEO', 'TOWN', 'STATE', \
	 'CURRICULUM', 'EXTRA_CURRICULUM',  'AWARDS', 'DIRECTION', 'WEBSITE')


@admin.register(ParentsRemark)
class parents_remark(admin.ModelAdmin):
	list_display =('full_name', 'school_name', 'comment')