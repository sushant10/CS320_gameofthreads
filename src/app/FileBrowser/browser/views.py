from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import File, System


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

class SystemView(generic.ListView):
    template_name = 'browser/systems_page.html'
    context_object_name = 'system_list'

    def get_queryset(self):
        return System.objects.all().order_by('-serialNumberInserv')[:100]

def systems(request):
    system_list = System.objects.all().order_by('serialNumberInserv')[:100]
    counts = []
    for system in system_list:
        counts.append(File.objects.filter(SystemID = system.serialNumberInserv).count())
    system_count_list = zip(system_list, counts)
    return render(request, 'browser/systems_page.html', {'system_list' : system_count_list})

def files(request, serialNumberInserv):
    files = get_list_or_404(File, SystemID = serialNumberInserv)
    system = get_object_or_404(System, serialNumberInserv=serialNumberInserv)
    return render(request, 'browser/files_page.html', {'file_list':files, 'companyID':serialNumberInserv, 
        'companyName':system.name})


def help(request):
    return render(request, 'browser/help.html', {})

def login(request):
    return render(request, 'browser/login.html', {})
