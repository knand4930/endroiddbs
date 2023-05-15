from django.db import models


# Create your models here.


class SoftwareCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SoftwareSubCategory(models.Model):
    category = models.ForeignKey(SoftwareCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SoftwareBlock(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Software(models.Model):
    category = models.ForeignKey(SoftwareSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    block = models.ForeignKey(SoftwareBlock, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    model_details = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, null=True, unique=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    release_note = models.FileField(upload_to="software/release_note/")
    download = models.FileField(upload_to='software/download/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
