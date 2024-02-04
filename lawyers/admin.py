from django.contrib import admin
from .models import *   # Import your models

# Register your models to appear in the admin interface
admin.site.register(Client)
admin.site.register(Avocat)
# Register your models here.
