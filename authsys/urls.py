from django.urls import path
from .views import *

urlpatterns = [
    path('/create', SignUpView.as_view(), name='create_account'),
    path('logout', log, name='logout'),
    path('/login', SignInView.as_view(), name='login'),

]
