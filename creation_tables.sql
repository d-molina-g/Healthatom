CREATE TABLE david-molina-test.HealthAtom.sales (
    sale_id INT64,
    product_id INT64,
    customer_id INT64,
    sale_date DATE,
    sale_amount_clp FLOAT64,
    quantity INT64
);



CREATE TABLE david-molina-test.HealthAtom.exchange_rates (
    date DATE,
    usd_rate FLOAT64,
    euro_rate FLOAT64
);



INSERT INTO david-molina-test.HealthAtom.sales (sale_id, product_id, customer_id, sale_date, sale_amount_clp, quantity) 
VALUES 
    (1001, 501, 3001, '2024-01-01', 100000.00, 2),
    (1002, 502, 3002, '2024-01-02', 150000.50, 3),
    (1003, 503, 3003, '2024-01-03', 200000.75, 1),
    (1004, 504, 3004, '2024-01-04', 250000.20, 5),
    (1005, 505, 3005, '2024-01-05', 300000.00, 2),
    (1006, 506, 3006, '2024-01-06', 350000.60, 4),
    (1007, 507, 3007, '2024-01-07', 400000.40, 1),
    (1008, 508, 3008, '2024-01-08', 450000.30, 3),
    (1009, 509, 3009, '2024-01-09', 500000.00, 2),
    (1010, 510, 3010, '2024-01-10', 550000.50, 5);