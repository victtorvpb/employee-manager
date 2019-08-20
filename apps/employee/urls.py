from django.urls import path, re_path

from .views import its_alive, EmployeeView, EmployeeViewDelete

app_name = 'employee'
urlpatterns = [
    path('its_alive/', its_alive, name='its_alive'),
    path('employee/', EmployeeView.as_view()),
    re_path(r'employee/(?P<uuid>[-\w\W\d]+)/$', EmployeeViewDelete.as_view()),
]
