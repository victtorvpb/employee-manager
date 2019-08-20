from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.employee.models import Employee, Department
from apps.employee.serializers import EmployeeSerializer


class EmployeeView(APIView):
    def get(self, request):

        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            department = get_object_or_404(
                Department, name=request.data.get('department')
            )

            serializer.save(department=department)

            return Response(serializer.data)
        return Response(serializer.errors, 400)

    @classmethod
    def get_department(cls, department_name):
        return
