-- Table: Winehaus.Wine

-- DROP TABLE IF EXISTS "Winehaus"."Wine";

CREATE TABLE IF NOT EXISTS "Winehaus"."Wine"
(
	ID INT NOT NULL,
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
	PRIMARY KEY (ID)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Winehaus"."Wine"
    OWNER to postgres;