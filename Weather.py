import requests

api_key = "87d845b0b6cf29baa1a73cc34b067a95"
url= "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 
full_url = url + "q=" + city_name + "&appid=" + api_key
req = requests.get(full_url)
info = req.json() 

if info["cod"] != "404": 
    x = info["main"] 
    current_temperature = x["temp"]
    tnc = round(float(current_temperature - 273.15),2)
    current_pressure = x["pressure"] 
    current_humidiy = x["humidity"] 
    z = info["weather"] 
    weather_description = z[0]["description"]
    s = info["wind"]
    speed = s["speed"]
    print()
    print("Temperature (in celsius unit): ", 
                  round(float(current_temperature - 273.15),2) , "°C",
            "\nAtmospheric pressure : " +
                  str(current_pressure) + "hpa"
            "\nHumidity : " +
                  str(current_humidiy) + "%"
            "\nDescription: " +
                  str(weather_description).capitalize()+
                "\nWind Speed :" + str(speed) + "m/s")

else: 
  print(" City Not Found ")
