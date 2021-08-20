import requests

response = requests.post('http://localhost:7000/api/FallEvent', json ={
        "username": "usuariosilla1",
        "photo": "foto",
        "latitude": 19.4436952,
        "longitude": -70.68114969999999,
        "dateTime": "2021-08-20"
    })

print(response.json())
