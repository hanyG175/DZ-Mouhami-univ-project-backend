"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from django.conf import settings
from django.conf.urls.static import static
from lawyers.views import *

urlpatterns = [
    path('', index, name='index'),

    path('admin/', admin.site.urls),
    re_path(r'^api/' , include('lawyers.urls')),
    path("api/", include("authentication.urls")),
    path('trusted_lawyers/',Trusted_lawyers),
    path('profil_avocat_filtered/',ProfilAvocatListView.as_view()),
    path('signup/', signup),
    path('login/', user_login),
    path('logout/', user_logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
