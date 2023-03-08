from django.shortcuts import render, redirect
from . models import Link
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        link = request.POST["link"]
        the_link = Link.objects.create(url=link)
        the_link.save()

        messages.info(request, "Your result has being submitted")
        return redirect("core:index")

    return render(request, "index.html")

def myview(request):
    urls = Link.objects.all()
    return render(request, "view.html", {"links": urls})