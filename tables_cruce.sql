CREATE TABLE david-molina-test.HealthAtom.sales_with_currency_conversion AS
SELECT 
    a.sale_id,
    a.sale_amount_clp,
    a.sale_amount_clp / e.usd_rate AS sale_amount_usd,
    a.sale_amount_clp / e.euro_rate AS sale_amount_euro,
    a.sale_date
FROM 
    david-molina-test.HealthAtom.sales a
JOIN 
    david-molina-test.HealthAtom.exchange_rates b ON a.sale_date = b.date;