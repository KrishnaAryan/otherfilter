from django.contrib import admin
from webapp.models import filtermodel
# Register your models here.
class filteradmin(admin.ModelAdmin):
	list_display=['Name','Add','Dept','Sub','Date']
admin.site.register(filtermodel,filteradmin)