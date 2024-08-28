from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirmpassword = request.POST.get("password2")
        if password != confirmpassword:
            messages.warning(request, "Password incorrect")
            return redirect("/signup")

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username is taken")
                return redirect("/signup")
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is taken")
                return redirect("/signup")
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup success, please login")
        return redirect("/login")
    return render(request, "signup.html")


def log_In(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("password1")

        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("/")
        else:
            messages.error(request, "invalid credentials")
            return redirect("/login")
    return render(request, "login.html")


def log_out(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect("/login")
