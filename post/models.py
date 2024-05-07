import os

from django.db import models
from colorfield.fields import ColorField
from django.template.defaultfilters import slugify


class CarModel(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "марку"
        verbose_name_plural = "марки"
        db_table = 'car_model'
        ordering = ['title']

class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = 'category'
        ordering = ['title']


class Transmission(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "коробку"
        verbose_name_plural = "коробки"
        db_table = 'transmission'
        ordering = ['title']


class Wheel(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "руль"
        verbose_name_plural = "рули"
        db_table = 'wheel'
        ordering = ['title']


class CarManager(models.Manager):
    def create_post(self, title, description, image):
        post = self.create(title=title.upper(), description=description, image=image)
        return post


class Cars(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cars', null=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    #----------------------------------------------------
    released = models.IntegerField()
    mileage = models.IntegerField()
    color = ColorField(verbose_name="color")
    engine = models.FloatField()
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)
    condition = models.CharField(max_length=15)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    #-----------------------------------------------------------------------------------------
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.released}"

    class Meta:
        verbose_name = 'машину'
        verbose_name_plural = 'машины'
        db_table = 'car dealership'
        ordering = ['released']


def get_image_filename(instance,filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "post/user/"+ str(instance.post.user.id) + "/"+ str(instance.post.id)+ "/"+"IMG_" + str(instance.post.id)+ext


class Images(models.Model):
    post = models.ForeignKey(Cars, on_delete=models.CASCADE, default=None, related_name='images')
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
