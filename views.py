from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from app.models import register,Contact
import random
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import ContactForm


def ev1(request):
    return render(request,"eve1.html")

def log(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"eve1.html")

def reg(request):
    return render(request,"register.html")

def mia(request):
    return render(request,"main.html")

def cont(request):
    return render(request,"contact.html")

def abo(request):
    return render(request,"about.html")

def use(request):
    return render(request,"user.html")

def adm(request):
    return render(request,"admin.html")

def forg(request):
    return render(request,"forget.html")

def rest(request):
    return render(request,"forget.html")

def modi(request):
    h = request.GET.get('del', '')
    print(h)
    username = request.GET.get('fullname', '')
    email1 = request.GET.get('email', '')
    password = request.GET.get('password', '')
    phone=request.GET.get('phone', '')
    desig = request.GET.get('desig', '')

    # Get the instance to update or delete
    r = register.objects.filter(Email=email1).first()

    if h == "update":
        if r:
           r.Username = username
           r.Email = email1 # Ensure this field name matches your model
           r.password = password
           r.Phone=phone
           r.desig = desig  # Ensure this field name matches your model
           r.save()
    elif h == "delete":
        if r:
          r.delete()


    users = register.objects.all()
    return render(request, "views.html", {"users": users})

def vus(request):
    users = register.objects.all()
    return render(request,"views.html",{"users":users})

def con(request):
    users = register.objects.all()
    return render(request,"viewcon.html",{"users":users})


def doreg(request):
    print("calindee...")
    Username = request.GET['username']
    Email  = request.GET['email']
    Password = request.GET['password']
    Phone = request.GET['phone']
    r = register()
    r.Username=Username
    r.Email=Email
    r.password=Password
    r.Phone=Phone
    r.save()

    if request.method == 'GET':
       email = request.GET['email']
       send_mail(
        'Registration Successful',
        'Congratulations! Your registration has been successfully completed. You can login now by clicking below link:-http://127.0.0.1:8000/login',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
       
    return render(request,"login.html",{"msg":"success"})



def logincheck(request):
    email1=request.GET['email']
    password1=request.GET['password']
    r=None
    try:   
     r=register.objects.get(Email=email1,password=password1)
    except Exception as ex:
        return render(request,"login.html",{"msg":"Invalid Email/Password"})
    if(r!=None):
        if(r.desig == 'user'):
            return redirect("/userhome")
        if(r.desig == 'admin'):
            return redirect("/adminhome")
        else:
            return render(request,"login.html", {'msg': "Invalid designation"})
    return render(request,"success.html")


def con(request):
    username = request.GET['name']
    phonenumber =request.GET['lastname']
    email = request.GET['email']
    comment = request.GET['comment']
    message = request.GET['message']
    r1=Contact()
    r1.Username=username
    r1.phonenumber=phonenumber
    r1.Email=email
    r1.subject=comment
    r1.message=message
    r1.save()
    return render(request,"contact.html",{"msg":"successfully submitted .we will contact u soon......"})



def generate_otp():
    return random.randint(100000, 999999)

def getotp(request):
     if request.method == 'GET':
            email = request.GET['email']
            otp = generate_otp()
            request.session['otp'] = otp
 # Send OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'verify.html')     
        
    
    

def verifyotp(request):
    if request.method == 'GET':
        entered_otp = int(request.GET['otp'])
        stored_otp = request.session.get('otp')

        if entered_otp == stored_otp:
            # OTP is correct
            return render(request, "userpassword.html")
        else:
            # OTP is incorrect
            return render(request, 'forget.html', {'error': 'Invalid OTP'})

    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        phone = request.POST['phone']

        if password != confirmPassword:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        # Code to save the user details (this might depend on your user model)
        # Assuming you have User model or custom user model
        # Example:
        # user = User.objects.create_user(username=username, email=email, password=password, phone=phone)
        # user.save()

        # Send a confirmation email
        send_mail(
            'Welcome to HappyEvents!',
            f'Dear {username},\n\nYou are successfully registered for HappyEvents.\n\nYou can go to the website again and login.\n\nBest regards,\nHappyEvents Team',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "You have been successfully registered! Please check your email for confirmation.")
        return redirect('login')  # Redirect to login page after registration

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage or another view
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')  # Ensure you have a template 'login.html'




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
            return redirect('contact')  # Redirect after successful submission
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



       