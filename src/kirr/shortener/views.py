from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})


    def post(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})

class KirrShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
