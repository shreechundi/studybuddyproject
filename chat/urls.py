from django.urls import path, re_path
from . import views
app_name = 'chat'

urlpatterns = [
    path('chat/', views.home, name= 'home1'),
    path('<str:room>/', views.room, name = "room"),
    re_path('checkview', views.checkview, name= 'checkview'),
    path('send',views.send,name ='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

#Source for the code in chat (used on all files)
#https://www.youtube.com/watch?v=IpAk1Eu52GU
#https://www.youtube.com/watch?v=ynyk1z8NLr8&t=920s
#author: Tomi Tokko
#Date published: April 19, 2021