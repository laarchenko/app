import os

from flask import Flask, render_template, request, redirect, jsonify
import psycopg2

app = Flask(__name__)
app.config

conn = psycopg2.connect(
    database = 'mydatabase',
    user = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD'),
    host = os.environ.get('DB_HOST'),
    port = 5432
)

@app.route('/users', methods=['GET'])
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    users = []
    for row in rows:
        user = {'id': row[0], 'name': row[1], 'email': row[2]}
        users.append(user)
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    return jsonify({'message': f'User {name} created successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    conn.commit()
    cursor.close()
    return jsonify({'message': f'User {name} updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'User deleted successfully'})

