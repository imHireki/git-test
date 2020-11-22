from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')
    

def textemoji(request):
    return render(request, 'pages/textemoji.html')
