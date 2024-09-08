from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='WebHome'), #index page
    path('about/', views.about, name='AboutPage'),
    path('events/', views.events_view, name='events'),
    path('event/<int:event_id>/', views.event_detail_view, name='event_detail'),
    path('tickets/<int:event_id>/', views.buy_tickets_view, name='buy_tickets'),
    path('auth/', views.sliding_auth_view, name='auth_home'),  # Renders the sliding auth page
    path('signup/', views.signup_view, name='signup'),    # Handles sign-up
    path('login/', views.login_view, name='login'),       # Handles login
    path('logout/', views.logout_view, name='logout'),    # Handles logout
]