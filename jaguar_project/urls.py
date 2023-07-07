from django.contrib import admin
from django.urls import path, include

from jaguar.views import home, about

urlpatterns = [
    path('', include('store.urls')),
    path('',home, name='home'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
