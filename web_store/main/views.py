from django.shortcuts import render


def index(request):
    context = {
        'title': 'MY first site',
    }
    return render(request, 'main/index.html', context)