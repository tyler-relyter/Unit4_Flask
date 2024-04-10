from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)

app.secret_key = 'Password01CSC227FlaskProject'

MYSQL_HOST = '172.18.213.15'
MYSQL_USER = 'admin'
MYSQL_PASSWORD = 'Password01'
MYSQL_DB = 'htbullard346'


@app.route('/')
def index():
    conn = mysql.connector.connect(
        host=MYSQL_HOST, 
        user=MYSQL_USER, 
        password=MYSQL_PASSWORD, 
        database=MYSQL_DB)
    cursor = conn.cursor()
    query = ("SELECT * FROM Courses")
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template('home.html', data=rows)


@app.route('/loadout', methods=['GET', 'POST'])
def loadout():
    if request.method == 'POST':
        name = request.form.get('name')
        # Connect to db
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        # Insert new data
        query = ("INSERT INTO loadout (name) VALUES (%s)")
        cursor.execute(query, (name,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Loadout added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('loadout.html')

@app.route('/character', methods=['GET', 'POST'])
def character():
    if request.method == 'POST':
        name = request.form.get('name')
        # Connect to db
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        # Insert new data
        query = ("INSERT INTO character (name) VALUES (%s)")
        cursor.execute(query, (name,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Character added successfully!', 'success')
        return redirect(url_for('loadout'))
    return render_template('character.html')





if __name__ == '__main__':
    app.run(debug=True)
