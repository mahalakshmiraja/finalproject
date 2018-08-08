from django.contrib import admin
from .models import ProductName, ProductTestCase, TestRun

# Register your models here.

admin.site.register(ProductName)
admin.site.register(ProductTestCase)
admin.site.register(TestRun)