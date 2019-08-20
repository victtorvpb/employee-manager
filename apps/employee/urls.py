from django.urls import path

from .views.its_alive import its_alive

app_name = 'employee'
urlpatterns = [path('its_alive/', its_alive, name='its_alive')]
