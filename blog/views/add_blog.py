from django.shortcuts import render, redirect
from blog.forms import AddBlogModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add_blog(request):
    form = AddBlogModelForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        form.save_m2m()
        return redirect('/', slug=blog.slug)
    return render(request, 'pages/add-blog.html', context={
        'form': form
    })



