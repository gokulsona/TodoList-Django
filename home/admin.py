from django.contrib import admin
from home.models import Task, Completed
# Register your models here.
admin.site.register(Task)
admin.site.register(Completed)