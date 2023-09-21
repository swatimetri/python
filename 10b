import requests, json
api_key = "980fc61e5f43515a2ec709c871aa6b70"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

Dr. Babu Rao K 21CSL46 – Python Programming Laboratory 16
if x["cod"] != "404":

y = x["main"]
current_temperature = y["temp"]
current_pressure = y["pressure"]
current_humidity = y["humidity"]
z = x["weather"]
weather_description = z[0]["description"]
# print following values
print(" Temperature (in kelvin unit) = " + str(current_temperature) +
"\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
"\n humidity (in percentage) = " + str(current_humidity) +
"\n description = " + str(weather_description))

else:
print(" City Not Found ")
