INSERT INTO WorkActivity (Contract, Weekday, MedicalID, JobPlaceID, OperationID, Amount, Payment)
VALUES ($1, $2, $3, $4, $5, $6, $7)
RETURNING *;

