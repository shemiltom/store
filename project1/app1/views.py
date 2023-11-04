

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponse, Http404
from .models import Department
from django.shortcuts import get_object_or_404, redirect
from .forms import FormDataForm
from django.urls import reverse
from django.contrib.auth.models import User

def home(request):
    # Implement login logic here
    return render(request, 'home.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        password= request.POST['password']
        cpassword= request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('app1:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('app1:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
                return redirect(reverse('app1:login'))
                

        else:
            messages.info(request,"Password not matching")
            return redirect('app1:register')
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app1:afterl')
            #return render('/')
        else:
            #messages.info(request,"Invalid Credentials")
            return redirect('app1:login')
    return render(request,"login.html")


def afterl(request):
    # Implement login logic here
    return render(request, 'afterl.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def afterl(request):
    # Implement login logic here
    return render(request, 'afterl.html')

#def npage(request):
    # Implement login logic here
    #return render(request, 'npage.html')

def npage(request):
    
    
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('app1:success_page')
            messages.info(request,"Form submitted")
            return render(request, 'npage.html')
    else:
        form = FormDataForm()

    return render(request, 'npage.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')

def test1(request):
    departments = Department.objects.all()
    department_links = [(department.name, department.wikipedia_link) for department in departments]
    return render(request, 'test1.html', {'department_links': department_links})

def dtest1(request):
    departments = Department.objects.all()
    department_links = [(department.name, department.wikipedia_link) for department in departments]
    return render(request, 'test1.html', {'department_links': department_links})

def dtest1(request):
    departments = Department.objects.all()
    department_links = [(department.name, department.wikipedia_link) for department in departments]
    return render(request, 'test1.html', {'department_links': department_links})

def t10(request):
    departments = Department.objects.all()
    department_links = [(department.name, department.wikipedia_link) for department in departments]
    # Implement login logic here
    return render(request, 't10.html',{'department_links': department_links})
