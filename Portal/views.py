from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from .forms import UsersLoginForm 
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login-page.html', {})

def profile(request):
    context = {}
    data = get_object_or_404(Register, user__id=request.user.id)
    context["data"]=data        
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        con = request.POST["contact_number"]
        fat = request.POST["fathers_name"]
        add = request.POST["address"]
        # gen = request.POST["gender"]
        

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.contact_number = con
        data.fathers_name = fat
        data.address = add
        # data.gender = gen
        data.save()
    return render(request,'profile-page.html',context)

def auth(request):
    return render(request,'auth.html')    

def register(request):
    if request.method=="POST":
        un = request.POST["username"]
        fname = request.POST["first_name"]
        last = request.POST["last_name"]
        pwd = request.POST["password"]
        em = request.POST["email"]
        # cem = request.POST["confirm_email"]
        con = request.POST["contact_number"]
        fat = request.POST["fathers_name"]
        add = request.POST["address"]
        gen = request.POST["gender"]
        desig = request.POST["designation"]
        bloodg = request.POST["blood_group"]
        about = request.POST["about"]
        print(request.POST)
        
        usr = User.objects.create_user(un,em,pwd)
        usr.first_name = fname
        usr.last_name = last
        usr.save()
        
        
        reg = Register(user=usr, contact_number=con, fathers_name=fat, address=add, gender=gen, designation= desig, blood_group= bloodg , about=about)
        reg.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            reg = Register(profile_pic = img)
            reg.save()
  
        alert = {
        "username": request.GET.get('username', ''),
        }

        if request.method == 'POST':
            un = request.POST.get('username', '')

        if User.objects.filter(username = request.POST['username']).exists():
            alert['username'] = "Username already exists"

        return render(request,"register.html",{"status":" {} your Account created Successfully".format(fname)})
    return render(request,"register.html")
                
def edit_profile(request):
    context = {}
    data = get_object_or_404(Register, user__id=request.user.id)
    context["data"]=data        
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        con = request.POST["contact_number"]
        fat = request.POST["fathers_name"]
        add = request.POST["address"]
        gen = request.POST["gender"]
        desig = request.POST["designation"]
        bloodg = request.POST["blood_group"]
        about = request.POST["about"]
        

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.contact_number = con
        data.fathers_name = fat
        data.address = add
        data.gender = gen
        data.designation = desig
        data.blood_group = bloodg
        data.about = about
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

        context["status"] = "Changes Saved Successfully"
        # return HttpResponse("updated successfully")
     
    return render(request,'edit_profile.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")                



def check_user(request):
    if request.method=="GET":
        un = request.GET["usern"]
        check = User.objects.filter(username=un)
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")    