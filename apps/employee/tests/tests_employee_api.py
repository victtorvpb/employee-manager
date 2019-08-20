from django.test import TestCase
from django.urls import reverse

from apps.employee.models import Employee


class TestEmployeeApi(TestCase):
    def setUp(self):
        self.default_data = [
            {
                "name": "Arnaldo Pereira",
                "email": "arnaldo@email.com",
                "department": "Architecture",
            },
            {
                "name": "Renato Pedigoni",
                "email": "renato@email.com",
                "department": "E-commerce",
            },
            {
                "name": "Thiago Catoto",
                "email": "catoto@email.com",
                "department": "Mobile",
            },
        ]

    def test_list_employee(self):
        url = reverse('employee:employee_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), list)
        self.assertEqual(len(response.data), 3)

    def test_post_employee(self):
        data_post = {
            "name": "Victor",
            "email": "victor@victor.com",
            "department": "Architecture",
        }
        url = reverse('employee:employee_list')
        response = self.client.post(url, data=data_post)
        employee = Employee.objects.get(
            name=data_post['name'], email=data_post['email']
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(employee)

    def test_delete_employee(self):
        employee = Employee.objects.get(email='renato@email.com')
        url = reverse(
            'employee:delete_employee', kwargs={'uuid': str(employee.uuid)}
        )
        response = self.client.delete(url)
        employee = Employee.objects.filter(email='renato@email.com')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(employee.count(), 0)

    def test_post_employee_invalid_department(self):
        data_post = {
            "name": "Victor",
            "email": "victor@victor.com",
            "department": "teste",
        }
        url = reverse('employee:employee_list')
        response = self.client.post(url, data=data_post)
        employee = Employee.objects.filter(
            name=data_post['name'], email=data_post['email']
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(employee.count(), 0)
