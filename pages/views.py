from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')
    

def simbolemoji(request):
    return render(request, 'pages/simbolemoji.html')


def textconvert(request):
    return render(request, 'pages/textconvert.html')
