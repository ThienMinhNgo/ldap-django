from django.urls import path
from .views import ldap_login, user_logout

urlpatterns = [
    path('login/', ldap_login, name='ldap_login'),
    path('logout/', user_logout, name='logout'),
]