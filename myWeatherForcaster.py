import weathercom
import json

'''
Desciption  : get the weather forecast
Example		: getWeatherForcastByAddress("koronadal")
'''

def getWeatherForcastByAddress(area):

	try:
		weather = weathercom.getCityWeatherDetails(area)
		weatherDetails = json.loads(weather)
		#print(weatherDetails)
		#print()

		millibars = str(weatherDetails['vt1observation']['altimeter'])
		temperature = str(weatherDetails['vt1observation']['temperature'])
		windSpeed = str(weatherDetails['vt1observation']['windSpeed'])
		humidity = str(weatherDetails['vt1observation']['humidity'])
		temperatureMaxSince7am = str(weatherDetails['vt1observation']['temperatureMaxSince7am'])
		uvIndex = str(weatherDetails['vt1observation']['uvIndex'])
		uvDescription = str(weatherDetails['vt1observation']['uvDescription'])
		visibility = str(weatherDetails['vt1observation']['visibility'])
		observationTime = str(weatherDetails['vt1observation']['observationTime'])
		dewPoint = str(weatherDetails['vt1observation']['dewPoint'])
		phrase = str(weatherDetails['vt1observation']['phrase'])
		windDirCompass = str(weatherDetails['vt1observation']['windDirCompass'])

		if windDirCompass == 'N':
			windDirCompass = "North"
		elif windDirCompass == 'W':
			windDirCompass = "West"
		elif windDirCompass == 'E':
			windDirCompass = "East"
		elif windDirCompass == 'S':
			windDirCompass = "South"

		elif windDirCompass == 'NE':
			windDirCompass = "North East"
		elif windDirCompass == 'SE':
			windDirCompass = "South East"
		elif windDirCompass == 'SW':
			windDirCompass = "South West"
		elif windDirCompass == 'NW':
			windDirCompass = "North West"

		forecast = "Todays weather forecast in "+area+" is: "+ temperature +" degree celcius suns temperature. " 
		forecast += "The recorded wind speed is "+windSpeed+" kilometers per hour in the " + windDirCompass + ' direction. '
		forecast += "The maximum recorded temperature is "+temperatureMaxSince7am+" degree cenlius since 7 in the morning and "
		forecast += "The atmospheric temperature is "+dewPoint+" degree celcius with the Humidity is "+humidity+"%. "
		
		if phrase == 'Rain Shower':
			forecast += "I think its raining outiside."
		elif phrase == 'Cloudy':
			forecast += "Its really looks cloudy outside, I think you need to bring with you your umbrella."
		elif phrase == 'Mostly Cloudy':
			forecast += "Its mostly cloudy, there is a probability of rain."
		elif phrase == 'Partly Cloudy' and uvDescription == 'Low':
			forecast += "Its Partly cloudy outside and the UV level is low, It would be nice to have a walk outside!"
		elif phrase == 'Partly Cloudy':
			forecast += "Its Partly cloudy outside and the UV level is quite high, you might need a sun protection sir!"

		return forecast

	except:

		return "Im sorry sir, Im unable to access the weather forecast information for now! Please try again later!"
