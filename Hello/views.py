from django.shortcuts import render
from django.http import HttpResponse
from  django import forms
from .forms import studentform
from .models import students
# Create your views here.
form=studentform()
my_dict={"insert_me":"Its lowest......","sr":"Star dust","n":300,'form':form}

def index(request):
    return HttpResponse("<h1> I started learning Django and its fun </h1>")

def Hello(request):
    # return HttpResponse("<h2> I am calling the applications urls.py file </h2>")
    if request.method == "POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=studentform()

    return render(request,'Hello/Home.html',context=my_dict)

def list_view(request):
    # dict for initial data with
    #field name as key
    context={}
    #add the dic during  initialization
    #it ll be in dataset- key
    context["dataset"]=students.objects.all() #it ll read all objects in student class
    return render(request,"Hello/list_view.html",context)

