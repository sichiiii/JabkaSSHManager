from django.urls import path, re_path
from . import views

urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('connect', views.connect_ssh, name='connect_ssh'),
]
