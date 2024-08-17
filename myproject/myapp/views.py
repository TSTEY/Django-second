from django.shortcuts import render

def index(arg):
    return render (arg,"index.html")
