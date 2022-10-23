SELECT id, name,
CASE WHEN winepoints != 0 THEN 1 END as winepoints_signalled,
CASE WHEN packaging IS NOT NULL THEN 1 END as packaging_signalled,
CASE WHEN vintage != 0 THEN 1 END as vintage_signalled,
CASE WHEN bottlesize_l != 0 THEN 1 END as bottlesize_signalled,
CASE WHEN origin IS NOT NULL THEN 1 END as origin_signalled,
CASE WHEN fill_level IS NOT NULL THEN 1 END as fill_level_signalled,
CASE WHEN state IS NOT NULL THEN 1 END as state_signalled,
CASE WHEN minimum_price != 0 THEN 1 END as min_price_signalled,
CASE WHEN maximum_price != 0 THEN 1 END as max_price_signalled
	FROM "Winehaus"."Wine";