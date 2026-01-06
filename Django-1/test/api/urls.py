from django.urls import path
from .views import Signup, Login, home

urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view())
]