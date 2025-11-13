from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import Evento
from django.contrib.auth.decorators import login_required, permission_required

def login_view(request):
    if request.method == 'GET':
        return render(request, 'app_eventos/login.html')
    else:
        usu = request.POST.get('username')
        pasw = request.POST.get('password')
        usuario = authenticate(request, username=usu, password=pasw)
        if usuario:
            login(request, usuario)
            return redirect ('eventos-list')
        else:
            return redirect('login')

@login_required
@permission_required('app_eventos.view_evento')
def eventos_view(request):
    if request.user.is_authenticated:
        eventos = Evento.objects.all()
        return render(request, 'app_eventos/eventos.html', {'eventos': eventos})
    else:
        return redirect('login')

from django.http import JsonResponse
import os
from django.core.files.storage import default_storage
from django.conf import settings


def __debug_storage__(request):
    return JsonResponse({
        "CLOUDINARY_URL_exists": bool(os.getenv("CLOUDINARY_URL")),
        "CLOUDINARY_URL_preview": (os.getenv("CLOUDINARY_URL")[:12] + "...") if os.getenv("CLOUDINARY_URL") else None,
        "DEBUG": getattr(settings, "DEBUG", None),
        "DEFAULT_FILE_STORAGE": getattr(settings, "DEFAULT_FILE_STORAGE", None),
        "default_storage_class": default_storage.__class__.__module__ + "." + default_storage.__class__.__name__,
    })