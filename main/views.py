from django.shortcuts import render

def firstPage(request):
    data = {
        'title': 'Тренажерный зал "ЮГ"'
    }
    return render(request, 'base.html', data)

