from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class ApplicationCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicationSubCategory(models.Model):
    category = models.ForeignKey(ApplicationCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    category = models.ForeignKey(ApplicationSubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    model_details = models.CharField(max_length=200, blank=True, null=True)
#    reference = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#    short = RichTextField(default=None, blank=True, null=True)
#    description = RichTextField(default=None, blank=True, null=True)
#    details = RichTextField(default=None, blank=True, null=True)
#    img = models.ImageField(upload_to="application/", blank=True, null=True)
#    img1 = models.ImageField(upload_to="application/", blank=True, null=True)
#    img2 = models.ImageField(upload_to="application/", blank=True, null=True)
#    img3 = models.ImageField(upload_to="application/", blank=True, null=True)
#    img4 = models.ImageField(upload_to="application/", blank=True, null=True)
#    download = models.FileField(upload_to="application/pdf/", blank=True,null=True)
    google = models.URLField(blank=True, null=True)
    ios = models.URLField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicationRequest(models.Model):
    application_name = models.CharField(max_length=500, blank=True, null=True)
    application_category = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    company = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    msg = models.CharField(max_length=500, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
