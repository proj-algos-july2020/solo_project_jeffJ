from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def user(request):
    if 'id' not in request.session:
        return redirect('/')
    context = { 
        'current_user' : User.objects.get(id=request.session['id']),
        'users': User.objects.all()

        
    }
    print(context['current_user'])

    return render(request, 'user.html', context)

def login(request):
    user = User.objects.filter(email=request.POST['email_input'])
    if user:
        user_logged = user[0]
        if bcrypt.checkpw(request.POST['password_input'].encode(), user_logged.password.encode()):
            request.session['id'] = user_logged.id 
            return redirect('/user')
        # prints (request.session['id'])        
    return redirect('/')


def reg(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')

    hash_pw = bcrypt.hashpw(request.POST['password_input'].encode(), bcrypt.gensalt()).decode()

    new_user=User.objects.create(first_name=request.POST['fname_input'], last_name=request.POST['lname_input'], email=request.POST['email_input'], password=hash_pw, workout_goals=request.POST['workout_input'])

    request.session['id'] = new_user.id 
    return redirect('/user')

# def comments(request):
#     comment=Comments.objects.create(comment=request.POST['comment_input'], user_comment=User.objects.get(id=request.session['id']))

#     print(comment)
#     return redirect('/user')

def logout(request):
    request.session.clear()
    return redirect('/')

