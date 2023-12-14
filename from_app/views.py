from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView

from .form import *
from .models import *


def home(request):
    server = Services.objects.all()
    team = Team.objects.all()
    category=Category.objects.all()
    product=Product.objects.all()

    if request.method == "POST":
        model = Contact()
        model.name = request.POST.get('name', None)
        model.email = request.POST.get('email', None)
        model.number = request.POST.get('number', None)
        model.subject = request.POST.get('message', None)

        model.save()


    ctx={
        "server": server,
        "category": category,
        "product": product,
        "team":team,

    }

    return render(request, 'index.html', ctx)


# class BlogServerView(ListView):
#     model = Services
#     template_name = "index.html"


