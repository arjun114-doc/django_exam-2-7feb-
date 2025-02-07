"""
URL configuration for E_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.Addproduct.as_view()),
    path('addreview/',views.Reviewproductview.as_view()),
    
    path('deletereview/',views.Deletereview.as_view()),
    path('showreview/<int:pk>',views.Review_of_a_product.as_view()),
    path('averagereview/',views.AverageReview.as_view()),
    
]
