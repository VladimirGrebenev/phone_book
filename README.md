# About PhoneBook
Телефонная книжка, умеет:
- заливать в базу телефоны из файла cvs (first_name, last_name, phone).
- выводить список телефонов
- осуществлять поиск по телефону

# Stack
- Python > 3.9
- Flask==3.0.2
- Flask-HTTPAuth==4.8.0
- Jinja2==3.1.3
- mysql-connector-python==8.3.0
и т.д. -> requirements.txt

# To start 

1. стяни ветку мастер - pull master from github
2. установи docker, docker compose 
3. docker-compose up --build
4. переходи в браузере http://0.0.0.0:5000/

# To work

Доступные ендпоинты:
/ - главная страница
/upload - загрузка файла
/phonebook -телефонная книга
/search - поиск

Для проверки загрузки файла можно использовать:
1) curl -X POST -u admin:pass http://127.0.0.1:5000/upload - это в автоматическом режиме загрузит файл phone.csv из корня приложения
2) или используйте curl -X POST -u username:password -F "file=@/path/to/your/file" http://127.0.0.1:5000/upload
   
Для тестирования поиска:
1) в адресной строке браузера http://127.0.0.1:5000/search?phone=79284960493
2) или curl -X GET "http://127.0.0 .1:5000/search?phone=79284960493"
   
Для аутентификации:
1) можно использовать login: admin, password: pass
2) или захардкодить своего пользователя в auth.py
