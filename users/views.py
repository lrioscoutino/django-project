from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    for i  in range(5):
        print(i)
    print(i)

    return HttpResponse("<h1>Hello, world.</h1>")

def inicio(request):
    context = {
        "name": "Mario Garcia",
        "message": "Hello, world.",
        "age": 45,
        "example_list": [23, 5, 6, 7, 8, 9]
    }
    return render(request, "base.html", context=context)