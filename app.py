import json
import csv
import os
import re

from flask import Flask, request, jsonify, Response, render_template

from database import Database
from auth import auth

# Initialize the Flask app
app = Flask(__name__)

# Initialize the database
db = Database()

@app.route('/', methods=['GET'])
def home():
    """
    A description of the entire function, its parameters, and its return types.
    """
    endpoints = [
        {'url': '/', 'description': '/ - главная страница'},
        {'url': '/upload', 'description': '/upload - загрузка файла'},
        {'url': '/phonebook', 'description': '/phonebook -телефонная книга'},
        {'url': '/search', 'description': '/search - поиск'}
    ]
    return render_template('home.html', endpoints=endpoints)


@app.route('/upload', methods=['POST'])
@auth.login_required
def upload_file():
    """
    Function for uploading a file and extracting phone numbers from it.
    If no file is provided, it attempts to read phone numbers from the
    default file phones.csv.
    """
    phone_numbers = []  # инициализация списка номеров
    if 'file' in request.files:
        file = request.files['file']
        with file.stream as file_stream:
            reader = file_stream.readlines()
            for idx, row in enumerate(reader):
                if idx == 0:  # пропускаем первую строку с заголовками
                    continue
                data = row.decode('utf-8').strip().split(';')
                phone_numbers.append({
                    'first_name': data[0],
                    'last_name': data[1],
                    'phone': data[2]
                })
    else:
        # Если файл не передан, попробуйте взять файл phones.csv из корневой папки
        file_path = os.path.join(app.root_path, 'phones.csv')
        try:
            with open(file_path, 'rt', encoding='utf-8') as file:
                reader = file.readlines()
                for idx, row in enumerate(reader):
                    if idx == 0:  # пропускаем первую строку с заголовками
                        continue
                    data = row.strip().split(';')
                    phone_numbers.append({
                        'first_name': data[0],
                        'last_name': data[1],
                        'phone': data[2],
                    })
        except FileNotFoundError:
            return jsonify({'error': 'Default file phones.csv not found'}), 400

    db.add_phone_numbers(phone_numbers)
    return jsonify({'message': 'Phone numbers added successfully'}), 201


@app.route('/phonebook', methods=['GET'])
@auth.login_required
def get_phonebook():
    """
    A function to get the phonebook data by retrieving phone numbers from
    the database and returning them as a JSON response.
    """
    phone_numbers = db.get_phone_numbers()
    return Response(json.dumps(phone_numbers, ensure_ascii=False),
                    mimetype='application/json')


@app.route('/search', methods=['GET'])
@auth.login_required
def search_phone_number():
    """
    To search for a phone number in the database.
    Returns:
    - JSON response containing the search result for the phone number.
    """
    phone = request.args.get('phone')
    result = db.search_phone_number(phone)
    return Response(json.dumps(result, ensure_ascii=False),
                    mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
