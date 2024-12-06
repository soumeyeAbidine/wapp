
# from django.shortcuts import render, redirect
# import requests

# def home(request):
#     return render(request, 'index.html')  # The page with the search bar

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

#             return render(request, 'index.html', {'error': 'Please enter a city name.'})  # Handle missing city input



from django.shortcuts import render
import requests

def home(request):
    return render(request, 'index.html')  # The page with the search bar

def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        if city:
            # Replace with your actual OpenWeatherMap API key
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=542c342af0d0d5f128a41ea863ae0e1c&units=metric"
            response = requests.get(api_url)
            if response.status_code == 200:
                weather_data = response.json()
                context = {
                    'city': city,
                    'temperature': weather_data['main']['temp'],
                    'description': weather_data['weather'][0]['description'],
                    'icon': weather_data['weather'][0]['icon'],
                }
                return render(request, 'index.html', context)
            else:
                # Handle invalid city error
                return render(request, 'index.html', {'error': 'City not found!'})
        else:
            return render(request, 'index.html', {'error': 'Please enter a city name.'})













