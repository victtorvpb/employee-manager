from django.contrib import admin

from apps.employee.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'department')
    list_display = ('name', 'email', 'get_department_name')
    search_fields = ['name', 'email', 'department__name']

    def get_department_name(self, obj):
        return obj.department.name
