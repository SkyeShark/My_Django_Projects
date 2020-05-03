from django.shortcuts import render, redirect
from .models import User, Post, Comment
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def success(request):
    try:
        request.session['userid']
        posts = {
        'posts': Post.objects.all()
        }
        return render(request, 'success.html',posts)
    except: 
        return redirect('/')

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

def post_message(request):
    Post.objects.create(message=request.POST['message'], posted_by=User.objects.get(id=request.session['userid']))
    return redirect('/success')

def post_comment(request, id):
    poster = User.objects.get(id=request.session['userid'])
    message = Post.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], posted_by=poster, post=message)
    return redirect('/success')