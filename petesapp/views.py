from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def classes(req):
    return render(req, 'classes.html')


def gym(request):
    if 'id' not in request.session:
        return redirect('/')
    chat = Chat()
    context = { 
        'current_user' : User.objects.get(id=request.session['id']),
        'users': User.objects.exclude(id=request.session['id']),
        'chat' : chat
    }    
    print(context['current_user'])

    return render(request, 'gym.html', context)

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email=request.POST['email_input'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password_input'].encode(), user.password.encode()):
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id 
            return redirect('/user')
        # prints (request.session['id'])        
    return redirect('/')

def regForm(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hash_pw = bcrypt.hashpw(request.POST['password_input'].encode(), bcrypt.gensalt()).decode()

    user=User.objects.create(email=request.POST['email_input'],  username=request.POST['user_name'], password=hash_pw,)

    request.session['name']=user.first_name
    request.session['id'] = user.id 
    return redirect('/user')

def chat(request):

    print(request.POST)
    return HttpResponse('yep working')

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

