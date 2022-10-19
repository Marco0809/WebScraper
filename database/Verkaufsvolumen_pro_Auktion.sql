SELECT auctiondate, sum(price) as price_sum, count(price) as number_lots, 
	COUNT(CASE WHEN price > 0 THEN 1 END) AS lot_sold,
	COUNT(CASE WHEN price = 0 THEN 1 END) AS lot_not_sold
	FROM "Winehaus"."Wine"
	GROUP BY auctiondate
	ORDER BY auctiondate;