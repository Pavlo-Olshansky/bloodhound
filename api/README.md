## GET TOKEN
To get token you must to POST username and password to `http://127.0.0.1:8000/api/api-token-auth/`.
Example in python:
```python
>>> url = "http://127.0.0.1:8000/api/api-token-auth/"
>>> data = {"username": "valid_username", "password": "valid_pass"}
>>> r = requests.post(url, data=data)
>>> r.text
```
The output will be like this:
```json
 { "Authorization Token": "c6a1f166790017ddb47d3d7f5e8efdf3187a5f28 }
```

## GET METHOD
Example how to get information from the website (python):
```python
>>> product_list_url = "http://127.0.0.1:8000/api/product/"
>>> product_detail_url = "http://127.0.0.1:8000/api/product/1/"
>>> headers = { "Authorization": "Token c6a1f166790017ddb47d3d7f5e8efdf3187a5f28" }
>>> r = requests.get(url=product_list_url, headers=headers)
>>> r.text
```

The output will be like this:
```json
{ 
    "id": 1, 
    "name": "first", 
    "code": 1, 
    "manufacturer": "first", 
    "manufacturer_code": "first", 
    "url": "http://example.com", 
    "status": "OK", 
    "created_at": "2017-10-12T16:29:56.815338+03:00", 
    "updated_at": "2017-10-12T16:29:56.815450+03:00", 
    "visited_at": "2017-10-12T16:30:31.120481+03:00", 
    "current_price": 1.0, 
    "last_price": 2.0, 
    "price_raw_variance": 3.0, 
    "price_percentage_variance": 4.0, 
    "price_changes": 5 
}
```

## POST METHOD
Example how to add product to the website (python):
```python
>>> url = 'http://127.0.0.1:8000/api/product/'
>>> data = { "id": 2, 
... "name": "second", 
... "code": 1, 
... "manufacturer": "second", 
... "manufacturer_code": "second", 
... "url": "http://example.com", 
... "status": "OK", 
... "created_at": "2017-10-12T16:29:56.815338+03:00", 
... "updated_at": "2017-10-12T16:29:56.815450+03:00", 
... "visited_at": "2017-10-12T16:30:31.120481+03:00", 
... "current_price": 1.0, 
... "last_price": 2.0, 
... "price_raw_variance": 3.0, 
... "price_percentage_variance": 4.0, 
... "price_changes": 5 }
>>> headers = { "Authorization": "Token c6a1f166790017ddb47d3d7f5e8efdf3187a5f28" }
>>> q = requests.post('http://127.0.0.1:8000/api/test/', headers=headers, data=data)
>>> q.text
```

The output will be like this:
```json
{ 
    "id": 2, 
    "name": "second", 
    "code": 1, 
    "manufacturer": "second", 
    "manufacturer_code": "second", 
    "url": "http://example.com", 
    "status": "OK", 
    "created_at": "2017-10-12T16:29:56.815338+03:00", 
    "updated_at": "2017-10-12T16:29:56.815450+03:00", 
    "visited_at": "2017-10-12T16:30:31.120481+03:00", 
    "current_price": 1.0, 
    "last_price": 2.0, 
    "price_raw_variance": 3.0, 
    "price_percentage_variance": 4.0, 
    "price_changes": 5 
}
```
