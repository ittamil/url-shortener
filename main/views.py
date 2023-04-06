from django.shortcuts import render
from main.models import Shortener
from django.contrib import messages

def index(request):
    if request.method == "POST":
        short = Shortener.objects.create(name = request.POST['name'],url = request.POST['url'])
        messages.add_message(request, messages.INFO, str("http://127.0.0.1:8000/redirect/"+short.slug))
    return render(request,'index.html')

def redirect(request,slug):
    try:
        url = Shortener.objects.get(slug = slug)
        return render(request,'redirect.html',{"url":url.url})
    except:
        return HttpResponse("Not found")
    