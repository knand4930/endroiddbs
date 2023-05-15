from random import random

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from application.models import *
from software.models import *
from products.models import *

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(request):
    cat = Category.objects.all()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        visit = x_forwarded_for.split(',')[0]
    else:
        visit = request.META.get('REMOTE_ADDR')
    var = PageVisit.objects.create(visit=visit)
    var.save()
    visit = PageVisit.objects.all().count()
    video = EmbadedVideo.objects.all()
    products = Products.objects.all().order_by('-id')
    slider = Slider.objects.all().order_by('-id')
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()
    # trending = Products.objects.filter('trending').order_by('-id')[:5]
    return render(request, 'home.html', {'cat': cat, 'visit': visit, 'video': video, 'products': products,
                                         'slider': slider, 'mcat': mcat, 'pdf': pdf})


def about(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'about.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def career(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        experience = request.POST.get('experience')
        address = request.POST.get('address')
        city = request.POST.get('city')
        field = request.POST.get('field')
        cv = request.FILES.get('cv')
        remark = request.POST.get('remark')

        data = Career.objects.create(name=name, surname=surname, experience=experience, address=address, city=city,
                                     field=field, cv=cv, remark=remark)
        data.save()
        msg = "Your Career Details Has Been Submitted!"
        subject = f"Career Details Person Name: {name} {surname} and Experience: {experience}"
        message = f"Person Name : {name}  {surname}\n Person Experience : {experience} \n Address : {address}" \
                  f" \n City Name : {city} \n Fields Name : {field}, \n Resume/CV: {settings.SITES_URL}{data.cv.url} \n Remarks {remark}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.SENDING_EMAIL
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'success.html', {'msg': msg})
    return render(request, 'career.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def contact(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        msg = request.POST.get('msg')
        data = ContactUs.objects.create(name=name, email=email, sub=sub, msg=msg)
        data.save()
        msg = "Your contact details has been sent !"
        subject = f"Contact Details Person Name: {name} and Email: {email}"
        message = f"Person Name : {name} \n Person Email : {email} \n Subject : {sub}" \
                  f" \n Messages Details : {msg} \n "
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.SENDING_EMAIL
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'success.html', {'msg': msg})
    return render(request, 'contact.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def dealership(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'dealership.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def dvr(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'dvr.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def hdcctv(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'hd-cctv.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def hiring(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'hiring.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def marketing(request):
    visit = PageVisit.objects.all().count()
    # cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    market = Marketing.objects.all()
    pdf = PDF.objects.all()

    p = Paginator(market, 12)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    cat = Category.objects.all()
    return render(request, 'marketing.html',
                  {'visit': visit, 'cat': cat, 'mcat': mcat, 'page_obj': page_obj, 'pdf': pdf, 'cat': cat})


def myaccount(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'my-account.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def partner(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    if request.method == 'POST':
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        gst = request.POST.get('gst')
        year_business = request.POST.get('year_business')
        type_business = request.POST.get('type_business')
        revenue = request.POST.get('revenue')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zipcode = request.POST.get('zipcode')
        sales_employee = request.POST.get('sales_employee')
        technical_employee = request.POST.get('technical_employee')
        major_brand = request.POST.get('major_brand')

        user_obj = User.objects.create_user(username=email, email=email, first_name=name, last_name=phone)
        user_obj.set_password(password)
        user_obj.save()

        data = Partner.objects.create(user=user_obj, company=company, name=name, email=email, phone=phone,
                                      website=website, year_business=year_business
                                      , type_business=type_business, revenue=revenue, address=address, city=city,
                                      state=state,
                                      country=country, zipcode=zipcode, sales_employee=sales_employee,
                                      technical_employee=technical_employee,
                                      major_brand=major_brand, gst=gst, password=password)
        data.save()
        msg = "Your Registrations Successfully Completed!"
        subject = f"Partnership Details Company Name: {company} and User Name: {name}"
        message = f"Person Name : {name} \n Person Email : {email} \n Person Contact Number:{phone} \n" \
                  f" Person Company Name : {company} \n Person Website Name: {website} \n Gst Details: {gst} \n" \
                  f"Business Year: {year_business} \n Types of Business: {type_business} \n Revenue: {revenue}" \
                  f" \n Person Country Name : {country} \n Person State Name: {state} \n Person City Name : {city} \n" \
                  f"Address : {revenue} \n Zip Code : {zipcode}, \n Sales Employee : {sales_employee}, \n" \
                  f"Technical Employee : {technical_employee} \n Major Brand Name : {major_brand}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.SENDING_EMAIL
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'success.html', {'msg': msg})
    return render(request, 'partner.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def photogallery(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    gallery = GalleryCat.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'photogallery.html',
                  {'visit': visit, 'cat': cat, 'mcat': mcat, 'gallery': gallery, 'pdf': pdf})


def proswitches(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'poe-switches.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def privacy(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'privacy.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def ssl(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'ssl.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def userlogin(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            msg = "User Not Found !"
            return render(request, 'userlogin.html', {'msg': msg})
        user = authenticate(username=username, password=password)
        if user is None:
            msg = "Wrong Password !"
            return render(request, 'userlogin.html', {'msg': msg})
        if user is not None:
            if user.is_status:
                login(request, user)
                return redirect('home')
            else:
                msg = "User Not Verified, Please Contact Adminstrator !"
                return render(request, 'userlogin.html', {'msg': msg})
    return render(request, 'userlogin.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def videogallery(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()
    video = VideoGallery.objects.all()
    return render(request, 'videogallery.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf, 'video': video})


def support(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            msg = "User Not Found !"
            return render(request, 'login.html', {'msg': msg})
        user = authenticate(username=username, password=password)
        if user is None:
            msg = "Wrong Password !"
            return render(request, 'login.html', {'msg': msg})
        if user is not None:
            if user.is_support:
                login(request, user)
                return redirect('software')
            else:
                msg = "Invalid Credential, Please Contact With Administrator!"
                return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def logout_attempt(request):
    logout(request)
    return redirect('userlogin')


def waste_management(request):
    cat = Category.objects.all()
    pdf = PDF.objects.all()
    return render(request, 'e-waste-management.html', {'cat': cat, 'pdf': pdf})


def send_email(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = settings.SENDING_EMAIL

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully')
