from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *
from main.models import *
from application.models import *
from products.models import *


# Create your views here.

def software(request):
    if not request.user.is_support:
        return redirect('support')
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    category = SoftwareCategory.objects.all()
    var = SoftwareBlock.objects.all()
    pdf = PDF.objects.all()

    return render(request, 'software.html',
                  {'visit': visit, 'cat': cat, 'mcat': mcat, 'category': category, 'pdf': pdf, 'var': var,
                   })


def softwarecategory(request, slug):
    if not request.user.is_support:
        return redirect('support')
    visit = PageVisit.objects.all().count()
    cat = Category.objects.all()
    mcat = MicroCategory.objects.all()
    category = SoftwareCategory.objects.all()
    soft = SoftwareSubCategory.objects.get(slug=slug)
    var = Software.objects.filter(category=soft)
    pdf = PDF.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request, 'software-category.html',
                  {'page_obj': page_obj, 'visit': visit, 'cat': cat, 'mcat': mcat, 'pdf': pdf,
                   'category': category, 'var': var})
