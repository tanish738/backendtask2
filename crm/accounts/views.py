from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .forms import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView


# Create your views here.
def loginpage(request):

    context={}
    return render(request,"login.html",context)

def register(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was craeted successfully")
            return redirect('login')
    context={"form":form}
    return render(request,"register.html",context)

def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    pending=orders.filter(status="Pending").count()
    delivered=orders.filter(status="Delivered").count()
    context={
        "orders":orders,
        "customers":customers,
        "total_customers":total_customers,
        "total_orders":total_orders,
        "pending":pending,
        "delivered":delivered,
        }
    return render(request,"dashboard.html",context)

def products(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request, 'products.html',context)

def products_create(request):
    form=ProductForm()
    context={"form":form}
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    return render(request,"products_create.html",context)

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=Order.objects.filter(customer=customer)
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    total_orders=orders.count()
    context={"customer":customer,"orders":orders,"total_orders":total_orders,"myFilter":myFilter}
    return render(request, 'customer.html',context)

def createOrder(request,pk):
    customer=Customer.objects.get(id=pk)
    form=OrderForm(initial={"customer":customer})
    if request.method=="POST":
        #form=OrderForm(request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print("oh")
    context={"form":form}
    return render(request,"order_form.html",context)

def updateOrder(request,pk):
    try:
        order=Order.objects.get(id=pk)
    except:
        order=Order.objects.first()
    customer=order.customer
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={"form":form}
    return render(request,"order_form.html",context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect("/")
    context={"item":order}
    return render(request,"delete.html",context)




class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

