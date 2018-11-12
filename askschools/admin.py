from django.contrib import admin
from .models import Schools, parents_remark, school_data
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('SCHOOL_NAME','MOTTO', 'BADGE', 'LEVEL' ,  'ADVANTAGE', 'ADDRESS', 'SCHOOL_TYPE', 'FEES_RANGE', 'EMAIL', 'PHONE', 'VIDEO', 'TOWN', 'STATE')


@admin.register(school_data)
class school_data(admin.ModelAdmin):
	list_display = ( 'CURRICULUM', 'EXTRA_CURRICULUM',  'AWARDS', 'DIRECTION', 'WEBSITE')

@admin.register(parents_remark)
class parents_remark(admin.ModelAdmin):
	list_display =('full_name', 'school_name', 'comment')