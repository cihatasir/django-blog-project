from django.shortcuts import render


def contact(request):
    return render(request, 'pages/contact.html', context={})