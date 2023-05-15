from django.urls import path
from .views import *

urlpatterns = [
    path('single/product/<slug>', singleproduct, name='singleproduct'),
    path('category/<slug>', category, name='category'),
    path('sub/category/<slug>', sub_category, name='sub_category'),
    path('micro/category/<slug>', micro_category, name='micro_category'),
]