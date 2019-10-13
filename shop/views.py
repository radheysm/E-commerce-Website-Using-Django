from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product, Reg
from math import ceil
# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def login(request):
    return render(request, 'shop/login.html')


def signup(request):
    return render(request, 'shop/signup.html')


def contact(request):
    return HttpResponse("You can contact us at detail given below")


def tracker(request):
    return HttpResponse("Track your order here")


def search(request):
    return HttpResponse("Search Anything here that you wish to buy Today")


def prodview(request):
    return HttpResponse("ProductViews")


def checkout(request):
    return HttpResponse("You check Out your Cart from here")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        password = request.POST.get('password', '')
        reg = Reg(first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password)
        reg.save()
    return HttpResponse("Successfully Register! Welcome to myCart!!!")


def sign(request):
    if request.method == "POST":
        a = []
        a = Reg.objects.values('email', 'password')
        email = {item['email'] for item in a}
        password = {item['password'] for item in a}

        # print(email,password)
        emaill = request.POST.get('email', '')
        passwordd = request.POST.get('password', '')
        if emaill in email and passwordd in password:
            return render(request, 'shop/index.html')
        else:
            return HttpResponse("Incorrect Password or Email Address please check and try again")



