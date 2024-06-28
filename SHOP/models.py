from django.db import models

class PRODUCT(models.Model):
    PRODUCT_ID = models.AutoField
    PRODUCT_NAME = models.CharField(max_length=50)
    CATEGORY = models.CharField(max_length=50 , default="")
    SUBCATEGORY = models.CharField(max_length=50 , default="")
    PRICE = models.IntegerField(default=0)
    DESCRIPTION = models.CharField(max_length=500)
    PUBLISH_DATE = models.DateField()
    IMAGE = models.ImageField(upload_to="SHOP/IMAGES" , default="")


    def __str__(self):
        return self.PRODUCT_NAME
    
class CONTACT(models.Model):
    MESSAGE_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50 , default="")
    PHONE = models.CharField(max_length=50 , default="")
    DESC = models.CharField(max_length=50 , default="")
    


    def __str__(self):
        return self.NAME
    
    