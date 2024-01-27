# yourapp/management/commands/transfer_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from django.test import TestCase
import requests ,os
# Create your tests here.
from lawyers.models import Lawyer, Avocat, ProfilAvocat

attorneys_data = Lawyer.objects.all()
for attorney_data in attorneys_data:
    attorney = Avocat.objects.create(
        id=attorney_data.id,
        nom =attorney_data.name,
        email=attorney_data.email,
        adresse=attorney_data.office_location,
        numero_tlfn=attorney_data.phone
    )
    attorney.categories.set(attorney_data.categories.all())

    ProfilAvocat.objects.create(
        avocat=attorney,
        experience=attorney_data.description,
        photo = attorney_data.photo,
        working_hours = attorney_data.working_hours
    )
print('Data transfer completed successfully')
