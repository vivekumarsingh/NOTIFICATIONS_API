import requests
import json

data ={"email": "anand@tache.in", "password": "tachee"}
data= requests.post("http://13.233.186.205/rest-auth/login/", data)
headers = {'Content-type': 'application/json', 'Authorization': 'Token df60cad8f46658cdc1a03938aafdacebbef44f9c'}
data = requests.get("http://13.233.186.205/links/notifications/",headers=headers)          
print(data.status_code)
if data.status_code != 200:
    print("Bad Status")
elif data.status_code !=400:
    print("OK Status") 
a= data.json()
print(data.text)
for data in a ['results']:
    print (data['title'])

