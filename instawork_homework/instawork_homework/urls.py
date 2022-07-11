from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('member.urls')),
    path('admin/', admin.site.urls),
]
