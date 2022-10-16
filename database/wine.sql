-- Table: Winehaus.Wine

DROP TABLE IF EXISTS "Winehaus"."Wine";

CREATE TABLE IF NOT EXISTS "Winehaus"."Wine"
(
	ID SERIAL PRIMARY KEY,
	Auctiondate TIMESTAMP NOT NULL,
	Name VARCHAR(1000) NOT NULL,
	Vintage INT,
	Bottlesize_l Float,
	Origin VARCHAR(255),
	Winepoints INT,
	Description VARCHAR(1000),
	Fill_level Varchar(10),
	State Varchar(255),
	Packaging Varchar(255),
	Price Float,
	Minimum_Price Float,
	Maximum_Price Float
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Winehaus"."Wine"
    OWNER to postgres;