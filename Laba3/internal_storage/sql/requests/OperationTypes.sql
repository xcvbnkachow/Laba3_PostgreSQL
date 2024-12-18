INSERT INTO OperationTypes (ID, Name, StrongPoint, Stocks, Cost)
VALUES ($1, $2, $3, $4, $5)
RETURNING *;
