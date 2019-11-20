from django.urls import path

from accountapi.views import LoginView, UserCreate, GetUserDetails, Logout

urlpatterns = [
    path('auth/login', LoginView.as_view(), name="auth-login"),
    path('auth/register', UserCreate.as_view(), name="auth-register"),
    path('auth/userdetails', GetUserDetails.as_view(), name="auth-userdetails"),
    path('auth/logout', Logout.as_view(), name="auth-logout")
]
