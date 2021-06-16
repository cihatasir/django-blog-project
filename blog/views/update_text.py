from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UpdateTextFormModel
from blog.models import TextModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def update_text(request, slug):
    text = get_object_or_404(TextModel, slug=slug, author=request.user)
    form = UpdateTextFormModel(request.POST or None, files=request.FILES or None, instance=text)
    
    if form.is_valid():
        form.save()
        return redirect('detail', slug=text.slug)

    return render(request, 'pages/update-text.html', context={
        'form':form
    })
