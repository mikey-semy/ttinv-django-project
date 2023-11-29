from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
import os


class Benefits(models.Model):

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=148)
    image = models.FileField(upload_to="images/%Y/%m/%d/",
                              default='default/no-image.svg',
                              null=True,
                              blank=True,
                              validators=[FileExtensionValidator(['svg'])])

    def __str__(self):
        return self.title


class Products(models.Model):

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=512, blank=True,)
    image = models.FileField(upload_to="images/%Y/%m/%d/",
                              default='default/no-image.svg',
                              null=True,
                              blank=True,
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])

    def __str__(self):
        return self.title