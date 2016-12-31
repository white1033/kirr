from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
                'form': form,
                'title': 'Kirr.co'
            }
        return render(request, 'shortener/home.html', context)


    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
                'form': form,
                'title': 'Kirr.co'
            }
        return render(request, 'shortener/home.html', context)

class KirrShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
