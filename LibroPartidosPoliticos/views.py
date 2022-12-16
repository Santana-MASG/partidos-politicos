from django.shortcuts import render


def home(request):
    context = {
        'partidos':[
            'PRI',
            'Morena',
            'PAN',
            'Parido Verde',
            'Movimiento Ciudadano'
        ],
    }
    return render(request, 'index.html', context)