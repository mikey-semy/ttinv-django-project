from django.contrib import admin
from .models import Benefits

# class BenefitsAdmin(admin.ModelAdmin):
#     fields = ['title', 'subtitle', 'image',]

admin.site.register(Benefits)
