from django.shortcuts import render


def base(request):
    
    context = {
        'name': 'Cihat Asir'
    }    

    return render(request, 'pages/anasayfa.html', context=context)