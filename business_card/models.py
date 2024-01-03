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
        return self.title + ' ' + self.subtitle

class Brands(models.Model):

    class Meta:
        verbose_name = 'Бренды'
        verbose_name_plural = 'Бренды'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    image = models.FileField(upload_to="images/%Y/%m/%d/",
                              default='default/no-image.svg',
                              null=True,
                              blank=True,
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])

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
    link = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class Delivery(models.Model):

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    name = models.CharField(max_length=64, blank=True)
    image = models.FileField(upload_to="images/%Y/%m/%d/",
                              default='default/no-image.svg',
                              null=True,
                              blank=True,
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    path = models.CharField(max_length=64, blank=True)
    link = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class Request(models.Model):

    class Meta:
        verbose_name = 'Запросы'
        verbose_name_plural = 'Запросы'

    # def files_upload_to(self, instance=None):
    #     if instance:
    #         return os.path.join('files', slugify(self.series.slug), slugify(self.article_slug), instance)
    #     return None

    name = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=148, blank=True)
    inn = models.CharField(max_length=148)
    email = models.CharField(max_length=148, blank=True)
    # files = models.FileField(upload_to="files/%Y/%m/%d/",
    #                           null=True,
    #                           blank=False,
    #                           validators=[FileExtensionValidator(['xls', 'xlsx', 'ods', 'doc', 'docx'])])
    message = models.TextField(max_length=512)

    def __str__(self):
        return self.name

class Requisites(models.Model):

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    name = models.CharField(max_length=128, verbose_name="Наименование реквизита", blank=True)
    value = models.CharField(max_length=128, verbose_name="Содержание реквизита", blank=True)

    def __str__(self):
            return self.name

class CatalogGroups(models.Model):
    class Meta:
        verbose_name = 'Группы каталогов'
        verbose_name_plural = 'Группы каталогов'

    name = models.CharField(max_length=128, verbose_name="Наименование группы каталога", blank=True)
    caption = models.CharField(max_length=128, verbose_name="Загаловок группы каталога", blank=True)
    items = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=False)
    
    def __str__(self):
            return self.name
    
class Catalog(models.Model):
    class Meta:
        verbose_name = 'Каталоги'
        verbose_name_plural = 'Каталоги'

    name = models.CharField(max_length=128, verbose_name="Наименование каталога", blank=True)
    image = models.FileField(verbose_name="Картинка каталога",
                                upload_to="images/%Y/%m/%d/",
                                default='default/no-image.svg',
                                null=True,
                                blank=True,
                                validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    link = models.CharField(max_length=128, verbose_name="Ссылка каталога", blank=True)
    
    def __str__(self):
            return self.name