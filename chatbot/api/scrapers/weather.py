import json
import requests


class WeatherScraper:

	def get(self):
		api_key = "ee3f2427f6fab2792b9ba8bc599c02c4"
		url = "http://api.openweathermap.org/data/2.5/weather?"
		city_name = "St. Catharines"
		url = url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(url)
		resp = response.json()
		if resp["cod"] != "404":
			main = resp["main"]
			current_temperature = main["temp"]
			current_humidity = main["humidity"]
			weather = resp["weather"]
			weather_description = weather[0]["description"]
			response = ("Weather in St. Catharines" + "\n\tTemperature: " +
							str(int(current_temperature - 273.15)) + "°C" +
				"\n\tHumidity: " +
							str(current_humidity) + "%" +
				"\n\tDescription: " +
							str(weather_description))
			return response
		else:
			response = "Weather unavailable"
			return response
