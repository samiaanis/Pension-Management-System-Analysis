CREATE DATABASE pension_management;
select *
from pension_management.pension;

--Average pension payout by region.

SELECT
  region,
  ROUND(AVG(monthly_pension),2) AS avg_pension
FROM pension_management.pension
GROUP BY region;


--Top 10 pensioners by payout.

SELECT
  pensioner_id,
  monthly_pension
FROM pension_management.pension
ORDER BY monthly_pension DESC
LIMIT 5;

--Identifying employees nearing retirement

SET @reference_date = '2026-01-16';

SELECT DISTINCT pensioner_id, retirement_date
FROM pension_management.pension
WHERE retirement_date BETWEEN @reference_date
  AND DATE_ADD(@reference_date, INTERVAL 1 YEAR)
ORDER BY retirement_date;

--Pension type and status distributions.

SELECT pension_type, COUNT(*) 
FROM pension_management.pension
GROUP BY pension_type;

SELECT pension_status, COUNT(*) 
FROM pension_management.pension
GROUP BY pension_status;


--Bucketing pensions based on the newly calculated years_of_service to analyze tenure vs. payout.

SELECT
  CASE
    WHEN years_of_service < 10 THEN '0–9'
    WHEN years_of_service < 20 THEN '10–19'
    WHEN years_of_service < 30 THEN '20–29'
    ELSE '30+'
  END AS service_bucket,
  ROUND(AVG(monthly_pension),2) AS avg_pension
FROM pension_management.pension
GROUP BY service_bucket;
