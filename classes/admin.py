from django.contrib import admin
from .models import FitnessClass, UserClass
# Register your models here.
admin.site.register(FitnessClass)
admin.site.register(UserClass)