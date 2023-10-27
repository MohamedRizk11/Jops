from django.contrib import admin
from .models import Category , Job ,Company


class JobAdmin(admin.ModelAdmin):
    search_fields=('title','loction','category','description')
    list_filter=('vecancy','job_nature','job_nature','experience')
    list_display=['title','loction','company','job_nature','vecancy','category']
admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Company)

# Register your models here.
