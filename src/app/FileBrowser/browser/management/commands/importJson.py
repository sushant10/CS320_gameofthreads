from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.dateparse import parse_date

from browser.models import File, System

"""
Call with 2 arguments: 'app' 'tarfolder'
from the folder where manage.py is located searches for app/tarfolder and imports json files in that that folder
database must be
"""

class Command(BaseCommand):

    help = "Parses JSON - call with argument for app which contains data-export folder (for example manage.py importJson browser data-export)  "
    """
    option_list = BaseCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )
    """

    def add_arguments(self, parser):
        parser.add_argument('app', type=str, help='Indicates the app which contains the target folder')
        parser.add_argument('target_folder', type = str, help = 'Indicates the name of the folder which contains the json object')

    def handle(self, *args, **kwargs):
        app = kwargs['app']
        tarFolder = kwargs['target_folder']
        importJson(app, tarFolder)


def importJson(app, tarFolder):
    import os
    import json
    from sys import platform

    if platform == "linux" or platform == "linux2" or platform == 'darwin':
    # linux or OS X
        f_slash = '/'
    elif platform == "win32":
    # Windows...
        f_slash = r'\\'

    cwd = os.getcwd()
    #print("cwd = %s " % cwd)
    folder = cwd + f_slash
    for fold in os.listdir(cwd):
        if(fold == app):
            folder = folder + fold
    #print("folder = %s" % folder)
    for file in os.listdir(folder):
        #print(file)
        if(file == tarFolder):
            print("found data")
            folder = folder + f_slash + file

    #print ("folder then = %s " % folder)
    files = os.listdir(folder)
    for file in files:
        path = os.path.abspath(folder+ f_slash + file)
        #print(path)
        f = open(path)
        fText = f.read()
        #print(fText)
        try:
            j = json.loads(fText)
            ID = (file.split('.')[0]).replace('-','')
            datestring = "-".join(file.split('-')[1:]).split('.')[0]
            datadate = parse_date(datestring)
            systemID = file.split('-')[0]
            companyName = j['system']['companyName']
            tenants = j['authorized']['tenants']
            freePct = round(j['capacity']['total']['freePct'], 3)
            try:
                sys = System.objects.get(pk = systemID)
                if(sys):
                   if(sys.recentDate < datadate):
                       System.objects.update_or_create(serialNumberInserv = systemID, defaults = {'name': companyName, 'tenants': tenants, 'recentDate' : datadate, 'capacity' : freePct})      
                else:
                   System.objects.update_or_create(serialNumberInserv = systemID, defaults = {'name': companyName, 'tenants': tenants, 'recentDate' : datadate, 'capacity' : freePct})
                   
					
                sys = System.objects.get(pk = systemID)
                #print("created file with %s ID, %s path" % (ID, path))
            except Exception as ex:
                print(ex)
                System.objects.create(serialNumberInserv = systemID, recentDate = datadate, capacity = freePct)
                sys = System.objects.get(pk = systemID)

            fpath = "files" + f_slash + file
            File.objects.update_or_create(FileID = ID,
            defaults = { 'filePath' : fpath,'dataDate' : datadate, 'name' : file, 'SystemID' : sys, 'capacity' : freePct} )

        except Exception as e:
            print(e)

def createFile(ID, filepath, datadate, Name, systemid, freePct):
    File.objects.create(FileID = ID, filePath = filepath, dataDate = datadate, name = Name,SystemID = systemid, capacity = freePct)

def createSystem(Serial, Name, datadate, freePct):
    System.objects.create(serialNumberInserv = Serial, name = Name, recentDate = datadate, capacity = freePct)
