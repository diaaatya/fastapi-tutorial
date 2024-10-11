import requests

#print(requests.get('http://127.0.0.1:8000/items/5').json())

print(requests.get('http://127.0.0.1:8000/items?name=Cola').json())

print(requests.get('http://127.0.0.1:8000/items?category=food').json())

print(requests.post("http://127.0.0.1:8000/",
                    json={"name": "juice", "price": 10, "count": 10, "category": "drinks", "id": 5}
                    ).json()
                    )
print("deleting item")
print(requests.delete('http://127.0.0.1:8000/4').json())

print("updating item")
print(requests.put("http://127.0.0.1:8000/items/5?count=50").json()), 
                                     
print(requests.get('http://127.0.0.1:8000/').json())
print("not vaild query")
print(requests.get('http://127.0.0.1:8000/items?category=cloths').json())

print(requests.get('http://127.0.0.1:8000/items?count=hello').json())

