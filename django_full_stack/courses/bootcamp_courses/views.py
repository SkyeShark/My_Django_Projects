from django.shortcuts import render, redirect
from .models import Course,Description
from django.contrib import messages
import datetime

def index(request):
    data = {
        "courses": Course.objects.all(),
    }
    return render(request, 'index.html',data)

def new(request):
    if request.method == "POST":
        errors = Course.objects.course_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            nam = request.POST['name']
            descinput = request.POST['description']
            if Description.objects.filter(text=descinput).exists():
                descinput = Description.objects.get(name=descinput)
            else:
                Description.objects.create(text=descinput)
                descinput = Description.objects.get(text=descinput)
            Course.objects.create(name=nam,description=descinput)
            return redirect('/')

def delete(request, course_id):
    data = {
        "courses": Course.objects.filter(description_id=course_id),
    }
    return render(request, 'delete.html',data)    

def destroy(request, course_id):
    deleteme = Course.objects.get(description_id=course_id)
    deleteme.delete()
    return redirect('/')