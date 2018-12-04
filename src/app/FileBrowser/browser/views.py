from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from .models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
import json
from django.utils.encoding import smart_str
import os
from sys import platform

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
    if not request.session.has_key('username'):
        return redirect("browser:login")
    username = str(request.session['username'])
    system_list = System.objects.filter(tenants__contains = [username]).order_by('serialNumberInserv')[:100]
    counts = []
    for system in system_list:
        counts.append(File.objects.filter(SystemID = system.serialNumberInserv).count())
    system_count_list = zip(system_list, counts)
    return render(request, 'browser/systems_page.html', {'system_list' : system_count_list})


def files(request, serialNumberInserv):
    if not request.session.has_key('username'):
        return redirect("browser:login")
    files = get_list_or_404(File, SystemID = serialNumberInserv)
    system = get_object_or_404(System, serialNumberInserv=serialNumberInserv)
    return render(request, 'browser/files_page.html', {'file_list':files, 'companyID':serialNumberInserv, 
        'companyName':system.name})

def download(request, fileID):
    if not request.session.has_key('username'):
        return redirect("browser:login")
    file = get_object_or_404(File, FileID=fileID)
    if platform == "linux" or platform == "linux2" or platform == 'darwin':
    # linux or OS X
        f_path = 'browser/static/'
    elif platform == "win32":
    # Windows...
        f_path = r'browser\\'
    systemID = file.SystemID
    system = get_object_or_404(System, serialNumberInserv=systemID)
    tenants = system.tenants
    username = str(request.session['username'])
    if username in tenants:
        with open(f_path+file.filePath) as f:
            data = json.load(f)
        response = HttpResponse(json.dumps(data, indent=4), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file.name)
        return response
    else:
        return redirect("browser:login")

def help(request):
    if not request.session.has_key('username'):
        return redirect("browser:login")
    return render(request, 'browser/help.html', {})

def loginView(request):
    errors = []
    try:
      del request.session['username']
    except:
      pass
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            usr = login_form.cleaned_data['username']
            pswd = login_form.cleaned_data['password']
            try:
                u = customUser.objects.get(username=usr)
                if check_password(pswd, u.password):
                    request.session['username'] = usr
                    return redirect("browser:systems")
                else:
                    errors = ['invalid username or password']
            except ObjectDoesNotExist:
                errors = ['invalid username or password']
        else:
            errors = ['invalid username or password']

    return render(request, 'browser/login.html', {'error' : errors})

def logoutView(request):
    try:
      del request.session['username']
    except:
      pass
    return redirect("browser:login")
