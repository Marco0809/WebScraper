SELECT auctiondate, avg(price),
	COUNT(CASE WHEN price > 0 THEN 1 END) AS lot_sold,
	COUNT(CASE WHEN price = 0 THEN 1 END) AS lot_not_sold
	FROM "Winehaus"."Wine"
	WHERE 1 = CASE WHEN winepoints != 0 THEN 1 ELSE 0 END AND -- reduces by 10000 rows
	1 = CASE WHEN packaging NOT Like 'None' THEN 1 ELSE 0 END -- reduces by 10000 rows
	GROUP BY auctiondate;
	--1 = CASE WHEN vintage != 0 THEN 1 END; -- vintage=0 reduces by 4500 rows
	
	
	
	
	--fill_level Like 'ts-hs'; -- reduces by another 4000
	--bottlesize_l = 3;



/*	WHERE co.DTEntered = CASE 
                          WHEN LEN('blah') = 0 
                               THEN co.DTEntered 
                          ELSE '2011-01-01' 
                     END 
					 
					 
	SELECT id, name,
CASE WHEN winepoints != 0 THEN 1 END as winepoints_signalled,
CASE WHEN state NOT Like 'None' THEN 1 END as state_signalled,
CASE WHEN price > 0 THEN 1 END as sold, 
winepoints, state
	FROM "Winehaus"."Wine";
	
SELECT id, name,
CASE WHEN packaging NOT Like 'None' THEN 1 END as packaging_signalled,
CASE WHEN bottlesize_l != 0 THEN 1 END as bottlesize_signalled,
CASE WHEN fill_level NOT Like 'None' THEN 1 END as fill_level_signalled,
CASE WHEN state NOT Like 'None' THEN 1 END as state_signalled,
CASE WHEN minimum_price != 0 THEN 1 END as min_price_signalled,
CASE WHEN maximum_price != 0 THEN 1 END as max_price_signalled,
CASE WHEN price > 0 THEN 1 END as sold, 
price,
minimum_price,
maximum_price
	FROM "Winehaus"."Wine";
	
*/