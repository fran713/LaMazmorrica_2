from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import EventForm
from .models import Eventos
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        print("enviando formulario")
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks2')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exist'

                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                "error": 'Passwords do not match'

            })

    return render(request, 'signup.html', {
        'form': UserCreationForm

    })

@login_required
def event(request):
    #events=Eventos.objects.all()
    events =Eventos.objects.filter(user=request.user, datecompleted__isnull=True)
    
    return render (request, 'events/event.html',{'events': events})

@login_required
def signout(request):
    logout(request)
    return redirect(home)

def signin(request):
    if request.method== 'GET':
        return render (request, 'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render (request, 'signin.html',{
            'form':AuthenticationForm,
            'error': 'username or password is incorrect'
            })
        else:
            login (request, user)
            return redirect('events')
        return render (request, 'signin.html',{
            'form':AuthenticationForm
        })
        
@login_required
def create_event(request):
    print(request.method)
    if request.method == 'GET':
        
        return render(request, 'events/create_event.html',{
            'form': EventForm
    })
    else:
        try:
            form=EventForm(request.POST)
            new_event=form.save(commit=False)
            new_event.user=request.user
            print(new_event)
            new_event.save()
            return redirect('events')
        except:
            return render(request, 'events/create_event.html',{
                'form': EventForm,
                'error': 'Please provide valide data'
        })
            
@login_required            
def event_detail(request,event_id):
    if request.method =='GET':
        
        event=get_object_or_404(Eventos,pk=event_id)
        form=EventForm(instance=event)
        
        return render (request, 'events/detail.html', {'event' : event, 'form':form})
    else:
        try:
            event=get_object_or_404(Eventos, pk=event_id)
            form=EventForm(request.POST,instance=event)
            form.save()
            return redirect('events')
        except ValueError:
            return render (request, 'events/detail.html', {'event' : event, 'form':form, 'error': 'error updating task'})
        
@login_required        
def complete_event(request,event_id):
    event=get_object_or_404(Eventos, pk=event_id, user=request.user)
    if request.method=='POST':
        event.datecompleted = timezone.now()
        event.save()
        return redirect('events')