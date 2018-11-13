from django.contrib.auth.models import Group, Permission, User, UserManager
from django.core.management.base import BaseCommand, CommandError
from browser.models import customUser 
from django.contrib.auth.hashers import make_password, check_password


'''
    Usage: python3 manage.py add_user [username] [password] [role]

    More Info:
    Create hashed password using django hashing, 
    to check the password use the django function check_password(password, encoded)
'''

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('role', type=str)

    def handle(self, *args, **options):
        user = options['username']
        passw = make_password(options['password'])
        r = options['role']
        if r.lower() != 'admin':
            r = 'admin'
        u = customUser.objects.create(username = user, password = passw, role=r)
