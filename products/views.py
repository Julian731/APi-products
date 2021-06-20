from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.core.cache import cache
from products.models import Productos, Archivos
from .forms import UploadFileForm
import json
import datetime

def home(request):
    cache.clear()
    productos=Productos.objects.all()
    return render(request, "products/prod.html", {"productos": productos})

def new(request):
    cache.clear()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_ini=request.FILES['file'].read()
            data_str=data_ini.decode('utf-8').replace("},\r\n]","}\r\n]")
            datos = json.loads(data_str)
            no_cargado=[]
            cargados=0
            for dato in datos:
                if len(dato['Nombre']) <= 64:
                    cargados+=1
                    cargar=Productos(ean=dato['Ean'],nombre=dato['Nombre'],descripcion=dato['Descripcion'],precio=dato['precio'])
                    cargar.save()
                else:
                    no_cargado+={"ean":dato['Ean'],"nombre":dato['Nombre'],"descripcion":dato['Descripcion'],"precio":dato['precio']}

            archive=Archivos(nombre=request.FILES['file'],cant_prod=len(datos),prod_val=cargados,created=datetime.datetime.now())
            archive.save()
            return redirect("../archivos/")
                
    else:
        form = UploadFileForm()
    return render(request, 'products/new_product.html', {'form': form})

def cargar_archivo(request):
    archivos=Archivos.objects.all()
    return render(request, "products/cargado.html", {"archivos": archivos})
    
def mod(request, p_id):
    product=Productos.objects.get(id=p_id)
    if request.method=="POST":
        product=Productos.objects.get(id=p_id)
        ean_u=request.POST.get("ean_act")
        nombre_u=request.POST.get("nombre_act")
        descripcion_u=request.POST.get("descripcion_act")
        precio_u=int(request.POST.get("precio_act"))
        product.ean=ean_u
        product.nombre=nombre_u
        product.descripcion=descripcion_u
        product.precio=precio_u
        product.save()
        return render(request, "products/mod.html", {"product": product})
    return render(request, "products/mod.html", {"product": product})