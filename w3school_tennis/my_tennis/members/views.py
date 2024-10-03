from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Member

# Create your views here.

def index(request):
    myMembers = Member.objects.all().values()
    context = {
        "myMembers": myMembers,
    }
    return render(request, "index.html", context)

def details(request, id):
    myMember = Member.objects.get(id=id)
    context = {
        "myMember": myMember,
    }
    return render(request, "details.html", context)

def home(request):
    return render(request, 'home.html')

def testing(request):
    myData = Member.objects.all().order_by('-lastname', '-id').values()
    context = {
        "myMembers": myData
    }
    return render(request, 'template.html', context)