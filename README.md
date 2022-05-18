Чтобы запустить проект нужно:  
установить зависимости - pipenv - sync; pipenv shell.  
создать бд postgres: sudo su postgres; CREATE DATABASE test_django; GRANT ALL privileges ON DATABASE test_django TO postgres;  
запустить проект из каталога backend:  ./manage.py runserver  

Примеры запросов из Postman:  
Получить список Торговых точек привязанных к переданному номеру телефона  
http://127.0.0.1:8000/visits/list_point_sale/?num_ph=8932454545454  
Ответ:  
{  
  "Points of sale:": [
    {
      "uuid": "b2d29867-3d0b-d497-9191-18a9d8ee1111",
      "name": "MTS"
    },
    {
      "uuid": "b2d29867-3d0b-d497-9191-18a9d8ee2222",
      "name": "Beeline"
    }
  ]
}


Выполнить посещение в Торговую точку  
http://127.0.0.1:8000/visits/visit_point_sale/  
{  
  "point_sale_id": "b2d29867-3d0b-d497-9191-18a9d8ee1111",  
  "latitude": "19.3056342",  
  "longitude": "19.3056342"  
}  
  
Ответ:  
{  
  "Посещение торговой точки:": {  
    "point_sale_id": "b2d29867-3d0b-d497-9191-18a9d8ee1111",  
    "date_visit": "2022-05-18T13:20:55.127103Z",  
    "latitude": 19.3056342,  
    "longitude": 19.3056342  
  }  
}  
