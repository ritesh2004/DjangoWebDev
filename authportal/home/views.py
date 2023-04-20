from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import smtplib
from random import randint
import time
arr = []
# Create your views here.
def loguser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'logout.html')
    
    return render(request, 'login.html')
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
def loguserOut(request):
    logout(request)
    return render(request,'login.html')
def SignIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        OTP = str(emailAuth(email=email))
        print("Generated OTP:",OTP)
        arr.append(username)
        arr.append(password)
        arr.append(firstname)
        arr.append(lastname)
        arr.append(email)
        arr.append(OTP)
        return redirect("/verify")
    return render(request,'signin.html')

def emailAuth(email):
    ### GENERATING OTP
    OTP = ""
    for i in range(6):
        OTP += str(randint(0,9))
    ### SETTING UP THE SERVER
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    ### LOG IN TO THE GMAIL ACCOUNT
    server.login('anonymousmsgofficial@gmail.com', 'wjmpsgafevekmqfr')
    ### CREATIN THE MAIL BODY
    sub = 'Verify Your Email Address'
    body = "Your OTP is " + OTP
    message = f"Subject: {sub}\n\n {body}"
    ### SENDING THE MAIL
    server.sendmail('anonymousmsgofficial@gmail.com',
                    email,
                    message)
    server.quit()
    return OTP

def verify(request):
    if request.method == "POST":
        username = arr[0]
        password = arr[1]
        firstname = arr[2]
        lastname = arr[3]
        email = arr[4]
        OTP = arr[5]
        otp = request.POST.get("otp")
        print("Data received from verify page:",otp)
        print("OTP generated:",OTP)
        time.sleep(1)
        if otp == OTP:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            USER = authenticate(request, username=username, password=password)
            if USER is not None:
                login(request, USER)
                return redirect('/')
        return redirect("/")
    return render(request, 'verify.html')
