from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import OrderFilter
from django .contrib.auth.forms import UserCreationForm


def loginPage(request):

    context = {}
    return render(request, 'login.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def products(request):
    products = product.objects.all()
    return render(request, 'product.html', {'products': products})


def customers(request, cid):
    customers = customer.objects.get(id=cid)
    orders = customers.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customers': customers,
               'orders': orders, 'order_count': order_count, 'myFilter': myFilter}

    return render(request, 'customer.html', context)


def dashboard(request):
    orders = order.objects.all()
    customers = customer.objects.all()

    total_orders = orders.count()
    Delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'Delivered': Delivered, 'pending': pending}

    return render(request, 'dashboard.html', context)


def updateOrder(request, cid):
    orders = order.objects.get(id=cid)
    form = orderForm(instance=orders)

    if request.method == 'POST':
        form = orderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, cid):
    item = order.objects.get(id=cid)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html', context)


def UpdateCustomer(request, cid):
    orders = customer.objects.get(id=cid)
    form1 = updateForm(instance=orders)

    if request.method == 'POST':
        form1 = updateForm(request.POST, instance=orders)
        if form1.is_valid():
            form1.save()
            return redirect('/')

    context = {'form1': form1}
    return render(request, 'update_form.html', context)


def placeOrder(request, cid):
    orders = customer.objects.get(id=cid)
    form3 = orderForm(initial={'customer': orders})
    if request.method == 'POST':
        form3 = orderForm(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('/')

    context = {'form3': form3}
    return render(request, 'create_order.html', context)


def createCustomer(request):
    form4 = updateForm()
    if request.method == 'POST':
        form4 = updateForm(request.POST)
        if form4.is_valid():
            form4.save()
            return redirect('/')

    context = {'form4': form4}
    return render(request, 'create_customer.html', context)
