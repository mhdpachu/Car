from django.contrib import messages
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from . models import Car,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return render(request,'index.html')

def sign(request):
    if request.method == "POST":
        Username=request.POST['username']
        Email=request.POST['email']
        Password=request.POST['password']
        myuser=User.objects.create_user(Username,Email,Password)
        myuser.save()
        return redirect('login')
    return render(request,'sign.html')

def loginn(request):
    if request.method == "POST":
        Username=request.POST['username']
        Password=request.POST['password']
        user=authenticate(username=Username,password=Password)
        if user is not None:
            login(request,user)
            return redirect('add')
        else:
            return redirect('sign')
    return render(request,'login.html')

def home(request,category_id=None):
    categories=Category.objects.all()
    if category_id:
        item=Car.objects.filter(category_id=category_id)
    else:
        item=Car.objects.all()
       
    return render(request,'main.html',{'Item':item,'categories':categories})

def usercar(request):
    if request.method == "POST":
        name=request.POST['name']
        owner=request.POST['owner']
        model=request.POST['model']
        number=request.POST['phone']
        kilometer=request.POST['kilometer']
        price=request.POST['price']
        location=request.POST['location']
        image=request.FILES.get('image')
        category_id=request.POST['category']
        category=Category.objects.get(id=category_id)
        obj1=Car(Carname=name,Owner=owner,Carmodels=model,Contactnumber=number,Kilometer=kilometer,Price=price,Location=location,Carimage=image,category=category)
        obj1.save()
        return redirect('add')
    categories=Category.objects.all()
    return render(request,'userp.html',{'categories':categories})

def detail(request,pk):
    caritem=get_object_or_404(Car,pk=pk)
    return render(request,'detail.html',{'Caritem':caritem})
def search(request):
    query = request.GET.get('query', '')  # Retrieve the search query
    results = []
    message=""
    if query:
        results =Car.objects.filter(Carname__icontains=query)  # Adjust filter as needed
        if not results:
            message = f"No items found '{query}'."
    else:
        message = "please enter a search item."  # Check if a query exists
        
    return render(request,'search.html', {'results': results,'message':message})


def delete(request,delete_id):
    if request.method == "POST":
        item=get_object_or_404(Car,id=delete_id)
        item.delete()
    return redirect('add')
         
    