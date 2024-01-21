from django.contrib import admin
from .models import Benefits, Products, Deliveries, Brands, Requisites, Catalogs, Categories, Groups

# class BenefitsAdmin(admin.ModelAdmin):
#     fields = ['title', 'subtitle', 'image',]
admin.site.site_header = "Панель администрирования"

admin.site.register(Benefits)
admin.site.register(Products)
admin.site.register(Deliveries)
admin.site.register(Brands)
admin.site.register(Requisites)

admin.site.register(Catalogs)
admin.site.register(Groups)
admin.site.register(Categories)