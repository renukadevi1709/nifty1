SELECT COUNT(*) FROM companies;

SELECT COUNT(*) FROM profitandloss;

SELECT COUNT(*) FROM balancesheet;

SELECT COUNT(*) FROM cashflow;

SELECT COUNT(*) FROM stock_prices;

SELECT company_name, ticker
FROM companies
LIMIT 10;

SELECT DISTINCT sector
FROM companies;

SELECT *
FROM financial_ratios
LIMIT 10;

SELECT *
FROM peer_groups
LIMIT 10;

SELECT *
FROM analysis
LIMIT 10;