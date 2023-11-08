from django.contrib import admin
from .models import Category , Job ,Company ,jobapply
from django_summernote.admin import SummernoteModelAdmin


class JobAdmin(  SummernoteModelAdmin ):
    search_fields=('title','loction','category','description')
    list_filter=('vecancy','job_nature','job_nature','experience')
    list_display=['title','loction','company','job_nature','vecancy','category']
    summernote_fields = '__all__'






admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(jobapply)

# Register your models here.
