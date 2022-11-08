SELECT auctiondate, avg(price),
	COUNT(CASE WHEN price > 0 THEN 1 END) AS lot_sold,
	COUNT(CASE WHEN price = 0 THEN 1 END) AS lot_not_sold
	FROM "Winehaus"."Wine"
	WHERE 0 = CASE WHEN winepoints != 0 THEN 1 ELSE 0 END AND -- reduces by 10000 rows
	0 = CASE WHEN packaging NOT Like 'None' THEN 1 ELSE 0 END -- reduces by 10000 rows
	GROUP BY auctiondate;