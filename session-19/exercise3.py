# Example of getting information stored in github

import http.client
import json
ID = input("Inser a user name: ")


# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
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
conn.request(METHOD, ENDPOINT + ID, None, headers)

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
user = json.loads(text_json)

# -- Get some data
login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + ID +'/repos', None, headers)
r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
text_json = r1.read().decode("utf-8")
conn.close()

repositories = json.loads(text_json)

for repo in repositories:
    print(repo['name'])


HOSTNAME = "api.github.com"
ENDPOINT = "/repos/"+ID+"/2018-19-PNE-practices/commits"
METHOD = "GET"

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT , None, headers)
r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
text_json = r1.read().decode("utf-8")
conn.close()

response = json.loads(text_json)
print ("Total commmits: ", len(response))

