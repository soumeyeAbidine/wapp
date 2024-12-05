from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

# def get_weather(request, city):
#     api_key = settings.WEATHER_API_KEY
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return JsonResponse(data, safe=False)
#     else:
#         return JsonResponse({"error": "City not found"}, status=404)




# import requests
# from django.http import JsonResponse

# API_KEY = '542c342af0d0d5f128a41ea863ae0e1c'  # Replace with your actual API key
# API_URL = 'https://api.openweathermap.org/data/2.5/weather'

# def get_weather(request, city):
#     # Construct the API request URL
#     url = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"
    
#     # Send the request to the weather API
#     response = requests.get(url)
    
#     # Check if the response is successful
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = {
#             'city': data['name'],
#             'temperature': data['main']['temp'],
#             'description': data['weather'][0]['description'],
#             'humidity': data['main']['humidity'],
#             'wind_speed': data['wind']['speed'],
#         }
#         return JsonResponse(weather_data)
#     else:
#         return JsonResponse({'error': 'City not found or API error'}, status=404)


# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Weather App!")




# import requests
# from django.shortcuts import render, redirect

# def get_weather(request):
#     city = request.GET.get('city')  # Get the city from the query string
#     if city:
#         api_key = '206f66d222574e869a7183005240512'  # Replace with your actual Weatherbit API key
        
#         # Step 1: Get the city's latitude and longitude from the current weather endpoint
#         current_weather_url = f"http://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"
#         current_response = requests.get(current_weather_url)
        
#         # Debugging: Print the response
#         print("API Response:", current_response.text)  # Check the raw API response
        
#         if current_response.status_code == 200:
#             current_weather_data = current_response.json()
            
#             # Check if the city data exists in the response
#             if 'data' in current_weather_data and current_weather_data['data']:
#                 lat = current_weather_data['data'][0]['lat']  # Get latitude
#                 lon = current_weather_data['data'][0]['lon']  # Get longitude

#                 # Step 2: Get hourly and daily forecast data
#                 forecast_url = f"http://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lon}&key={api_key}&days=10"
#                 hourly_url = f"http://api.weatherbit.io/v2.0/forecast/hourly?lat={lat}&lon={lon}&key={api_key}&hours=24"
                
#                 forecast_response = requests.get(forecast_url)
#                 hourly_response = requests.get(hourly_url)

#                 if forecast_response.status_code == 200 and hourly_response.status_code == 200:
#                     daily_forecast = forecast_response.json()['data']
#                     hourly_forecast = hourly_response.json()['data']

#                     # Extract current weather info
#                     current_temp = current_weather_data['data'][0]['temp']
#                     current_desc = current_weather_data['data'][0]['weather']['description']
#                     current_icon = current_weather_data['data'][0]['weather']['icon']
                    
#                     # Build the context to pass to the template
#                     context = {
#                         'city': city,
#                         'temperature': current_temp,
#                         'description': current_desc,
#                         'icon': current_icon,
#                         'hourly_forecast': hourly_forecast,
#                         'daily_forecast': daily_forecast,
#                     }
#                     return render(request, 'weather.html', context)
#                 else:
#                     print(f"Error fetching forecast data: {forecast_response.text}")
#                     return render(request, 'home.html', {'error': 'Unable to fetch forecast data!'})
#             else:
#                 # Handle case where city data is not found
#                 return render(request, 'home.html', {'error': 'City not found!'})
#         else:
#             # Handle invalid response from the current weather API
#             print(f"Error fetching current weather data: {current_response.text}")
#             return render(request, 'home.html', {'error': 'City not found!'})
#     else:
#         return redirect('home')  # Redirect to the home page if no city is entered

# def home(request):
#     return render(request, 'home.html')


# from django.shortcuts import render, redirect
# import requests

# def home(request):
#     return render(request, 'home.html')  # The page with the search bar

# def get_weather(request):
#     if request.method == 'GET':
#         city = request.GET.get('city')
#         if city:
#             # Replace with your actual Weatherbit API key
#             api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=542c342af0d0d5f128a41ea863ae0e1c&units=metric"
#             response = requests.get(api_url)
#             if response.status_code == 200:
#                 weather_data = response.json()
#                 context = {
#                     'city': city,
#                     'temperature': weather_data['main']['temp'],
#                     'description': weather_data['weather'][0]['description'],
#                     'icon': weather_data['weather'][0]['icon'],
#                 }
#                 return render(request, 'weather.html', context)
#             else:
#                 # Handle invalid city error
#                 return render(request, 'home.html', {'error': 'City not found!'})
#         else:

#             return render(request, 'home.html', {'error': 'Please enter a city name.'})  # Handle missing city input




# import requests
# from django.shortcuts import render
# from django.http import JsonResponse

# def get_weather(request):
#     city = request.GET.get('city', 'London')  # Default city if not provided
#     api_key = '54a57bc234ad752a4f59e59cd372201d'  # Replace with your actual API key

#     # Call the OpenWeather API
#     response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params={
#         'q': city,
#         'appid': api_key,
#         'units': 'metric'
#     })

#     if response.status_code == 200:
#         data = response.json()
#         current_temperature = data['list'][0]['main']['temp']
#         daily_forecast = {}

#         for forecast in data['list']:
#             day = forecast['dt_txt'].split()[0]  # Extract date
#             if day not in daily_forecast:
#                 daily_forecast[day] = {
#                     'minTemp': forecast['main']['temp_min'],
#                     'maxTemp': forecast['main']['temp_max'],
#                     'description': forecast['weather'][0]['description'],
#                     'humidity': forecast['main']['humidity'],
#                     'windSpeed': forecast['wind']['speed'],
#                     'icon': forecast['weather'][0]['icon']
#                 }
#             else:
#                 daily_forecast[day]['minTemp'] = min(daily_forecast[day]['minTemp'], forecast['main']['temp_min'])
#                 daily_forecast[day]['maxTemp'] = max(daily_forecast[day]['maxTemp'], forecast['main']['temp_max'])

#         context = {
#             'city': city,
#             'currentTemperature': round(current_temperature),
#             'dailyForecast': daily_forecast,
#             'weatherIconUrl': 'https://openweathermap.org/img/wn/',
#             'unit': '°C'
#         }
#         return render(request, 'weather.html', context)
#     else:
#         return JsonResponse({'error': 'City not found!'}, status=404)







