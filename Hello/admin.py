from django.contrib import admin

# Register your models here.
from .models  import students  #. is important
admin.site.register(students)
