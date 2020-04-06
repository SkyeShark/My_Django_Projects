from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        if 'three' not in request.POST:
            request.session['three'] = ""
        else:
            request.session['three'] = request.POST['three']
        if 'four' not in request.POST:
            request.session['four'] = ""
        else:
            request.session['four'] = request.POST['four']
        if 'five' not in request.POST:
            request.session['five'] = ""
        else:
            request.session['five'] = request.POST['five']
        request.session['one'] = request.POST['one']
        request.session['two'] = request.POST['two']
        return redirect(f'/results')

def results(request):
    data = {
        'Name':request.session['one'],
        'Pizza':request.session['two'],
        'Topping1':request.session['three'],
        'Topping2':request.session['four'],
        'Topping3':request.session['five']
    }
    return render(request, "results.html",data)