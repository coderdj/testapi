import requests
import json

server = "http://127.0.0.1:5000/users/"
headers={'Content-Type': 'application/json'}

def AddNewUser(userdoc):
    requests.post(server, data=json.dumps(userdoc), headers=headers)

def FetchUser(email):
    doc = requests.get(server, params={"email": email})
    return doc.json()

def AddItem(user, item):
    doc = requests.get(server, params={"email": user}).json()
    if '_items' not in doc or len(doc['_items'])<1:
        return
    doc = doc['_items'][0]
    user = doc['_id']
    etag = doc['_etag']
    
    items = []
    if 'listings' in doc:
        items = doc['listings']
    items.append(item)
    
    headers['If-Match'] = etag
    data = json.dumps({"listings": items})
    requests.patch(server+user+"/", data=data, headers=headers)

def GetUserItems(email):
    doc = requests.get(server, params={"email": email}).json()
    if '_items' not in doc or len(doc['_items'])<1:
        return
    doc = doc['_items'][0]

    if 'listings' not in doc:
        print("User " + email + " has no listings")
    items = doc['listings']

    for item in items:
        print("Item: "+item['title']+
              " in "+item['location']+
              ": "+item['description'])
    
