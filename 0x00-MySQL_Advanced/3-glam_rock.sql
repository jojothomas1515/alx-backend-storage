-- select bands with Glam rock as the main styles and calculate the lifspan with info or form data and split date
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style Like 'Glam rock%'
ORDER BY lifespan DESC;
