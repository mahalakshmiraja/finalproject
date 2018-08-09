from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .models import ProductName, ProductTestCase, TestRun
from django.contrib import messages



# Create your views here.
def index(request):
    print ("index!!!")
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message" : "Invalid credentials"})

    if request.method == 'GET':
        print ("get!!!")
        context = {
            "user": request.user,
            "product": ProductName.objects.all()
        }
        return render(request, "index.html",context)

    if request.method == 'POST':
        print ("post!!!")
        product = request.POST["product"]
        allproduct = ProductName.objects.values()
        print(product)
        print(allproduct)

        context_old = {
                    "user": request.user,
                    "product": ProductName.objects.all(),
                    "message": ""
                }

        for i in range(0,len(allproduct)):
            if allproduct[i]['product'] == product:
                print (product + " already in system")
                context_old["message"] = product + " already in system"
                return render(request, "index.html", context_old)

        newproduct = ProductName(product=product)
        newproduct.save()
        context = {
            "user": request.user,
            "product": ProductName.objects.all()
        }
        return render(request, "index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    print(username)
    print(password)
    if user is not None:
        print(user)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        print("User is None")
        return render(request, "login.html", {"message": "Invalid credentials"})



def newuser_view(request):
    print("newuser_view")
    if request.method == 'GET':
        return render(request, "newuser.html")
    if request.method == 'POST':
        username = request.POST["usernme"]
        password = request.POST["passwrd"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email1 = request.POST["email"]
        hashedPassword = make_password(password)
        print(username)
        print(password)

        if len(email1) > 0:
            newUser = User.objects.create_user(username=username,
                                 email=email1,
                                 password=password)
            newUser.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged Out"})


def testCase_view(request, productId):
    print("testCase_view")
    product = ProductName.objects.get(id=productId)
    print (product)
    if request.method == 'GET':
        print ("Get testcases for product: " + product.product + " productId: " + str(productId))
        context = {
            "user": request.user,
            "testcases": ProductTestCase.objects.filter(product=product),
            "product": product
        }
        return render(request, "testcase.html", context)

    if request.method == 'POST':
        testcase = request.POST["testcase"]
        print ("Trying to create new testcase: " + testcase)

        currentProductTestcase = ProductTestCase.objects.filter(product=product)
        print ("len(currentProductTestcase) = " + str(len(currentProductTestcase)))
        if len(currentProductTestcase) > 0:
            for i in range(0,len(currentProductTestcase)):
                print (currentProductTestcase[i])
                if currentProductTestcase[i].testcase == testcase:
                    context = {
                        "user": request.user,
                        "testcases": currentProductTestcase,
                        "product": product,
                        "message": testcase + " already associated with product"
                        }
                    return render(request, "testcase.html", context)

        newtestcase = TestCase(testcase=testcase, product=product)
        print(newtestcase)
        newtestcase.save()
        context = {
            "user": request.user,
            "testcases": ProductTestCase.objects.filter(product=product),
            "product": product,
            "message": testcase + " added to product: " + product.product
            }
        return render(request, "testcase.html", context)



def testrun_view(request):
    print("testrun_view")
    product = ProductName.objects.get(id=productId)
    print (product)
    if request.method == 'GET':
        print ("Get testcases for product: " + product.product + " productId: " + str(productId))
        context = {
            "user": request.user,
            "testcases": ProductTestCase.objects.filter(product=product),
            "product": product
        }
        return render(request, "testcase.html", context)

    if request.method == 'POST':
        testcase = request.POST["testcase"]
        print ("Trying to create new testcase: " + testcase)

        currentProductTestcase = ProductTestCase.objects.filter(product=product)
        print ("len(currentProductTestcase) = " + str(len(currentProductTestcase)))
        if len(currentProductTestcase) > 0:
            for i in range(0,len(currentProductTestcase)):
                print (currentProductTestcase[i])
                if currentProductTestcase[i].testcase == testcase:
                    context = {
                        "user": request.user,
                        "testcases": currentProductTestcase,
                        "product": product,
                        "message": testcase + " already associated with product"
                        }
                    return render(request, "testcase.html", context)

        newtestcase = TestCase(testcase=testcase, product=product)
        print(newtestcase)
        newtestcase.save()
        context = {
            "user": request.user,
            "testcases": ProductTestCase.objects.filter(product=product),
            "product": product,
            "message": testcase + " added to product: " + product.product
            }
        return render(request, "testcase.html", context)
