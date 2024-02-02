from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, "calculator/index.html")

def add(response):
    val1 = response.POST['num1']
    val2 = response.POST['num2']
    res = int(val1) + int(val2)
    return render(response, "calculator/add.html", {'result': res})