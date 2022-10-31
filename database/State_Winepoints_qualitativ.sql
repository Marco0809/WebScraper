SELECT id, name,
CASE WHEN winepoints != 0 THEN 1 END as winepoints_signalled,
CASE WHEN state NOT Like 'None' THEN 1 END as state_signalled,
CASE WHEN price > 0 THEN 1 END as sold, 
winepoints, state
	FROM "Winehaus"."Wine";