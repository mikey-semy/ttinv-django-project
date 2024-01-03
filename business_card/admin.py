from django.contrib import admin
from .models import Benefits, CatalogGroups, Products, Delivery, Brands, Requisites, CatalogGroups, Catalog

# class BenefitsAdmin(admin.ModelAdmin):
#     fields = ['title', 'subtitle', 'image',]
admin.site.site_header = "Панель администрирования"

admin.site.register(Benefits)
admin.site.register(Products)
admin.site.register(Delivery)
admin.site.register(Brands)
admin.site.register(Requisites)
admin.site.register(CatalogGroups)
admin.site.register(Catalog)
