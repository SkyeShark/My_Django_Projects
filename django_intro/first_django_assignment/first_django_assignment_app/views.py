from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return index(request)

def show(request, number):
    return HttpResponse("placeholder to display blog number " + str(number))

def edit(request, number):
    return HttpResponse("placeholder to edit blog number " + str(number))

def destroy(request, number):
    return index(request)

