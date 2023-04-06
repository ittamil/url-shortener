from django.urls import path
from main.views import index,redirect

urlpatterns = [
    path('', index,name="index"),
    path('redirect/<slug:slug>', redirect,name="redirect"),
]
