from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'instrument', 'schedule')
    search_fields = ('full_name', 'email', 'instrument')
    list_filter = ('mode', 'instrument', 'schedule')
