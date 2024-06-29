from django.shortcuts import render
from django.http import HttpResponse
from . forms import SignUp,Login
from . models import User

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def signup(response):
    if response.method == "POST":
        form = SignUp(response.POST)
        if form.is_valid():
            is_doctor = form.cleaned_data["is_doctor"]
            f_name = form.cleaned_data["f_name"]
            l_name = form.cleaned_data["l_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            address = form.cleaned_data["address"]

            all_users = User.objects
            if all_users.filter(username=username):
                return render(response,'main/signup.html',{"form":form,
                                "usernameExists":True,"confirmedPassword":True})

            if password!=confirm_password:
                return render(response,'main/signup.html',{"form":form,
                                "usernameExists":False,"confirmedPassword":False})
            
            new_user = User(is_doctor = is_doctor,
                            f_name = f_name,
                            l_name = l_name,
                            username = username,
                            password = password,
                            address = address)
            new_user.save()
            return render(response,'main/data_added.html',{})
    form = SignUp()
    return render(response,'main/signup.html',{"form":form,
                                "usernameExists":False,"confirmedPassword":True})






def login(response):
    if response.method == "POST":
        form = Login(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            all_users = User.objects
            if not all_users.filter(username=username):
                return render(response,'main/login.html',{"form":form,"wrongUsername":True,"wrongPassword":False})
            
            user = User.objects.get(username = username)
            if user.password != password:
                print(user.password)
                return render(response,'main/login.html',{"form":form,"wrongUsername":False,"wrongPassword":True})
            
            return render(response,'main/user_data.html',{"user":user})



    form =Login()
    return render(response, 'main/login.html',{"form":form,"wrongUsername":False,"wrongPassword":False})