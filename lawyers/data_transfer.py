# yourapp/management/commands/transfer_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from django.test import TestCase
import requests ,os
# Create your tests here.
from lawyers.models import Lawyer, Avocat, ProfilAvocat

print(1+1)