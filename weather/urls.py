# from django.contrib import admin
# from django.urls import path, include
# from weather.views import home  # Import the home view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('weather/', include('weather.urls')),  # Include weather app URLs
#     path('', home, name='home'),  # Default root view
# ]
# meteo_app/urls.py
# from django.urls import path
# from weather.views import home, get_weather

# urlpatterns = [
#     path('', home, name='home'),  # Root URL maps to the home view
#     path('get-weather/', get_weather, name='get_weather'),  # The weather search page
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with the search form
    path('get_weather/', views.get_weather, name='get_weather'),  # Weather data handling
]


# urls.py (dans votre application Django)

# urls.py in your weather app

# weather/urls.py (make sure this is the correct file)
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('api/get_weather/', views.get_weather, name='get_weather'),
# ]
