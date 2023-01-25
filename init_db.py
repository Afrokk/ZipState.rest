import os
import psycopg2

# Initializes the PostgreSQL database

conn = psycopg2.connect(
        host="localhost",
        database="state_data",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS "State Data";')
cursor.execute('CREATE TABLE "State Data"('
        '"Zip Code" INTEGER NOT NULL PRIMARY KEY,'
        '"Zip Type" VARCHAR(20),'
        '"State" VARCHAR(20),'
        '"City" VARCHAR(30),'
        '"County" VARCHAR(100),'
        '"Timezone" VARCHAR(50),'
        '"SOI Code" VARCHAR(50),'
        '"Area Codes" VARCHAR(50),'
        '"Country" VARCHAR(50),'
        '"Latitude" FLOAT,'
        '"Longitude" FLOAT,'
        '"IRS Estimated Population" INTEGER);'
        )

conn.commit()
cursor.close()
conn.close()
