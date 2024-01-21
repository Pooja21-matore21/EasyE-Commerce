from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,Recommendation
from UserApp.models import UserInfo,MyCart
from django.http import HttpResponse
# Create your views here.
def home(request):

    cats = Category.objects.all()
    products = Product.objects.all()
    return render(request,'master.html',{"cats":cats , "products":products})
    '''arr = ['boat','mi','samsung','vivo']
    mydict = {
        "arr": arr
    }
    return render(request,'master.html',mydict="mydict")'''
    

def ShowProduct(request,id):
    cats = Category.objects.all()
    products = Product.objects.filter(category = id) # 1 brand having multiple product
    return render(request,'master.html',{"cats":cats , "products":products})

def ViewDetails(request,id):
    cats = Category.objects.all()
    product = Product.objects.get(id=id)
    return render(request,"ViewDetails.html",{"cats":cats , "product":product})


def addToCart(request):
    if ("uname" in request.session):
        user = UserInfo.objects.get(username=request.session["uname"])
        #get the product info 
        product_id = request.POST["cid"]
        product = Product.objects.get(id=product_id)
        qty = request.POST["qty"]
        #item = MyCart.objects.get(user=user, product=product, qty=qty)
        cart = MyCart()
        cart.user = user
        cart.product = product
        cart.qty = qty
        cart.save()
        return redirect(home)    
    else:
        return redirect(Login)

def showCartItems(request):
    cats = Category.objects.all()
    # fetch those request which added by user
    if (request.method == "GET"):
        items = MyCart.objects.filter(user=request.session["uname"])
        total = 0
        for item in items:
            total += int(item.qty) * int(item.product.price)
        request.session["total"] = total
        return render(request, "showCartItems.html", {"items": items, "cats": cats})
    else:
        cart_id = request.POST["cart_id"]
        item = MyCart.objects.get(id=cart_id)
        action = request.POST["action"]
        if (action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(showCartItems)



def SignOut(request):
    # delete the session/relese the user
    request.session.clear()
    return redirect(home)


def Login(request):
    if (request.method == "GET"):
        return render(request, "Login.html", {})
    else:

        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            user = UserInfo.objects.get(username=uname, password=pwd)
        except:
            msg = "Invalid credentials..Please try again..!!"
            return render(request, "Login.html", {"msg": msg})
        else:
            request.session["uname"] = uname
            return redirect(home)



def SignUp(request):
    if (request.method == "GET"):
        return render(request, "signup.html", {})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        age = request.POST["age"]
        address = request.POST["address"]
        try:
            #is user already present
            user = UserInfo.objects.get(username=uname)
        except:
            #we can create user as user is not present
            user = UserInfo(uname,pwd,age,address)
            user.save()
            return redirect(home)
        else:
            msg = "This user is already exist..!!"
            return render(request, "signup.html", {"msg": msg})
