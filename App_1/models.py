from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length = 30)
    employee_last_name = models.CharField(max_length = 30)
    employee_age = models.IntegerField()
    employee_mail = models.EmailField()

    def __str__(self):
        return f"{self.employee_name} {self.employee_last_name} --- {self.employee_mail}"

class Store(models.Model):
    postal_code = models.IntegerField()
    street_name = models.CharField(max_length = 30)
    street_number = models.IntegerField()

    def __str__(self):
            return f"{self.postal_code} --- {self.street_name} {self.street_number}"

class Product(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length = 50)
    product_price = models.IntegerField()
  
    def __str__(self):
        return f"{self.product_code} --- {self.product_name}  ${self.product_price}"
