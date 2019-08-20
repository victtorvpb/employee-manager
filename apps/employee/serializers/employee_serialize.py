from rest_framework import serializers


from apps.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.SerializerMethodField()
    # department = DepartmentSeializer(read_only=True, many=False)

    class Meta:
        model = Employee
        exclude = ('created', 'modified', 'id')

    def get_department(self, obj):
        return obj.department.name
