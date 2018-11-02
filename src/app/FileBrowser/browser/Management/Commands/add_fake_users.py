from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.dateparse import parse_date

from browser.models import User, Company

