from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def index(request):
    return render(request, 'pages/index.html')
    

def simbolemoji(request):
    return render(request, 'pages/simbolemoji.html')


def textconvert(request):
    return render(request, 'pages/textconvert.html')
