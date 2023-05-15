from django.urls import path
from .views import *

urlpatterns = [
    path('application', application, name='application'),
    path('application/category/<slug>', catapplication, name='catapplication'),
    path('application/details/<slug>', singlepageapplication, name='singlepageapplication'),

]