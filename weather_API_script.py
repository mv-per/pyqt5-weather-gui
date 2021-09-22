
import requests
#API documentation https://openweathermap.org/current
import weather_class

weather = weather_class.CurrentWeather()

def translate_weather_data(data):
    global weather
    cod = int(data['cod'])
    if cod == 401 or cod == 429 or cod == 404:
        print(f"ERROR: {data['cod']} - {data['message']}")

    # elif data['cod'] == "200":
    else:
        print(data)
        weather.setMain(data["main"])
        # main = data['main']
        wind = data['wind']
        sky = data['weather']


        weather.sky_description = sky[0]['description']
        weather.wind_speed = wind['speed']


def get_weather(API, city_id):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + f"id={city_id}&APPID={API}" #
    # print(complete_url)
    response = requests.get(complete_url) #retuns the json code for the city

    updated_response = response.json()
    translate_weather_data(updated_response)




if __name__ == "main":
    pass
# 



