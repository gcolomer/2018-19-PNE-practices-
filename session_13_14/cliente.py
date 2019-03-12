import http.client

PORT = 80

conn = http.client.HTTPConnection('academia-atica.com', 80)
conn.request("GET" , "/")

r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 =r1.read().decode("utf-8")

print(data1)