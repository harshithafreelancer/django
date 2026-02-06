from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')
    search_fields = ('name', 'email')  # adding search bar
    list_filter = ('age',)  # adding filters

admin.site.register(Employee,EmployeeAdmin)
