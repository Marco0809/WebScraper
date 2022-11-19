SELECT id, auctiondate, 
CASE WHEN price > 0 THEN 1 END as sold, 
name, vintage, bottlesize_l, origin, 
winepoints, fill_level, state, packaging
	FROM "Winehaus"."Wine";
	
