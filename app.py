import os, json, psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def connectToDatabase():
    conn = psycopg2.connect(
        host="localhost",
        database="state_data",
        
        # Setup these environment variables!
        # Read README.md for more info.
        
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )
    return conn

@app.route("/")
def index():
    conn = connectToDatabase()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "State Data";')
    stateData = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', stateData=stateData)

@app.route("/api")
def api():
    #TO DO
    pass
