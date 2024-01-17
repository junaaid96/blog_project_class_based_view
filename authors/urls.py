from django.urls import path
from authors.views import registration, profile, edit_profile, password_change
from authors.views import UserLoginView, UserLogoutView

urlpatterns = [
    path('registration/', registration, name='registration'),
    # path('login/', user_login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', user_logout, name='logout'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/password_change/',
         password_change, name='password_change')
]
