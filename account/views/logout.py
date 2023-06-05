from django.contrib.auth import logout
from django.shortcuts import redirect

def _logout(request):
    logout(request)
    return redirect('main')


