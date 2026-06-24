from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Sales_Management.models import *

# Create your views here.

def register_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        
        you_exist = CustomUser.objects.filter(username = username).exists()
        
        if you_exist:
            messages.warning(request, "Your Username Already Exists")
            return redirect('register_view')
        
        if password == c_password:
            CustomUser.objects.create_user(
                username = username,
                email = email,
                full_name = full_name,
                password = password
            )
            messages.success(request, "Account Created Successfully")
            return redirect('login_view')
        
        else:
            messages.warning(request, "Please fill the form carefully")
            return redirect('register_view')
       
    return render(request, 'auth/register.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            messages.success(request, "Congratulation, Log-in Successfully")
            return redirect('dash_board')
        
        else:
            messages.warning(request, "Invalid Username or Credentials")
            return redirect('login_view')
        
    return render(request, 'auth/log_in.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def dash_board(request):
    return render(request, 'dashboard.html')

def sale_list(request):
    sale_data = SaleModel.objects.all()
    
    context = {
        'sale' : sale_data,
    }
    return render(request, 'sale/sale_list.html', context)

def add_sale(request):
    cate = CategoryModel.objects.all()
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        unit_price = request.POST.get('unit_price')
        quantity = request.POST.get('quantity')
        discount_percent = request.POST.get('discount_percent')
        tax_percent = request.POST.get('tax_percent')
        
        up = float(unit_price)
        qty = int(quantity)
        dp = float(discount_percent)
        tp = float(tax_percent)
        
        total_price = (up * qty) - ((up * qty) * dp / 100) + ((up * qty) * tp / 100)
        
        cat = CategoryModel.objects.get(id = category)
        
        SaleModel.objects.create(
            product_name = product_name,
            category = cat,
            unit_price = unit_price,
            quantity = quantity,
            discount_percent = discount_percent,
            tax_percent = tax_percent,
            total_price = total_price
        )
        messages.success(request, "New {{product_name}} Sale Added Successfully")
        return redirect('sale_list')
    
    context = {
        'cate' : cate
    }        
    return render(request, 'sale/add_sale.html', context)

def update_sale(request, s_id):
    sale_data = SaleModel.objects.get(id = s_id)
    cate = CategoryModel.objects.all()
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        unit_price = request.POST.get('unit_price')
        quantity = request.POST.get('quantity')
        discount_percent = request.POST.get('discount_percent')
        tax_percent = request.POST.get('tax_percent')
        
        cat = CategoryModel.objects.get(id = category)
        
        up = float(unit_price)
        qty = int(quantity)
        dp = float(discount_percent)
        tp = float(tax_percent)
        
        total_price = (up * qty) - ((up * qty) * dp / 100) + ((up * qty) * tp / 100)
        
        sale_data.product_name = product_name
        sale_data.category = cat
        sale_data.unit_price = unit_price
        sale_data.quantity = quantity
        sale_data.discount_percent = discount_percent
        sale_data.tax_percent = tax_percent
        sale_data.total_price = total_price
        sale_data.save()
        
        messages.success(request, "{{product_name}} Sale Updated Successfully")
        return redirect('sale_list')
    
    context = {
        'cate' : cate,
        'sale_data' : sale_data
    }        
    return render(request, 'sale/update_sale.html', context)

def delete_sale(request, s_id):
    SaleModel.objects.get(id = s_id).delete()
    return redirect('sale_list')
