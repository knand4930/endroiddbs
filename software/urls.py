from django.urls import path
from .views import *

urlpatterns = [
    path('software', software, name='software'),
    path('software/category/<slug>', softwarecategory, name='softwarecategory')

]
