-- +goose Up

CREATE TABLE MedicalStaff (
    ID SERIAL PRIMARY KEY,
    Surname VARCHAR(30) NOT NULL,
    Address VARCHAR(70) NOT NULL,
    Tax NUMERIC(4, 2) NOT NULL CHECK (Tax >= 0)
);

-- +goose Down

DROP TABLE MedicalStaff;
