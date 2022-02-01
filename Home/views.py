from django.shortcuts import render,HttpResponse
#from datetime import datetime
from Home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html') 
   # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html') 
   # return HttpResponse("this is home about page")

def services(request):
    return render(request,'services.html') 
    #return HttpResponse("this is home services page")s

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address= request.POST.get('address')
        contact = Contact(name=name,email=email,contact=contact,address=address)
        contact.save()
    
        
    return render(request,'contact.html') 
    #return HttpResponse("this is home contact page")





