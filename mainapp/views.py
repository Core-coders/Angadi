from django.shortcuts import render

# Create your views here.
def Indexview(request):
    return render(request,'account/home.html',{})

def depodashview(request):
    return render(request,'Depot/depotdashboard.html',{})

def shopdashview(request):
    return render(request,'shop/shopdashboard.html',{})


