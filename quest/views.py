from django.shortcuts import render


def index(request):
    return render(request, 'quest/index_examle.html')
