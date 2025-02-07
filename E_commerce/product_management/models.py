from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    discription=models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    

    
class Review(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    reviewer_name=models.CharField(max_length=50)
    rating=models.IntegerField()
    comment=models.CharField(max_length=100)
    review_date=models.DateField(auto_now=True)
    
    

    
    
