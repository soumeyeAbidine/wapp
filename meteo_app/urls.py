"""
URL configuration for meteo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from weather.views import home  # Import the home view

# urlpatterns = [
#     path('admin/', admin.site.urls),          # Admin page
#     path('weather/', include('weather.urls')),  # Include URLs from the weather app
#     path('', home, name='home'),              # Default root page, show a welcome message
# ]


# # meteo_app/urls.py
# from django.urls import path
# from weather.views import get_weather

# urlpatterns = [
#     path('', get_weather, name='home'),  # Home page where the search bar is
#     path('get-weather/', get_weather, name='get_weather'),  # The view to handle the weather search
# ]


# urls.py (dans le répertoire principal de votre projet)

# wapp/urls.py (make sure this file is correctly including your app's URL configuration)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),  # Include the URLs from the weather app
]



