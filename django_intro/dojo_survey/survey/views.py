from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == "POST":
        if 'three' not in request.POST:
            three = ""
        else:
            three = request.POST["three"]
        if 'four' not in request.POST:
            four = ""
        else:
            four = request.POST["four"]
        if 'five' not in request.POST:
            five = ""
        else:
            five = request.POST["five"]
        data = {
            "Name":request.POST["one"],
            "Pizza":request.POST["two"],
            "Topping1":three,
            "Topping2":four,
            "Topping3":five
        }
        return render(request, "results.html", data)