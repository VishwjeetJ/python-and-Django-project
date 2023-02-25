from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request): 
    context = {
        "variable1" : "This is 1st variable",   
        "variable2" : "This is 2nd variable"
    }
    return render(request, 'index.html', context) 
   #return HttpResponse("This is Homepage")

def about(request): 
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def category(request): 
    return render(request, 'category.html')
    # return HttpResponse("This is category page")

def contact(request): 
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

