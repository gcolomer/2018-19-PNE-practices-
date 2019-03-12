import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.github.com")
conn.request("GET", "/user/claudiar00/repos", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)

repos_raw = r1.read().decode("urf-8")
conn.close()

repos = json.loads(repos_raw)
repo = [0]
print()
