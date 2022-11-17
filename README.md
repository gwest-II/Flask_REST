#Приммеры API-запросов

POST http://127.0.0.1:5000/api_ads/4
Content-Type: application/json
    {

        "title": "Cat",
        "description": "green cat",
        "date_create": "28.10.2022",
        "owner": "Greg"
    }

###
GET http://127.0.0.1:5000/api_ads/

###
PUT http://127.0.0.1:5000/api_ads/4
Content-Type: application/json
    {

        "title": "Bird",
        "description": "green Bird",
        "date_create": "28.10.2022",
        "owner": "Greg"
    }

###
DELETE http://127.0.0.1:5000/api_ads/4