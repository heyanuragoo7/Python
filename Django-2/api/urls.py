from django.urls import path, include
from .views import LoginView, SignupView, BlogView, DefaultView

urlpatterns = [
    path('', DefaultView.as_view(), name='default'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('blog/', BlogView.as_view(), name='create-blog')
]