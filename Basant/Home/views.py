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
        
        
        {'id': 1, 'title': 'Music/Singing/RapBattle/Band', 'intro': 'Show off your musical genius', 'image': 'music.jpeg'},
        {'id': 2, 'title': 'Dancing/StreetDance/DanceBattle', 'intro': 'Show off your fluidity', 'image': 'dancing.jpeg'},
        {'id': 3, 'title': 'Fashion show', 'intro': 'Show off your charisma in style', 'image': 'fashion.jpeg'},
        {'id': 4, 'title': 'Drama/Theater', 'intro': 'Enchant audiences with your acting    ', 'image': 'drama.jpg'},
        {'id': 5, 'title': 'Art exhibition', 'intro': 'Bless the canvas with your minds eye ', 'image': 'art.jpeg'},
        {'id': 6, 'title': 'Cosplay Contest', 'intro': 'Show off your best cosplay!', 'image': 'cosplay.jpeg'},
        {'id': 7, 'title': 'Hackathon', 'intro': 'Out-code your rivals', 'image': 'hack.jpeg'},
        {'id': 7, 'title': 'Gym events', 'intro': 'Become the successor to Baki!', 'image': 'gym.jpeg'},
        {'id': 8, 'title': 'Anime Quiz', 'intro': 'Test your anime knowledge!', 'image': 'anime_quiz.jpeg'},
        {'id': 9, 'title': 'Robo-War', 'intro': 'Craft machines and engage in the war of steels', 'image': 'robo.jpeg'},
        {'id': 10, 'title': 'E-sports(BGMI)', 'intro': 'Conquer the battlegrounds', 'image': 'bgmi.png'},
        {'id': 11, 'title': 'E-sports(Free-fire)', 'intro': 'Spray and pray', 'image': 'ff.jpeg'},
        {'id': 12, 'title': 'Treasure Hunt', 'intro': 'Find the lost one piece!', 'image': 'treasurehunt.jpeg'},
        {'id': 13, 'title': 'Prom nite', 'intro': 'Shower a little love', 'image': 'promnite.jpeg'},
        {'id': 14, 'title': 'Open-mic', 'intro': 'Make audiences laugh!', 'image': 'openmic.jpeg'},
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

def ourTeam_view(request):
    events = [
        
        
        {'id': 1, 'title': 'person1', 'intro': 'year 4, branch cs', 'image': 'fashion.jpeg'},
        {'id': 2, 'title': 'person2', 'intro': 'year 4, branch cs', 'image': 'fashion.jpeg'},
        {'id': 3, 'title': 'person3', 'intro': 'year 4, branch cs', 'image': 'fashion.jpeg'},
        {'id': 4, 'title': 'person4', 'intro': 'year 4, branch cs', 'image': 'fashion.jpeg'},
        # Add more events as needed
    ]
    return render(request, 'home/team.html', {'events': events})
    
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
