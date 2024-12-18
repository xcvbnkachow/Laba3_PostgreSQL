INSERT INTO JobPlace (ID, Office, Address, LocalBudgetTax)
VALUES ($1, $2, $3, $4)
RETURNING *; 
