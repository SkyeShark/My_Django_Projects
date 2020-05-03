from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        else:    
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'], passhashed=pw_hash) 
            return redirect('/success')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.passhashed.encode()):
            request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.first_name
            return redirect('/success')
        else:
            messages.error(request, "Incorrect password.")
    else:
        messages.error(request, "No account exists for this email. Please register.")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")