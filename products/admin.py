from django.contrib import admin
from .models import Productos, Archivos

# Register your models here.
# class product_adm(admin.ModelAdmin):
#     readonly_fields=('creado','modificado')

admin.site.register(Productos)