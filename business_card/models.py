from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage
from django.conf import settings
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
    image = models.FileField(upload_to="media/benefits/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                              validators=[FileExtensionValidator(['svg', 'jpg'])])

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
    image = models.FileField(upload_to="media/brands/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
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
    image = models.FileField(upload_to="media/products/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    link = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class Deliveries(models.Model):

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    name = models.CharField(max_length=64, blank=True)
    image = models.FileField(upload_to="media/deliveries/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    path = models.CharField(max_length=64, blank=True)
    link = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class Requests(models.Model):

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

class Categories(models.Model):
    class Meta:
        verbose_name = 'Категории каталогов'
        verbose_name_plural = 'Категории каталогов'

    name = models.CharField(max_length=128, verbose_name="Наименование категории", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    
    def __str__(self):
        return self.name + '(' + self.slug + ')'
    
class Groups(models.Model):
    class Meta:
        verbose_name = 'Группа каталогов'
        verbose_name_plural = 'Группа каталогов'
    
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория", blank=True)
    name = models.CharField(max_length=128, verbose_name="Группа каталога", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    
    def __str__(self):
        return self.name + '(' + self.slug + ')'
    

class Catalogs(models.Model):
    class Meta:
        verbose_name = 'Каталоги'
        verbose_name_plural = 'Каталоги'
    
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория", blank=True)
    group = models.ForeignKey('Groups', on_delete=models.PROTECT, null=True, verbose_name="Группа", blank=True)
    name = models.CharField(max_length=128, verbose_name="Наименование каталога", blank=True)
    image = models.ImageField(verbose_name="Картинка каталога",
                                upload_to="catalogs/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                                validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    link = models.FileField(upload_to="catalogs/",
                              null=True,
                              blank=False,
                              validators=[FileExtensionValidator(['pdf'])])                            
    # link = models.CharField(max_length=128, verbose_name="Ссылка каталога", blank=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.group) + ')'