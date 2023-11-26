from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib import messages


class ProductView(View):
    def get(self, request):
        menwears = Product.objects.filter(category = 'M')
        womenwears = Product.objects.filter(category = 'W')
        childernwears = Product.objects.filter(category = 'C')
        home_appliances = Product.objects.filter(category = 'H')
        cosmetics_gadgets = Product.objects.filter(category = 'G')
        return render(request, 'app/home.html', {"menwears": menwears, "womenwears": womenwears,
        "childernwears":childernwears, "home_appliances":home_appliances, "cosmetics_gadgets": cosmetics_gadgets})
  
class ProductDetailView(View):
  def get(self, request, pk):
    product = Product.objects.get(pk =pk)
    return render(request, 'app/productdetail.html',
        {'product':product})

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount= 0.0
        shipping_amount= 100.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'amount':amount, 'totalamount': totalamount})
        else:
            return render(request, 'app/emptycart.html')
   


def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def homeappliances(request, data=None):
    if data is None:
        homeappliances = Product.objects.filter(category='H')
    elif data == 'Samsung' or data == 'LG' or data == 'Sony' or data == 'Whirlpool' or data == 'Philips': 
        homeappliances = Product.objects.filter(category='H', brand=data)
    return render(request, 'app/homeappliances.html', {'homeappliances': homeappliances})

class CustomerRegistratioinView(View):
   def get(self, request):
      form = CustomerRegistrationForm()
      return render(request, 'app/customerregistration.html', {'form':form})
   
   def post(self, request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         messages.success(request, 'Congratulations!! Registration Sucsessfully')
         form.save()
      return render(request, 'app/customerregistration.html', {'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')


def menwear(request):
    menwear = Product.objects.filter(category='M')
    return render(request, 'app/menwear.html', {'menwear': menwear})

def womenwear(request):
    womenwear = Product.objects.filter(category='W')
    return render(request, 'app/womenwear.html', {'womenwear': womenwear})

def childrenwear(request):
    childrenwear = Product.objects.filter(category='C')
    return render(request, 'app/childrenwear.html', {'childrenwear': childrenwear})

def cosmetics(request):
    cosmetics = Product.objects.filter(category='G')
    return render(request, 'app/cosmetics.html', {'cosmetics': cosmetics})

class ProfileView(View):
   def get(self, request):
      form = CustomerProfileForm()
      return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
   
   def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            reg = Customer(user=usr, name=name, locality=locality, city=city, phone_number=phone_number)
            reg.save()
            messages.success(request, 'Congratulations!! Profile updated Successfully!!')
        return render(request, 'app/profile.html', {'form':form , 'active':'btn-primary'})

        