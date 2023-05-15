from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from application.models import *
from main.models import *
from products.models import *


# Create your views here.


def application(request):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    app = Application.objects.all()
    pdf = PDF.objects.all()

    category = ApplicationCategory.objects.all()
    p = Paginator(app, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return render(request, 'application.html',
                  {'visit': visit, 'cat': cat, 'mcat': mcat, 'page_obj': page_obj, 'category': category, 'pdf': pdf})


def catapplication(request, slug):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    category = ApplicationCategory.objects.all()
    subcat = ApplicationSubCategory.objects.get(slug=slug)
    app = Application.objects.filter(category=subcat)
    p = Paginator(app, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return render(request, 'application.html',
                  {'visit': visit, 'cat': cat, 'mcat': mcat, 'page_obj': page_obj, 'category': category, 'pdf': pdf})


def singlepageapplication(request, slug):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()
    apps = get_object_or_404(Application, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        msg = request.POST.get('msg')
        product_name = apps.name
        product_cat = apps.category.name
        data = ApplicationRequest.objects.create(name=name, email=email, company=company, country=country,
                                                 state=state, city=city, msg=msg,
                                                 application_name=product_name, application_category=product_cat)
        data.save()
        msg = "Your Contact Data Has Been Successfully Sent!"
        return render(request, 'success.html', {'msg': msg})

    return render(request, 'single-page-application.html', {'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf, 'apps':apps})
