from django.urls import path
from users import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('login',views.login,name='login'),
]
