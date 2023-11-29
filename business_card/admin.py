from django.contrib import admin
from .models import Benefits, Products

# class BenefitsAdmin(admin.ModelAdmin):
#     fields = ['title', 'subtitle', 'image',]
admin.site.site_header = "Панель администрирования"

admin.site.register(Benefits)
admin.site.register(Products)
