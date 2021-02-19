from django.shortcuts import render, redirect

# Create your views here.
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreationUserForm, DocumentForm

from django.contrib.auth import authenticate, login, logout

from .models import Forminfo 

 
def home(request):
 return render(request,"demo1.html")


def register(request):
  form = CreationUserForm()
  if request.method == "POST":
    form = CreationUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request,'account was created for',user)
      return redirect('login')
  context = {'form':form}
  return render(request,"register.html",context)

def login1(request):
 return render(request,"login1.html")

msg = ''
def loginpage(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    context1 = {'username':username}
    if user is not None:
      login(request, user)
      return render(request,'activenewweb.html',{'username': username})
    else:
      messages.info(request,"Username or Password is incorrect")
  context = {}
  return render(request, 'loginform.html',context)

def logoutuser(request):
  logout(request)
  return redirect('newweb')

def activenewweb(request):
  return render(request,'activenewweb.html')

def form_info(request):
  if request.method == "POST":
    name1 = request.POST["name"]
    email1 = request.POST["email"]
    phoneno1 = request.POST["Telephone"]
    subjectname1 = request.POST["subjectname"]
    description1 = request.POST["description"]


    forminformation = Forminfo(name=name1, email=email1, telephone=phoneno1, subjectname=subjectname1, description=description1)
    forminformation.save()
    print("data save succesfully")
  return render(request,"newweb.html")
  
def newweb(request):
  return render(request,"newweb.html")

def newwebnavbar(request):
  return render(request,"newwebnavbar.html")

def about(request):
  return render(request,"about.html")