from django.urls import path

from .views import its_alive, EmployeeView

app_name = 'employee'
urlpatterns = [
    path('its_alive/', its_alive, name='its_alive'),
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>/', EmployeeView.as_view()),
]
