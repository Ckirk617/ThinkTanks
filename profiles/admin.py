from django.contrib import admin

# Register your models here.
from .models import Organization, City, PolicyArea, Staff

admin.site.register(Organization)
admin.site.register(PolicyArea)
admin.site.register(Staff)
admin.site.register(City)