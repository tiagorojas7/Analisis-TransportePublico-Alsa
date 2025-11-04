SELECT 
    t.trip_id,
    t.date_clea AS fecha,
    t.route_id,
    t.driver_id,
    t.bus_id,
    t.passengers,
    t.delay_min_clean AS delay_minutos,
    t.revenue_usd,
    t.delay_category,
    r.route_name,
    r.zone,
    r.route_type,
    r.region_macro AS region_ruta,
    r.average_speed_km_h,
    d.name AS conductor_nombre,
    d.experience_level,
    d.region_macro AS region_conductor,
    d.gender,
    b.model AS bus_model,
    b.fuel_type,
    b.año,
    b.capacity
FROM trips t
JOIN routes r ON t.route_id = r.route_id
JOIN drivers d ON t.driver_id = d.driver_id
JOIN buses b ON t.bus_id = b.bus_id
WHERE t.date_clea IS NOT NULL;
