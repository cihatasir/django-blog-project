from django.shortcuts import render, redirect
from blog.forms import AddTextModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add_text(request):
    form = AddTextModelForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        text = form.save(commit=False)
        text.author = request.user
        text.save()
        form.save_m2m()
        return redirect('/', slug=text.slug)
    return render(request, 'pages/add-text.html', context={
        'form': form
    })



