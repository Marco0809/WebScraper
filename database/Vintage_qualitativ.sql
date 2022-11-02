SELECT id, name, vintage,
CASE WHEN vintage != 0 THEN 1 END as vintage_signalled,
CASE WHEN price > 0 THEN 1 END as sold, 
price,
minimum_price,
maximum_price
	FROM "Winehaus"."Wine";