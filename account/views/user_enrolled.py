from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import EnrolledForm
from django.contrib.auth import login, authenticate

def user_enrolled(request):
    if request.method == 'POST':
        form = EnrolledForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = EnrolledForm()

    return render(request, 'pages/enrolled.html', context={
        'form':form
    })
