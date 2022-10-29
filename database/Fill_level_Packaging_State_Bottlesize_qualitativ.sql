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