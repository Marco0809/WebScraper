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
                Minimum_Price Float
            )
        """)


        
    def process_item(self, item, spider):

        # Extract Bottlesize
        try:
            idx = item["name"].rfind(',')
            bottlesize = float(item["name"][idx-1:idx+3].strip().replace(",", "."))
            # float(item["name"][-6:-2].strip().replace(",", "."))
        except ValueError as error:
            print(item["name"])
            print("Casting to float error: " + repr(error))

        # Extract Winepoints (no differentation between Parker, Wine Advocate or Wine Spectator points)
        try:
            points = int(item["description"][0:2])
        except: 
            points = 0

        self.cur.execute(""" 
            INSERT INTO "Winehaus"."Wine"(
	        auctiondate, name, vintage, bottlesize_l, origin, winepoints, description, state, packaging, price, minimum_price) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                item["auctiondate"].strftime('%Y-%m-%d %H:%M:%S'),
                str(item["name"]),
                int(re.search("[1-3][0-9]{3}", item["name"]).group()),  #TODO muss noch zu Vintage geparsed werden
                bottlesize,  
                str(item["origin"]),
                points,
                str(item["description"]),
                str(item["state"]),
                str(item["packaging"]),
                float(item["price"]),
                0,
            ))

        # VALUES ('2022-01-10', 'TEST', 2010, 0.75, 'Bordeaux', 'The Vine ADV', NULL, NULL, NULL, NULL);

        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()