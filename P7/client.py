import http.client
import json
import termcolor
from Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 =r1.read().decode("utf-8")
respuesta = json.loads(data1)
id = respuesta['data'][0]['id']
print(id)

conn.request("GET", "/sequence/id/"+id+"?content-type=application/json")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
respuesta = json.loads(data1)
print(respuesta)
cadena=respuesta['seq']
print(cadena)


s1 = Seq(cadena)
print("Total:", len(cadena))
print("G:",s1.count('G'))


print("A:",s1.count('A'))
print("T:",s1.count('T'))
print("G:",s1.count('G'))
print("C:",s1.count('C'))

print("A:",s1.perc('A'))
print("T:",s1.perc('T'))
print("G:",s1.perc('G'))
print("C:",s1.perc('C'))

print("Perc G:", s1.perc('G'))