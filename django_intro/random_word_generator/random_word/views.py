from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    stuff = {
        'random_word':get_random_string(length=14),
        'attempt_num':1
    }
    request.session['attempt_num'] = 1
    return render(request, "index.html", stuff)

def generate(request):
    request.session['random_word'] = get_random_string(length=14)
    request.session['attempt_num'] += 1
    return redirect(f'/index2')

def index2(request):
    newstuff = {
        'random_word':request.session['random_word'],
        'attempt_num':request.session['attempt_num']
    }
    return render(request, "index.html", newstuff)