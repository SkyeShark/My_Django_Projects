from django.shortcuts import render, redirect
from .models import User, book, Like
from django.contrib import messages
import bcrypt
import re

def index(request):
    if 'userid' in request.session:
        return redirect('/books')
    else:    
        return render(request, 'index.html')

def books(request):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        allbooks = {
            "books": book.objects.all(),
            "likes": Like.objects.all()
        }
    return render(request, 'books.html',allbooks)

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            try:
                del request.session['success']
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            except:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        else:
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            mail = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=firstname,last_name=lastname,email=mail,password=pw_hash)
            request.session['success'] = True
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.first_name
            request.session['userlastname'] = logged_user.last_name
            request.session['useremail'] = logged_user.email
            if 'success' in request.session:
                del request.session['success']
            return redirect('/books')
        else:
            messages.error(request, "Incorrect password.")
    else:
        messages.error(request, "No account exists for this email. Please register.")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")

def edit(request, user_id):
    if request.session['userid'] != user_id:
        return redirect('/')
    else:
        return render(request, 'myaccount.html')

def update(request, user_id):
    if request.method == "POST":
        if request.session['userid'] != user_id:
            return redirect('/')
        else:
            if len(request.POST['first_name']) < 1:
                messages.error(request, "All fields must be filled.")
                return redirect('/myaccount/' + str(user_id))
            if len(request.POST['last_name']) < 1:
                messages.error(request, "All fields must be filled.")
                return redirect('/myaccount/' + str(user_id))
            if len(request.POST['email']) < 1:
                messages.error(request, "All fields must be filled.")
                return redirect('/myaccount/' + str(user_id))
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(request.POST['email']):            
                 messages.error(request, "Invalid email address!")
                 return redirect('/myaccount/' + str(user_id))
            if request.POST['email'] != request.session['useremail']:
                email = User.objects.filter(email=request.POST['email'])
                if email:
                    messages.error(request, "This email is already taken by another user!")
                    return redirect('/myaccount/' + str(user_id))
                else:
                    userupdater = User.objects.get(id=user_id)
                    userupdater.first_name = request.POST['first_name']
                    userupdater.last_name = request.POST['last_name']
                    userupdater.email = request.POST['email']
                    request.session['username'] = request.POST['first_name']
                    request.session['userlastname'] = request.POST['last_name']
                    request.session['useremail'] = request.POST['email']
                    userupdater.save()
                    return redirect('/books')
            else:
                userupdater = User.objects.get(id=user_id)
                userupdater.first_name = request.POST['first_name']
                userupdater.last_name = request.POST['last_name']
                userupdater.email = request.POST['email']
                request.session['username'] = request.POST['first_name']
                request.session['userlastname'] = request.POST['last_name']
                request.session['useremail'] = request.POST['email']
                userupdater.save()
                return redirect('/books')
    else:            
        return redirect("/")

def postbook(request):
    if request.method == "POST":
        errors = book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
        else:
            book.objects.create(title=request.POST['title'],desc=request.POST['desc'],posted_by=User.objects.get(id=request.session['userid']))
            user_liking = User.objects.get(id=request.session['userid'])
            book_liking = book.objects.get(title=request.POST['title'])
            Like.objects.create(liked_by=user_liking,book_liked=book_liking)
        return redirect('/books')

def liking(request, book_id):
    if request.method == "POST":
        user_liking = User.objects.get(id=request.session['userid'])
        book_liking = book.objects.get(id=book_id)
        if Like.objects.filter(liked_by=user_liking,book_liked=book_liking).count() < 1:
            Like.objects.create(liked_by=user_liking,book_liked=book_liking)
            return redirect('/books')
        else:
            return redirect('/books')

def unlike(request, book_id):
    if request.method == "POST":
        user_liking = User.objects.get(id=request.session['userid'])
        book_liking = book.objects.get(id=book_id)
        if Like.objects.filter(liked_by=user_liking,book_liked=book_liking).count() == 1:
            like_delete = Like.objects.get(liked_by=user_liking,book_liked=book_liking)
            like_delete.delete()
            return redirect('/books')
        else:
            return redirect('/books')

def bookpage(request, book_id):
    data = {
            "books": book.objects.filter(id=book_id)
        }
    return render(request, 'bookpage.html', data)

def delete(request,book_id,user_id):
    if request.session['userid'] == user_id:
        deleteme = book.objects.get(id=book_id)
        deleteme.delete()
        return redirect('/books')
    else:
        return redirect('/books')

def update(request, book_id):
    updater = book.objects.get(id=book_id)
    updater.desc = request.POST['desc']
    updater.title = request.POST['title']
    updater.save()
    return redirect('/book/' + str(book_id))