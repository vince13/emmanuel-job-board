from django.contrib import admin

from .models import CustomUser, Job, Application

admin.site.register(CustomUser)
admin.site.register(Job)
admin.site.register(Application)




