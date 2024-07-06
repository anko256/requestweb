import requests

url = 'name_data'
 
response = requests.get(url,params={'key':'value'},timeout=1)
 
print(response.status_code)
print(response.text)

