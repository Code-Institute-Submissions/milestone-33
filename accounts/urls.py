
from django.urls import path, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="register"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', include(urls_reset))
]
