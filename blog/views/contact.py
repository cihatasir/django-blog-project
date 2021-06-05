from django.shortcuts import render


def contact(request):
    context = {
        'sayi': 5
    }

    return render(request, 'pages/contact.html', context=context)