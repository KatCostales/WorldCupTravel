from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import pymysql
import dotenv

# Use GET requests to return data from DB (retrieve)
# Use GET requests to return data from DB (retrieve)``
# Use POST request to change data in DB (update/create)


# CORS(app) # enables cross-domain requests
app = Flask(__name__, static_folder="./static") # Creates Flask app
CORS(app) # enables cross-domain requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

# 'Contact Us' submission
@app.route('/contact_submit', methods=['POST'])
def contact():
    data_received = request.get_json() # get JSON data
    print("im in contact")
    # Extract JSON data
    name = data_received.get('name')
    numPeople = data_received.get('people')
    #date = data_received.get('date')
    message = data_received.get('message')
    print(name)


    # Connect to database
    server = os.environ['DATAHOST']
    usr = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATABASE']
    
    print(usr)
    
    connection = pymysql.connect(host=server, user=usr, password=pwd, database=db)
    connection.autocommit(True)
    crsr = connection.cursor()




    sql = "INSERT INTO `Contact Requests` (Name, NumPeople, Date, Message) "
    sql = sql + f"VALUES ('{name}', {numPeople}, '{message}');"
    print(sql)

    crsr.execute(sql)

    return render_template("contact.html")

@app.route('/hostCities')
def hostCities():
    return render_template('hostCities.html')








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)