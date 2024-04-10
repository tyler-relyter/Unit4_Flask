from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)

app.secret_key = 'Password01CSC227FlaskProject'

MYSQL_HOST = 'helldivers.c9ese08asz4j.us-east-2.rds.amazonaws.com'
MYSQL_USER = 'admin'
MYSQL_PASSWORD = 'Password01'
MYSQL_DB = 'helldivers'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/loadout', methods=['GET', 'POST'])
def loadout():
    if request.method == 'POST':
        support_weapon = request.form.get('support_weapon')
        orbital_airstrike = request.form.get('orbital_airstrike')
        sentry = request.form.get('sentry')
        backpack = request.form.get('backpack')
        # Connect to db
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        # Insert new data
        query = ("INSERT INTO `loadout` (`support_weapon`, `orbital_airstrike`, `sentry`, `backpack`) VALUES (%s, %s, %s, %s);")
        cursor.execute(query, (support_weapon, orbital_airstrike, sentry, backpack))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Loadout added successfully!', 'success')
        return redirect(url_for('loadout'))
    else:
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        query = ("SELECT * FROM `loadout`;")
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template('loadout.html', data=rows)

@app.route('/character', methods=['GET', 'POST'])
def character():
    if request.method == 'POST':
        armor = request.form.get('Armor')
        emote = request.form.get('Emote')
        cape = request.form.get('Cape')
        # Connect to db
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        # Insert new data
        query = ("INSERT INTO `character` (`armor`, `emote`, `cape`) VALUES (%s, %s, %s);")
        cursor.execute(query, (armor, emote, cape))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Character added successfully!', 'success')
        return redirect(url_for('character'))
    else:
        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB)
        cursor = conn.cursor()
        query = ("SELECT * FROM `character`;")
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template('character.html', data=rows)





if __name__ == '__main__':
    app.run(debug=True)
