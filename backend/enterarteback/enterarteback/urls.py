"""
URL configuration for enterarteback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from enterarteapp.views import list_event, create_event, update_event, delete_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('../template/list_event/', list_event, name='list_events'),
    path('../template/create_event/', create_event, name='create_event'),
    path('../template/update_event/<int:pk>/', update_event, name='update_event'),
    path('../template/delete_event/<int:pk>/', delete_event, name='delete_event'),
]