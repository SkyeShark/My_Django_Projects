from django.shortcuts import render
from time import strftime
    
def index(request):
    context = {
        "time": strftime("%B %d, %Y at %H:%M %p in %Z")
    }
    return render(request,'index.html', context)