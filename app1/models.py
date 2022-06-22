from django.db import models


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=225)
    company_address = models.CharField(max_length=225)
    company_email = models.EmailField()
    company_phonenumber = models.BigIntegerField()


class Product(models.Model):
    name=models.CharField(max_length=225)
    product_image = models.ImageField()
    product_description = models.TextField()
    product_price = models.DecimalField(decimal_places=2,max_digits=5)
    product_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    product_totalQuatity = models.IntegerField(default=10)
    product_availableQuantity = models.IntegerField(default=1)




