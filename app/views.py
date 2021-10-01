from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart, Order_Placed, Customer
from .forms import CustomerRegister, CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# class ProductView(View):
#     def get(self, request):

def home(request):
    top = Product.objects.filter(catagory='TW')

    bottom = Product.objects.filter(catagory='BW')
    mob = Product.objects.filter(catagory='M')
    my_dict = {'topwears': top, 'bottomwears': bottom, 'mobile': mob}
    return render(request, 'app/home.html', context=my_dict)


def product_detail(request, id):
    detail = Product.objects.get(id=id)

    return render(request, 'app/productdetail.html', {'detail': detail})

@login_required(login_url='/login')
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    prod = Product.objects.get(id=product_id)
    Cart(user=user, product=prod).save()
    return redirect('/cart')


@login_required(login_url='/login')
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.00
        ship_amount = 70.00
        total = 0.00
        obj = [p for p in Cart.objects.all() if p.user == user]
        if obj:
            for x in obj:
                tmpamount = (x.quantity * x.product.discount_price)
                amount = amount + tmpamount
                total = amount + ship_amount
        return render(request, 'app/addtocart.html', {'carts': cart, 'amount': amount, 'total': total})

@login_required(login_url='/login')
def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity = c.quantity + 1
        c.save()
        amount = 0.00
        ship_amount = 70.00
        total = 0.00
        obj = [p for p in Cart.objects.all() if p.user == request.user]
        if obj:
            for x in obj:
                tmpamount = (x.quantity * x.product.discount_price)
                amount = amount + tmpamount
                # total = amount + ship_amount
            data = {'c': c.quantity, 'amount': amount, 'total': amount + ship_amount}
            return JsonResponse(data)

@login_required(login_url='/login')
def Minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity = c.quantity - 1
        c.save()
        amount = 0.00
        ship_amount = 70.00
        total = 0.00
        obj = [p for p in Cart.objects.all() if p.user == request.user]
        if obj:
            for x in obj:
                tmpamount = (x.quantity * x.product.discount_price)
                amount = amount + tmpamount
                # total = amount + ship_amount
            data = {'c': c.quantity, 'amount': amount, 'total': amount + ship_amount}
            return JsonResponse(data)

@login_required(login_url='/login')
def Remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.00
        ship_amount = 70.00
        total = 0.00
        obj = [p for p in Cart.objects.all() if p.user == request.user]
        if obj:
            for x in obj:
                tmpamount = (x.quantity * x.product.discount_price)
                amount = amount + tmpamount
                total = amount + ship_amount
            data = {'amount': amount, 'total': total}
            return JsonResponse(data)

@login_required(login_url='/login')
def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required(login_url='/login')
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})

@login_required(login_url='/login')
def orders(request):
    op = Order_Placed.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'op': op})


def mobile(request, data=None):
    global mobiles
    if data is None:
        mobiles = Product.objects.filter(catagory='M')
    elif data == 'Samsung' or data == 'Nokia':
        mobiles = Product.objects.filter(catagory='M').filter(brand=data)
    elif data == "Below":
        mobiles = Product.objects.filter(catagory='M').filter(discount_price__lt=10000)
    elif data == "Above":
        mobiles = Product.objects.filter(catagory='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    user_form = CustomerRegister()
    if request.method == 'POST':
        user_form = CustomerRegister(request.POST)
        if user_form.is_valid():
            users = user_form.save()
            # users.set_password(users.set_password)
            users.save()
        else:
            print(user_form.errors)

        return redirect('login')
    return render(request, 'app/customerregistration.html', {'user_form': user_form})

@login_required(login_url='/login')
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.00
    ship_amount = 70.00
    total = 0.00
    obj = [p for p in Cart.objects.all() if p.user == request.user]
    if obj:
        for p in obj:
            tempamount = (p.quantity * p.product
                          .discount_price)
            amount = amount + tempamount
            total = ship_amount + amount

    return render(request, 'app/checkout.html', {'add': add, "cart_item":cart_items, "total":total})

@login_required(login_url='/login')
def payment_done(request):
    user = request.user
    custid = request.GET.get("custid")
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Order_Placed(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')

@login_required(login_url='/login')
def profile(request):
    c_form = CustomerForm()
    if request.method == 'POST':
        c_form = CustomerForm(request.POST)
        if c_form.is_valid():
            usr = request.user
            name = c_form.cleaned_data['name']
            locality = c_form.cleaned_data['locality']
            city = c_form.cleaned_data['city']
            state = c_form.cleaned_data['state']
            zip_code = c_form.cleaned_data['zip_code']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zip_code=zip_code)
            reg.save()
            messages.success(request, 'Congratulations! profile has been updated')

    return render(request, 'app/profile.html', {'c_form': c_form, 'active': 'btn-primary'})
