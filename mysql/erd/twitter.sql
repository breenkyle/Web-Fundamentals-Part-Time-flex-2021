SELECT clients.company, SUM(billing.amount) 
AS total_sales 
FROM clients LEFT JOIN billing 
ON billing.client_id = client.id 
GROUP BY clients.company 
HAVING SUM(billing.amount) > 3500;