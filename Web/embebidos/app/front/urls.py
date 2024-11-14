from django.urls import path
from .views import ChatView

app_name = "chat"
urlpatterns_chat = [
    path('', ChatView.as_view(), name="chat")
]