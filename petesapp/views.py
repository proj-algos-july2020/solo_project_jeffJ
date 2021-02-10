from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from petesapp.models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'about.html')

def classes(req):
    return render(req, 'classes.html')

def about(request):
    return render(request, 'profile.html')


# def gym(request):
#     if 'id' not in request.session:
#         return redirect('/')
#     chat = Chat()
#     context = { 
#         'current_user' : User.objects.get(id=request.session['id']),
#         'users': User.objects.exclude(id=request.session['id']),
#         'chat' : chat
#     }    
#     print(context['current_user'])

#     return render(request, 'gym.html', context)

def login(request):
    user = User.objects.filter(username=request.POST['username'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id'] = user.id 
            return redirect('/gym')
        # prints (request.session['id'])        
    return redirect('/')

def regForm(request):
    hash_pw = bcrypt.hashpw(request.POST['password_input'].encode(), bcrypt.gensalt()).decode()

    user=User.objects.create(email=request.POST['email_input'],  username=request.POST['username_input'], password=hash_pw,)

    request.session['name']=user.username
    request.session['id'] = user.id 
    return redirect('/gym')

def gym(request):

    print(request.POST)
    return render(request, 'gym.html')

def comments(request):


    Comments.objects.create(comment=request.POST['comment_input'], user_posted=User.objects.get(id=request.session['id']), user_comment=User.objects.get(id=request.POST['user_com']))

    
    return redirect('/user')

def deleteComment(request, comments_id):
    toDelete = Comments.objects.get(id=comments_id)
    toDelete.delete()
    return redirect('/user')

def logout(request):
    request.session.clear()
    return redirect('/')

