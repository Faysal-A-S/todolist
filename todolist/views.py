from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models  import  Todo
# Create your views here.
def register(request):
    if request.method =='POST':
        username = request.POST['signupuser']
        password = request.POST['signuppass']
        cpassword =request.POST['confirmsignuppass']
        print(username,password)
        if  password == cpassword:
            try:
                user = User.objects.get(username=username)
                return  render(request,'todolist/reg.html',{'error':'Username already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                auth.login(request,user)
                return redirect('home')

        else:
            return  render(request,'todolist/reg.html',{'rerror':'Password doesn\'t match'})
    elif request.method =='GET':
        return  render(request,'todolist/reg.html')


        
    
def loginview(request):
    
    if request.method =='POST':
        username3 = request.POST['signinuser']
        password2 = request.POST['signinpass']
        
        user = auth.authenticate(username=username3,password=password2)
        if user is None:
            return  render(request,'todolist/reg.html',{'lerror':'Incorrect username or password'})

        else:
            auth.login(request,user)
            return redirect('home')
                 
    elif request.method =='GET':
        return  render(request,'todolist/reg.html')   






def logoutview(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method =='GET':
        tasks = Todo.objects.filter(user =request.user)
        

        context ={
            'todos' : tasks
        }
        return render(request,'todolist/home.html',context)  
    else:
        form = Todo()
        form.task=request.POST.get('todo')
        form.user =request.user
        form.save()
        return redirect('home')
        
              


def deleteview(request,id):
    dtask  =get_object_or_404(Todo,pk=id,user=request.user)
    dtask.delete()
    return redirect('home')
       