# Example of getting information about the weather of
# a location

import http.client
import json
import sys
city = input("Ask for a city: ")
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="+city
METHOD = "GET"
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT , None, headers)

r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

infocity = json.loads(text_json)
if len(infocity) == 0:
    print("The information about the city is not available")
    sys.exit()
print(infocity)
woeid= infocity[0]['woeid']





# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"

# -- For the location we have to use the
# -- Were on earth identifier
# -- London woeid = 44418
# -- Madrid woeid = 766273
LOCATION_WOEID = "766273"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

# -- Get the data
time = weather['time']
sun_set = weather['sun_set']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']


print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
print("The time the sun is set: {}".format(sun_set))
