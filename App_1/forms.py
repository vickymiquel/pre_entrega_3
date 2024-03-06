from django import forms

class Employee_form(forms.Form):
    Nombre = forms.CharField(max_length = 30)
    Apellido = forms.CharField(max_length = 30)
    Edad = forms.IntegerField()
    Mail = forms.EmailField()

class Store_form(forms.Form):
    Codigo_postal = forms.IntegerField()
    Nombre_de_la_calle = forms.CharField(max_length = 30)
    Altura_de_la_calle = forms.IntegerField()

class Product_form(forms.Form):
    Codigo_del_producto = forms.IntegerField()
    Nombre_del_producto = forms.CharField(max_length = 50)
    Precio = forms.IntegerField()