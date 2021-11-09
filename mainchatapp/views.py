from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from .chatapp import chat

# Create your views here.
class ChatterBotAppView(TemplateView):
    template_name = 'landing.html'

def index(request):
  return render(request, 'index.html')

def room(request):
    if request.is_ajax and request.method == "GET":
        query = request.GET.get('query', None)
        response= chat.chat(query)
        return JsonResponse({"instance": response})
        
        





