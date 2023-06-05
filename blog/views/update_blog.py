from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UpdateTextFormModel
from blog.models import BlogModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def update_blog(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug, author=request.user)
    form = UpdateTextFormModel(request.POST or None, files=request.FILES or None, instance=blog)
    
    if form.is_valid():
        form.save()
        return redirect('detail', slug=blog.slug)

    return render(request, 'pages/update-blog.html', context={
        'form':form
    })
