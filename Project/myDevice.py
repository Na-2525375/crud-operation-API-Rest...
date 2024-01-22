import requests 

URL="http://127.0.0.1:8000/myStudent_List"

r=requests.get(url=URL)
data=r.json()

print(data)




