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
from weather.views import home, get_weather

urlpatterns = [
    path('', home, name='home'),  # Home page with search bar
    path('get-weather/', get_weather, name='get_weather'),  # Weather search result page
]


