from django.urls import path
from . import views

urlpatterns = [
    path('home2/',  views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('events/', views.event, name="events"),
    path('logout/', views.signout, name="signout"),
    path('signin/', views.signin, name="signin"),
    path('event/create/', views.create_event, name="create_event"),
    path('event/<int:event_id>/', views.event_detail, name="detail_event"),
    path('event/<int:event_id>/complete', views.complete_event, name="complete_event")   




]
