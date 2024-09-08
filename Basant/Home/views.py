from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html') #index page

def about(request):
    return render(request, 'home/about.html')

def events_view(request):
    events = [
        {'id': 1, 'title': 'Anime Quiz', 'intro': 'Test your anime knowledge!', 'image': 'anime_quiz.jpeg'},
        {'id': 2, 'title': 'Cosplay Contest', 'intro': 'Show off your best cosplay!', 'image': 'cosplay.jpeg'},
        # Add more events as needed
    ]
    return render(request, 'home/events.html', {'events': events})

def event_detail_view(request, event_id):
    # Your logic for handling the event details goes here
    return render(request, 'event_detail.html', {'event_id': event_id})

def buy_tickets_view(request, event_id):
    # Your logic for handling the ticket purchase goes here
    return render(request, 'buy_tickets.html', {'event_id': event_id})

def sliding_auth_view(request):
    return render(request, 'home/sliding_auth.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/sliding_auth.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a homepage or another view
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/sliding_auth.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
