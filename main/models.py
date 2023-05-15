from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_status = models.BooleanField('Is Status', default=False)
    is_support = models.BooleanField("Is Support", default=False)
    cats = models.IntegerField(default=0, blank=True, null=True)


class PageVisit(models.Model):
    visit = models.CharField(max_length=200, blank=True, null=True, default=0)
    create_at = models.DateTimeField(auto_now_add=True)


class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    short = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='slider/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EmbadedVideo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    sub = models.CharField(max_length=500, blank=True, null=True)
    msg = models.TextField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    surname = models.CharField(max_length=300, blank=True, null=True)
    field = models.CharField(max_length=300, blank=True, null=True)
    experience = models.IntegerField()
    address = models.TextField(default=None, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    cv = models.FileField(upload_to="career/", blank=True, null=True)
    remark = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class PDF(models.Model):
    objects = None
    name = models.CharField(max_length=200, blank=True, null=True)
    pdf = models.FileField(upload_to="pdf/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    # slug= AutoSlugField(populate_from='title',unique=True,null=True,default=None)


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    gst = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    company = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=300, blank=True, null=True)
    website = models.CharField(max_length=300, blank=True, null=True)
    year_business = models.CharField(max_length=300, blank=True, null=True)
    type_business = models.CharField(max_length=300, blank=True, null=True)
    revenue = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=300, blank=True, null=True)
    zipcode = models.CharField(max_length=300, blank=True, null=True)
    sales_employee = models.CharField(max_length=300, blank=True, null=True)
    technical_employee = models.CharField(max_length=300, blank=True, null=True)
    major_brand = models.CharField(max_length=300, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Marketing(models.Model):
    name = models.TextField(default=None, blank=True, null=True)
    img = models.ImageField(upload_to="marketing/")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GalleryCat(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(GalleryCat, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='gallery/')
    name = models.TextField(default=None, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




class VideoGallery(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.title
