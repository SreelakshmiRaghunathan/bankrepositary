from django.http import HttpResponse
from django.shortcuts import render
from . models import Team,Blog,Gallery
# Create your views here.
def demo(request):
    obj1=Team.objects.all()
    obj2 = Gallery.objects.all()
    obj3 = Blog.objects.all()

    return render(request,"index.html",{'teams':obj1,'post':obj2,'blogs':obj3})

# def gallery(request):
#     obj2=Gallery.objects.all()
#     return render(request,"index.html",{'post':obj2})
#
# def blog(request):
#     obj3=Blog.objects.all()
#     return render(request,"index.html",{'blogs':obj3})