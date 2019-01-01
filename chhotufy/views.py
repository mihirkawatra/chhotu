from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import Form
# Create your views here.
from .models import shortURL

def redirect_view(request, code=None, *args, **kwargs): #function based view FBV
     obj = get_object_or_404(shortURL, code=code)
     return HttpResponseRedirect(obj.url)

def form_view(request):
    form = Form()
    return render(request,'chhotufy/form.html',{'form':form})

def after(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            u=form.cleaned_data['url']
            # new = shortURL(u)
            # new.save()
            entry = shortURL.objects.get_or_create(url = u)[0]
    return render(request,'chhotufy/after.html')
