from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('career', career, name='career'),
    path('contact', contact, name='contact'),
    path('dealership', dealership, name='dealership'),
    path('dvr', dvr, name='dvr'),
    path('hd/cctv', hdcctv, name='hdcctv'),
    path('hiring', hiring, name='hiring'),
    path('marketing', marketing, name='marketing'),
    path('my/account', myaccount, name='myaccount'),
    path('partner', partner, name='partner'),
    path('photo/gallery', photogallery, name='photogallery'),
    path('pro/switches', proswitches, name='proswitches'),
    path('privacy', privacy, name='privacy'),
    path('ssl', ssl, name='ssl'),
    path('user/login', userlogin, name='userlogin'),
    path('video/gallery', videogallery, name='videogallery'),
    path('support', support, name='support'),
    path('logout', logout_attempt, name='logout_attempt'),
    path('e-waste-management', waste_management, name='waste_management'),
    path('send_email', send_email, name='send_email'),
]
