from django.contrib import admin
from .models import Benefits, Products, Delivery, Brands, Requisites

# class BenefitsAdmin(admin.ModelAdmin):
#     fields = ['title', 'subtitle', 'image',]
admin.site.site_header = "Панель администрирования"

admin.site.register(Benefits)
admin.site.register(Products)
admin.site.register(Delivery)
admin.site.register(Brands)
admin.site.register(Requisites)
