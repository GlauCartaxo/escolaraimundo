from escola.urls import path
from users.views import UserLoginView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('login', UserLoginView.as_view(),name='login_users'),   
    path('logout', UserLogoutView.as_view(),name='logout_users'),
    
]