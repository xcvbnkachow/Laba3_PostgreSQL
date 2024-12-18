INSERT INTO MedicalStaff (ID, Surname, Address, Tax)
VALUES ($1, $2, $3, $4) 
RETURNING *;