from django.contrib import admin
from Sales_Management.models import *

# Register your models here.

admin.site.register([CustomUser, CategoryModel, SaleModel])
