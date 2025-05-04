from django.shortcuts import render
from django.http import Http404,HttpResponse
# Create your views here.

def index(request):
    return render(request, "spa/index.html")

texts = [
    "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
    "A repudiandae blanditiis corporis dolor fugit odit culpa libero repellat nulla! Reiciendis veritatis non,",
    "dicta sequi impedit magni dolorum inventore tempore aliquid!"
]

def sections(request, num):
    if 1 <= num <= len(texts):
        return HttpResponse(texts[num-1])
    else :
        return Http404("No Such Section Exists")

def Scroll(request):
    return render(request,"spa/scroll.html",{
        'numbers' : range(50)
    })