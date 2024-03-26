# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем содержимое текущей директории в контейнер в /app
COPY . /app

# Устанавливаем клиентские утилиты MySQL
RUN apt-get update && apt-get install -y default-mysql-client

# Устанавливаем необходимые зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт, на котором работает приложение
EXPOSE 5000
