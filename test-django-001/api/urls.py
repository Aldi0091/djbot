from django.urls import path
from .views import Message, Register, Login, Receiver


urlpatterns = [
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
    path('message/', Message.as_view(), name='message'),
    path('receiver/', Receiver.as_view(), name='receiver'),
]