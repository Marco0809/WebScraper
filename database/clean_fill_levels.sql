SELECT fill_level, state
	FROM "Winehaus"."Wine"
	WHERE fill_level = '4';

UPDATE "Winehaus"."Wine" 
SET fill_level='4,5 cm' 
WHERE fill_level='4';