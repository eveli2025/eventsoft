from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
from . import views
from .views import __debug_storage__

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('login/', views.login_view, name='login'),
    path('eventos/', views.eventos_view, name='eventos-list'),

]
urlpatterns += [
    path("__debug_storage__/", __debug_storage__),
]