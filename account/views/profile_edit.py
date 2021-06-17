from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfileEditForm

@login_required(login_url='/')
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')

    else:
        form = ProfileEditForm(instance = request.user)



    return render(request, 'pages/profile-edit.html', context={
        'form':form
    })
