SELECT id, auctiondate, name, vintage, bottlesize_l, origin, 
price, minimum_price, maximum_price
	FROM "Winehaus"."Wine" 
	WHERE name like '%Chateau Latour%' AND
	vintage = 2004
	ORDER BY auctiondate;