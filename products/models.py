#from ckeditor.fields import RichTextField
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " -- " + self.category.name


class MicroCategory(models.Model):
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " -- " + self.subcat.name

    # def save(self, *args, **kwargs):
    #     if MicroCategory.objects.filter(name=self.name).exists():
    #         extra = str(randint(1, 10000))
    #         self.slug = slugify(self.name) + "-" + extra
    #     else:
    #         self.slug = slugify(self.name)
    #     super(MicroCategory, self).save(*args, **kwargs)


class Products(models.Model):
    TYPES = (
        ('trending', 'trending'),
        ('latest', 'latest'),
        ('hide', 'hide'),
        ('trending_latest', 'trending_latest')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    micro_category = models.ForeignKey(MicroCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    model_details = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    dealer_price = models.IntegerField(default=0, blank=True, null=True)
    img = models.ImageField(upload_to="product/", blank=True, null=True)
    product_types = models.CharField(max_length=200, blank=True, default='hide', choices=TYPES)
    short_description = RichTextField(config_name='awesome_ckeditor')
    description = RichTextField(config_name='awesome_ckeditor')
    details = RichTextField(config_name='awesome_ckeditor')
    download = models.FileField(upload_to='products', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductRequest(models.Model):
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_cat = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    msg = models.TextField(default=None, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
