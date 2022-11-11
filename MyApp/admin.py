from django.contrib import admin
from .models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['id', 'name', 'age', 'contact']


admin.site.register(student, studentadmin)
