from django.urls import re_path
from django.urls import include, path
from . import views

urlpatterns = [
    re_path(r'^$', views.chatting, name='chat'),  # Home page for chat
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),  # Specific room
    path('', include('fundoo.urls')),
]
