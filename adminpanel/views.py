from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *


# Create your views here.
def adminpanel(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    ut = User.objects.all().count()
    support = User.objects.filter(is_support=True).count()
    verify = User.objects.filter(is_status=True).count()
    unverify = User.objects.filter(is_status=False).count()
    return render(request, 'adminpanel.html', {'ut': ut, 'support': support, 'verify': verify, 'unverify': unverify})


def total_user(request):
    total = User.objects.all()
    return render(request, 'total_user_list.html', {'total': total})


def create_support_user(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('name')
        if User.objects.filter(username=username).exists():
            msg = "User Name Already Exists !"
            return render(request, 'create_support_user.html', {'msg': msg})
        if User.objects.filter(email=email).exists():
            msg = "Email Already Exists !"
            return render(request, 'create_support_user.html', {'msg': msg})
        data = User.objects.create_user(username=username, email=email, first_name=first_name, is_support=True)
        data.set_password(password)
        data.save()
        msg = "User Create Successfully !"
        return render(request, 'adminsuccess.html', {'msg': msg, 'user': username, 'pass': password})
    return render(request, 'create_support_user.html')


def support_user_list(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    support = User.objects.filter(is_support=True)
    return render(request, 'support_user_list.html', {'support': support})


def change_password(request):
    return render(request, 'change_password.html')


def login_verification(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    value = User.objects.filter(is_status=True)
    return render(request, 'login_verification.html', {'value': value})


def login_pending(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    value = User.objects.filter(is_status=False)
    return render(request, 'login_pending.html', {'value': value})


def loginadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            msg = "User Not Found !"
            return render(request, 'loginadmin.html', {'msg': msg})
        user = authenticate(username=username, password=password)
        if user is None:
            msg = "Wrong Password !"
            return render(request, 'loginadmin.html', {'msg': msg})
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminpanel')
            else:
                msg = "Invalid Credential, Please Contact With Administrator!"
                return render(request, 'loginadmin.html', {'msg': msg})
    return render(request, 'loginadmin.html')


def logout_admin(request):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    logout(request)
    return redirect('loginadmin')


def edit_user(request, id):
    if not request.user.is_superuser:
        return redirect('loginadmin')
    var = get_object_or_404(User, id=id)

    if request.method == 'POST':
        username = request.POST.get('username')
 #       password = request.POST.get('password')
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        is_status = request.POST.get('is_status')
        is_support = request.POST.get('is_support')

        print(username, first_name, email, is_support, is_status)
        data = User.objects.get(id=id)
        data.username = username
        data.first_name = first_name
        data.email = email
        data.is_status = is_status
        data.is_support = is_support
#        data.set_password(password)
        data.save()
        msg = "Customer Has Been Successfully Updated!"
        return render(request, 'adminsuccess.html', {'msg': msg, 'user': username})
    return render(request, 'edit_user.html', {'var': var})
