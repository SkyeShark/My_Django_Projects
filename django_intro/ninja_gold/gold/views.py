from django.shortcuts import render, HttpResponse, redirect
from time import strftime 
import random

def index(request):
    stuff = {
        'activity_log':" ",
        'gold_amount':0
    }
    request.session['gold_amount'] = 0
    request.session['activity_log'] = " "
    return render(request, "index.html", stuff)

def process_money(request):
    if 'farm' in request.POST:
        goldup = random.randint(10,20)
        request.session['gold_amount'] += goldup
        request.session['activity_log'] += " --- Earned " + str(goldup) + " gold from the farm! (" + strftime("%Y/%m/%d %H:%M %p") + ")"
    elif 'cave' in request.POST:
        goldup = random.randint(5,10)
        request.session['gold_amount'] += goldup
        request.session['activity_log'] += " --- Earned " + str(goldup) + " gold from the cave! (" + strftime("%Y/%m/%d %H:%M %p") + ")"
    elif 'house' in request.POST:
        goldup = random.randint(2,5)
        request.session['gold_amount'] += goldup
        request.session['activity_log'] += " --- Earned " + str(goldup) + " gold from the house! (" + strftime("%Y/%m/%d %H:%M %p") + ")"
    elif 'casino' in request.POST:
        goldup = random.randint(-50,50)
        request.session['gold_amount'] += goldup
        if goldup > 0:
            request.session['activity_log'] += " --- Earned " + str(goldup) + " gold from playing in the casino! (" + strftime("%Y/%m/%d %H:%M %p") + ")"
        elif goldup < 0:
            request.session['activity_log'] += " --- Lost " + str(goldup*-1) + " gold from playing in the casino! (" + strftime("%Y/%m/%d %H:%M %p") + ")"    
        elif goldup == 0:
            request.session['activity_log'] += " --- Did not earn or lose any gold from playing in the casino! (" + strftime("%Y/%m/%d %H:%M %p") + ")"
    return redirect(f'/index2')

def index2(request):
    newstuff = {
        'activity_log':request.session['activity_log'],
        'gold_amount':request.session['gold_amount']
    }
    return render(request, "index.html", newstuff)
