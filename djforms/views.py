# from django.http import Http404
# from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from .forms import DjangForm
from .models import Simple

static_context = {
    'images': 'static/images/',
    'scripts': 'static/scripts/',
}

def home(request):
    context = dict(static_context)
    context['variable'] = "simple"
    q = Simple.objects.all()
    context['names'] = [x.name for x in q]
    return render(request, 'djforms/templates/index.html', context)

def djform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = DjangForm(request.POST)
        if form.is_valid():
            name = form["name"].value()
            # save in db:
            mod = Simple()
            mod.name = name
            mod.save()
            # acknowledge:
            resp = f'got it -- your name is: {name}<br/><br/><a href="/">homepage</a>'
            return HttpResponse(resp)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DjangForm()

    return render(request, 'djforms/templates/djform.html', {'form': form})