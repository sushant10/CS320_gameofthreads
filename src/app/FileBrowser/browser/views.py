from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import File


# Create your views here.
"""
def index(request):
    return HttpResponse("Welcome to HPE File Browser 0.0.1")
"""
class IndexView(generic.ListView):
    template_name = 'browser/files_page.html'
    context_object_name = 'file_list'

    def get_queryset(self):
        return File.objects.all().order_by('-SystemID')[:100]

def systems(request):
    return HttpResponse("Welcome to the HPE File Browser Systems page ")
