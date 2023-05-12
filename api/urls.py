from django.urls import path
from .views import CreateRoomView, RoomView, GetRoom, JoinRoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoomView.as_view())
]