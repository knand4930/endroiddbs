from django.urls import path
from .views import *

urlpatterns = [
    path('adminpanel', adminpanel, name='adminpanel'),

    path('total/user', total_user, name='total_user'),
    path('create/support/user', create_support_user, name='create_support_user'),
    path('support/user/list', support_user_list, name='support_user_list'),

    path('login/verification', login_verification, name='login_verification'),
    path('login/pending', login_pending, name='login_pending'),

    path('change/password', change_password, name='change_password'),
    path('edit/user/<id>', edit_user, name='edit_user'),

    path('loginadmin', loginadmin, name='loginadmin'),
    path('logout_admin', logout_admin, name='logout_admin'),
]