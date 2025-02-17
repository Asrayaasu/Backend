from django.urls import path
from .views import register_user, login_user, protected_view
urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('protected/', protected_view, name='protected_view'),
]