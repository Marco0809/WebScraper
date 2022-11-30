# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import time
import re

class PostgresWinePipeline:

    def __init__(self) -> None:
        ## Connection Details
        hostname = 'localhost'
        username = 'postgres'
        password = 'postgres'
        database = 'postgres'
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        ## Create Wine table of none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS "Winehaus"."Wine"
            (
                ID SERIAL PRIMARY KEY,
                Auctiondate TIMESTAMP NOT NULL,
                Name VARCHAR(1000) NOT NULL,
                Vintage INT,
                Bottlesize_l Float,
                Origin VARCHAR(255),
                Description VARCHAR(1000),
                State Varchar(255),
                Packaging Varchar(255),
                Price Float,
                Minimum_Price Float,
                Maximum_Price Float
            )
        """)


        
    def process_item(self, item, spider):

        # Extract Bottlesize
        try:
            idx = item["name"].rfind(',')
            bottlesize = float(item["name"][idx-1:idx+3].strip().replace(",", "."))
        except ValueError as error:
            print(item["name"])
            print("Casting to float error: " + repr(error))

        # Extract Winepoints (no differentation between Parker, Wine Advocate or Wine Spectator points)
        try:
            points = int(item["description"][0:2])
        except: 
            print("No Points found")
            points = 0

        # Extract Fill level
        try: 
            filllevel = item["state"][0:8]
            idx = filllevel.rfind(',')
            if idx > 0:     # exclude 'in', 'ts', ...
                filllevel = filllevel[0:idx]
        except:
            filllevel = 0

        # Extract vintage
        try:
            vintage = int(re.search("[1-3][0-9]{3}", item["name"]).group())
        except Exception as e:
            vintage = 0
            print("No vintage found: " + repr(e))
            pass


        #TODO Min Preis noch herausfiltern
        #   1. Füllniveau: in, ts, hs, hf, in, ms-lms, 0,5cm, 1cm, 1,5cm, 2cm, 3cm, 4cm 
        #   https://www.munichwinecompany.com/de/mwc-wine-fillings.html
        #   2. Etikett: Etikett ganz leicht verschmutzt, ganz leicht beschädigt, Kapsel leicht beschädigt

        try:
            self.cur.execute(""" 
                INSERT INTO "Winehaus"."Wine"(
                auctiondate, name, vintage, bottlesize_l, origin, winepoints, description, fill_level, state, packaging, price, minimum_price, maximum_price) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                    item["auctiondate"].strftime('%Y-%m-%d %H:%M:%S'),  # TODO: Fix parsing error with auction date where month and day get swapped
                    str(item["name"]),
                    vintage,  # vintage
                    bottlesize,  
                    str(item["origin"]),
                    points,
                    str(item["description"]),
                    filllevel,                  # fill level
                    str(item["state"]),
                    str(item["packaging"]),
                    float(item["price"]),
                    float(item["minimum_price"]),   
                    float(item["maximum_price"]),                               
                ))
        except Exception as e:
            print("Exception while inserting: " + repr(e))
            pass

        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()