from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")


def password(request):
    characters = list("abcdefghigklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special'):
        characters.extend("!@#$%^&*()")
    if request.GET.get('numbers'):
        characters.extend("0123456789")

    length = int(request.GET.get("length", 12))
    the_password = ""
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, "generator/password.html", {"password": the_password})


def info(request):
    return render(request, "generator/info.html")
