from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def index2(request):
    return render(request,'index-2.html')


def manu(request):
    return render(request,'manu.html')


def contact(request):
    return render(request,'contact.html')


def faq(request):
    return render(request,'faq.html')


def gallery(request):
    return render(request,'gallery.html')


def blog(request):
    return render(request,'blog-details.html')   



def blog(request):
    return render(request,'blog-standard.html') 

    
def restaurant(request):
    return render(request,'restaurant-details.html') 

    
def restaurant(request):
    return render(request,'restaurant.html') 

    
def team(request):
    return render(request,'team.html') 