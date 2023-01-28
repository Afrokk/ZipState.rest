import os, psycopg2
from flask import Flask, render_template, jsonify

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


# This is a dictionary of the columns in the database
columns = {
    "Zip Code": None,
    "Zip Type": None,
    "State": None,
    "City": None,
    "County": None,
    "Timezone": None,
    "IRS SOI Code": None,
    "Area Code": None,
    "Country": None,
    "Latitude": None,
    "Longitude": None,
    "IRS Estimated Population": None,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api")
def api():
    conn = connectToDatabase()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "State Data" ORDER BY RANDOM() LIMIT 1;')
    randomState = cur.fetchall()
    result = {key: value for key, value in zip(columns, randomState[0])}
    cur.close()
    conn.close()
    return jsonify(result)


@app.get("/api/<ZipCode>")
def getStateFromZipJSON(ZipCode):
    try:
        if not ZipCode.isnumeric():
            return jsonify({"Error": "Please provide a valid zip code (no letters!)."})

        conn = connectToDatabase()
        cur = conn.cursor()
        cur.execute('SELECT * FROM "State Data" WHERE "Zip Code" = %s;', (ZipCode,))
        state = cur.fetchall()

        if not state:
            return jsonify({"Error": "Invalid ZIP code."})

        result = {key: value for key, value in zip(columns, state[0])}
        cur.close()
        conn.close()
        return jsonify(result)
    except:
        return jsonify(
            {"Error": "Error while fetching data, please recheck your input."}
        )


@app.errorhandler(404)
def throwException(error):
    return jsonify({"Error": f"Code {error.code}: {error.description}"})
