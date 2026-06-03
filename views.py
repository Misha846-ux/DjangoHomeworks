from typing import Dict, Union
import json
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from datetime import datetime, date, timedelta
import random
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import Post, ContactInfo, Product, Buyer, Seller, SellInfo, RestauranTypes, Restauran

# Create your views here.

def homework7_3(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
def homework7_4(request):
    if request.method == 'GET':
        arr: list[str] = []
        for i in range(11):
            for j in range(11):
                arr.append(f"{i} x {j} = {i*j}")
        return HttpResponse("<br>".join(arr))
def homework7_5(request):
    if request.method == 'GET':
        dayDate = date(date.today().year, date.today().month, date.today().day) + timedelta(days=256)
        return HttpResponse(dayDate)


def homework8_1(request):
    return render(request, 'Homework8/English.html')

def homework8_2(request):
    return render(request, 'Homework8/France.html')

def homework8_3(request):
    return render(request, 'Homework8/Deutsche.html')

def homework8_4(request):
    return render(request, 'Homework8/Spanish.html')

@csrf_exempt
def homework9_register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'Homework9/register.html')
    elif request.method == 'POST':
        name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        age = request.POST.get('age', '')
        email = request.POST.get('email', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        subscribe = request.POST.get('subscribe', '')

        data = {
            'first_name': name,
            'last_name': last_name,
            'age': age,
            'email': email,
            'gender': gender,
            'address': address,
            'subscribe': subscribe,
        }
        return render(request, 'Homework9/result.html', data)

@csrf_exempt
def home(request: HttpRequest):
    if request.method == 'GET':
        posts = ContactInfo.objects.all()
        # name = request.GET.get("name")
        # age = request.GET.get("age")
        # data: Dict[str, Union[str, int]] = {
        #     "name":name,
        #     "age":age
        # }
        return render(request, 'home.html', {"posts": posts})
    elif request.method == 'POST':
        body = json.loads(request.body)
        return JsonResponse({"messeg": body.get("name")})




def about(request):
    return render(request, "about.html")


@csrf_exempt
def deleteObj(request: HttpRequest, id):
    if request.method == 'DELETE':
        print(id)
        ContactInfo.objects.filter(id=id).delete()
        return JsonResponse({"message": "Deleted"})
    return HttpResponse("Oh my god")


@csrf_exempt
def contacts(request: HttpRequest):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        ContactInfo.objects.create(
            name=body.get("name"),
            secondName=body.get("secondName"),
            email=body.get("email"),
            phoneNumber=body.get("phoneNumber"),
            notes=body.get("notes")
        
    )
    else:
        return render(request, "contacts.html",)  # type: ignore
    

def test(request, id):
    return HttpResponse("Oh my god")

def getCourentDate(request):
    day_name = datetime.now().strftime('%A')
    return HttpResponse(day_name)

def get_random_quote(request):
    quotes = [
        "История — это учитель жизни.",
        "Знание — сила.",
        "Музей — это память человечества.",
        "Кто не знает прошлого, не имеет будущего.",
        "Искусство — это способ видеть невидимое."
    ]
    
    return HttpResponse(random.choice(quotes))


###########################################Homework12
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})
    elif request.method == 'POST':
        Product.objects.create(
            title=request.POST.get("title", ""),
            price=int(request.POST.get("price", 0)),
            description=request.POST.get("description", ""),
            quantity=int( request.POST.get("quantity", 0))
        )
        return render(request, "products.html", {"products": Product.objects.all()})


def get_Buyers(request):
    if request.method == 'GET':
        buyers = Buyer.objects.all()
        return render(request, "Buyers.html", {"buyers": buyers})
    elif request.method == 'POST':
        Buyer.objects.create(
            name=request.POST.get("name", ""),
            secondName=request.POST.get("secondName", ""),
            email=request.POST.get("email", ""),
            phoneNumber=request.POST.get("phoneNumber", "")
        )
        return render(request, "Buyers.html", {"buyers": Buyer.objects.all()})


def get_sellers(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        return render(request, "Seller.html", {"sellers": sellers})
    elif request.method == 'POST':
        Seller.objects.create(
            name=request.POST.get("name", ""),
            secondName=request.POST.get("secondName", ""),
            email=request.POST.get("email", ""),
            phoneNumber=request.POST.get("phoneNumber", ""),
            role=request.POST.get("role", "seller")
        )
        return render(request, "Seller.html", {"sellers": Seller.objects.all()})


def get_sales(request):
    if request.method == 'GET':
        sales = SellInfo.objects.select_related("product", "buyer", "seller").all()
        products = Product.objects.all()
        buyers = Buyer.objects.all()
        sellers = Seller.objects.all()
        return render(request, "SellInfo.html", {
            "sales": sales,
            "products": products,
            "buyers": buyers,
            "sellers": sellers
        })
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get("product"))
        buyer = Buyer.objects.get(id=request.POST.get("buyer"))
        seller = Seller.objects.get(id=request.POST.get("seller"))
        SellInfo.objects.create(
            product=product,
            buyer=buyer,
            seller=seller,
            price=int(request.POST.get("price", product.price)),
            quantity=int(request.POST.get("quantity", 1))
        )
        sales = SellInfo.objects.select_related("product", "buyer", "seller").all()
        return render(request, "SellInfo.html", {
            "sales": sales,
            "products": Product.objects.all(),
            "buyers": Buyer.objects.all(),
            "sellers": Seller.objects.all(),
            "message": "Sale created"
        })

    


#######################################################Restauran

def restauranMain(request):
    return render(request, "restaurant/main.html")

@csrf_exempt
def addRestauran(request):
    if(request.method == "GET"):
        rTypes = RestauranTypes.objects.all();
        return render(request, "restaurant/addRestauran.html", {"rTypes": rTypes})
    elif (request.method == "POST"):
        body = json.loads(request.body)
        rst = Restauran.objects.create(
            name = body.get("name"),
            adress = body.get("adress"),
            phoneNumber = body.get("phoneNumber"),
            website = body.get("website"),
        )

        for el in body.get("restauranType"):
            rst.restauranType.add(RestauranTypes.objects.filter(id = el))
        return JsonResponse({"message": "Product created"})
