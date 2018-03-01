import requests
import json

# Load the city list file
data = json.load(open('city.list.json'))


# By City Name
'''
API call:

api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
Parameters:

q city name and country code divided by comma, use ISO 3166 country codes

Examples of API calls:

api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml
'''

def byCityname():
	print([x['name'] for x in data])
	cityname = input("Enter city name from the above list : ")
	print([x['country'] for x in data if x['name'] == cityname])
	countrycode = input("Enter the country code from the above list : ")
	print ("Weather forecast for 5 days with data every 3 hours by city name,"+ cityname+ "for the country code,", countrycode)

	# Make a get request with the parameters.
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="+cityname+","+countrycode+"&mode=json&APPID=8cb86f72f2f3bf797c62e81ed1caaf1e")
	
	if(response):
        # Print the content of the response (the data the server returned)
		parsed = json.loads(response.content)
		print(json.dumps(parsed, indent=4, sort_keys=True))
	else:
		print("Incorrect parameters..!!")
	return


# By city ID
'''
API call:

api.openweathermap.org/data/2.5/forecast?id={city ID}
Parameters:

id city ID
Examples of API calls:

api.openweathermap.org/data/2.5/forecast?id=524901
'''
def byCityId():
	cityid = [x['id'] for x in data]
	print(cityid)
	input_cityid = input("Enter the city id of your choice from the above list : ")
	print("Weather forecast for 5 days with data every 3 hours by city ID", input_cityid)

	# Make a get request with the parameters.
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id="+input_cityid+"&mode=json&APPID=8cb86f72f2f3bf797c62e81ed1caaf1e")

	if(response):
		# Print the content of the response (the data the server returned)
		parsed = json.loads(response.content)
		print(json.dumps(parsed, indent=4, sort_keys=True))
	else:
		print("Incorrect parameters..!!")
	return


# By geographic coordinates
'''
API call:

api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}
Parameters:

lat, lon coordinates of the location of your interest
Examples of API calls:

api.openweathermap.org/data/2.5/forecast?lat=35&lon=139
'''

def byGeography():
	coord = [x['coord'] for x in data]
	print(coord)
	input_lat = input("Enter the Latitude of your choice from the above list : ")
	input_lon = input("Enter the corresponsing lon : ")	
	print("Weather forecast for 5 days with data every 3 hours by geographic coordinates")

	# Make a get request with the parameters.
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?lat="+input_lat+"&lon="+input_lon+"&mode=json&APPID=8cb86f72f2f3bf797c62e81ed1caaf1e")

	if(response):
		# Print the content of the response (the data the server returned)
		parsed = json.loads(response.content)
		print(json.dumps(parsed, indent=4, sort_keys=True))
	else:
		print("Incorrect parameters..!!")
	return


# By Zip Code - Where to get the zipcode details?
'''
By ZIP code
Description:

Please note if country is not specified then the search works for USA as a default.

API call:

api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}
Parameters:

zip zip code

Examples of API calls:

api.openweathermap.org/data/2.5/forecast?zip=94040,us
'''

# Main method
def main():
	print("Display 5 day weather forecast by :\n")
	print("1. City Name\n")
	print("2. City Id\n")
	print("3. Geography\n")
	option = int(input("Enter your option : "))

	if(option == 1):
		byCityname()
	elif(option == 2):
		byCityId()
	elif(option == 3):
		byGeography()	
	else:
		print("Incorrect choice..!")
		
if __name__ == '__main__':
    main()
