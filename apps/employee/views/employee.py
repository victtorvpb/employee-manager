from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.employee.models import Employee, Department
from apps.employee.serializers import EmployeeSerializer


class EmployeeView(APIView):
    def get(self, request, uuid=None):
 
        if uuid:
            employee = get_object_or_404(Employee, uuid=uuid)
            serializer = EmployeeSerializer(employee)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data, 200)

    def post(self, request, uuid=None):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            department = get_object_or_404(
                Department, name=request.data.get('department')
            )

            serializer.save(department=department)

            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)

    @classmethod
    def get_department(cls, department_name):
        return

    def delete(self, request, uuid):
        employee = get_object_or_404(Employee, uuid=uuid)
        employee.delete()
        return Response(status=204)
