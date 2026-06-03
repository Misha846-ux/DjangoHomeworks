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

def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})
    elif request.method == 'POST':
        body = json.loads(request.body)
        Product.objects.create(
            title=body.get("title"),
            price=body.get("price")
        )
        return JsonResponse({"message": "Product created"})

def get_Buyers(request):
    buyers = Buyer.objects.all()
    return render(request, "Buyers.html", {"buyers": buyers})


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
