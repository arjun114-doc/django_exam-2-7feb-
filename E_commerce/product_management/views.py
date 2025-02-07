from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from product_management.forms import Productform,Reviewform
from product_management.models import Product,Review

class Addproduct(View):
    def get(self,request):
        form=Productform
        return render(request,"addproduct.html",{'form':form})
    
    def post(self,request):
        form=Productform(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return render(request,"addsuccess.html")
        
class Reviewproductview(View):
    def get(self,request):
        form=Reviewform
        return render(request,"addreview.html",{'form':form})
    
    def post(self,request):
        form=Reviewform(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            return render(request,"reviewadded.html")
        else:
            return render(request,'reviewfailed.html')


class Deletereview(View):
    def get(self,request, **kwargs):
        id=kwargs.get('pk')
        Review.objects.get(id=id).delete()
        
class Review_of_a_product(View):
    def get(self,request, **kwargs):
        id=kwargs.get('pk')
        data=Review.objects.get(id=id)
        return render(request,"reviewall.html",{"data":data})
    
                
class AverageReview(View):
    def get(self,request):
        data=Review.objects.all()
        return render(request,"averagereview.html",{'data':data})