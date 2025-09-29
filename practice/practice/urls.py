"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from starter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='hello/', view=views.hello_view, name='hello'),
    path(route='users/', view=views.users_view, name='users'),
    path(route='city-time/', view=views.city_time_view, name='city-time'),
    path(route='city-time/<str:city_name>/', view=views.city_time_view, name='city-time-with-param'),
    path(route='cnt/', view=views.counter_view, name='counter'),
]
