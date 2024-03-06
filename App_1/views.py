from django.shortcuts import render
from django.http import HttpResponse
from App_1.models import *
from App_1.forms import *

def home(request):
    return render(request, "App_1/home.html")

# EMPLEADOS
def employee(request):
    if request.method == "POST":
    
        form_1 = Employee_form(request.POST)

        if form_1.is_valid():
            
            info = form_1.cleaned_data

            employee = Employee(employee_name = info["Nombre"], employee_last_name = info["Apellido"],employee_age = info["Edad"],employee_mail = info["Mail"])
       
            employee.save()

            return render(request, "App_1/home.html")
    
    else:
        form_1 = Employee_form()

    return render(request, "App_1/employee/employee.html", {"form_1":form_1})

# TIENDAS/LOCALES
def store(request):
    if request.method == "POST":
    
        form_2 = Store_form(request.POST)

        if form_2.is_valid():
            
            info = form_2.cleaned_data

            store = Store(postal_code = info["Codigo_postal"], street_name = info["Nombre_de_la_calle"],street_number = info["Altura_de_la_calle"])
       
            store.save()

            return render(request, "App_1/home.html")
    
    else:
        form_2 = Store_form()
    return render(request, "App_1/store/store.html", {"form_2" :form_2})

# PRODUCTOS
def product(request):
    if request.method == "POST":
    
        form_3 = Product_form(request.POST)

        if form_3.is_valid():
            
            info = form_3.cleaned_data

            product = Product(product_code = info["Codigo_del_producto"], product_name = info["Nombre_del_producto"],product_price = info["Precio"])
       
            product.save()

            return render(request, "App_1/home.html")
    
    else:
        form_3 = Product_form()

    return render(request, "App_1/product/product.html" , {"form_3" :form_3})

def search_product(request):
    return render(request, "App_1/product/product.html")
 
def product_results(request):
    if request.GET['product_code']:
        product_code = request.GET['product_code']
        product = Product.objects.filter(product_code__iexact = product_code)

        return render(request, "App_1/product/product.html",{"product":product, "product_code":product_code})
    else:
        respuesta = "No ingresaste un codigo"
        
    return HttpResponse(respuesta)