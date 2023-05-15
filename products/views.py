from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404
from application.models import *
from main.models import *
from software.models import *

from products.models import *


# Create your views here.

def category(request, slug):
    visit = PageVisit.objects.all().count()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    cat = Category.objects.get(slug=slug)
    product = Products.objects.filter(category=cat)
    p = Paginator(product, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    cat = Category.objects.all()
    return render(request, 'category.html',
                  {'product': product, 'page_obj': page_obj, 'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def sub_category(request, slug):
    visit = PageVisit.objects.all().count()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    cat = SubCategory.objects.get(slug=slug)
    product = Products.objects.filter(sub_category=cat)
    p = Paginator(product, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    cat = Category.objects.all()
    return render(request, 'category.html',
                  {'product': product, 'page_obj': page_obj, 'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def micro_category(request, slug):
    visit = PageVisit.objects.all().count()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    cat = MicroCategory.objects.get(slug=slug)
    product = Products.objects.filter(micro_category=cat)
    p = Paginator(product, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    cat = Category.objects.all()
    return render(request, 'category.html',
                  {'product': product, 'page_obj': page_obj, 'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})


def singleproduct(request, slug):
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    pdf = PDF.objects.all()

    prod = get_object_or_404(Products, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        msg = request.POST.get('msg')
        product_name = prod.title
        if prod.category is not None:
            product_cat = prod.category.name
        if prod.sub_category is not None:
            product_cat = prod.sub_category.name
        if prod.micro_category is not None:
            product_cat = prod.micro_category.name

        data = ProductRequest.objects.create(name=name, email=email, company=company, country=country,
                                             state=state, city=city, msg=msg,
                                             product_name=product_name, product_cat=product_cat)
        data.save()
        msg = "Your Contact Data Has Been Successfully Sent!"
        return render(request, 'success.html', {'msg': msg})

    return render(request, 'single-product.html', {'prod': prod, 'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf})
