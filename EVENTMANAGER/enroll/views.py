from email.policy import HTTP
from select import select
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import redirect, render
from .models import login, create_acc, kitchen, OrderItem
import datetime
from django.conf import settings
from django.contrib import messages
from django.views.decorators.cache import cache_control
# from cart.cart import Cart




def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def log(request):
    
    if request.method == "POST":

        data = create_acc.objects.all()
        obj = login()

        obj.uname = request.POST.get('uname')
        obj.upass = request.POST.get('upass')

        err = "Invalid Username or Password"
        ok = False

        for row in data:
            print(row.uname)
            if row.uname == str(obj.uname) and row.pswd == str(obj.upass):
                ok = True 
        
        if ok == False:
            return render(request, 'invalid.html', {'message':err})
        
        return render(request, 'dashboard.html')

    else:
        return render(request, 'login_page.html')

def create(request):

    if request.method == "POST":
        obj = create_acc()

        obj.fname = request.POST.get('fname')
        obj.lname = request.POST.get('lname')
        obj.hemail = request.POST.get('hemail')
        obj.uname = request.POST.get('uname')
        obj.pswd =  request.POST.get('pswd')
        obj.mobno = request.POST.get('mobno')
        
        clash = create_acc.objects.filter(hemail = obj.hemail)

        inside = False
        for c in clash:
            inside = True
        if inside:
            return render(request, 'invalid.html', {'message':"You have already registered"})

        obj.save()

        return render(request, 'login_page.html')

    else:
        template = loader.get_template('createacc.html')
        context = {

        }
        return HttpResponse(template.render(context,request))

def order_now(request):
    
    selected = []
    if request.method == "POST":
        return render(request, 'order_display.html', {'selected':selected})
    else:
        
        chinese = kitchen.objects.filter(desc="chinese")
        punjabi = kitchen.objects.filter(desc="punjabi")
        italian = kitchen.objects.filter(desc="italian")
        gujarati= kitchen.objects.filter(desc="gujarati")
        south =   kitchen.objects.filter(desc="south")
        beverages = kitchen.objects.filter(desc="beverages")
        context = {
                'chinese': chinese,
                'punjabi': punjabi,
                'italian': italian,
                'gujarati': gujarati,
                'south': south,
                'beverages':beverages,
                'selected' : selected,
                }

        return render(request, 'order.html', context )

def dashbrd(request):
    return render(request, 'dashboard.html')

def add(request):

    if request.method == "POST":

        obj = kitchen();
        obj.item = request.POST.get('iname')
        obj.price = request.POST.get('price')
        obj.desc = request.POST.get('food')

        obj.save()

        return render(request, 'dashboard.html')
    else:
        return render(request, 'add_item.html')

def delt(request):

    if request.method == "POST":

        obj = kitchen();
        obj.item = request.POST.get('dname')

        err = "Item not available in the inventory"

        try:
            it = kitchen.objects.get(item = obj.item)
        except:
            return render(request, 'invalid.html', {'message':err})
        
        it.delete()

        return render(request, 'dashboard.html')
    else:
        return render(request, 'delete_item.html')

def webb(request):
    return render(request, 'web.html')

