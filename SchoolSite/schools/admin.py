from django.contrib import admin
from .models import Member, School

# Registers the Member and School models so that they can be manipulated by admin users
admin.site.register(Member)
admin.site.register(School)