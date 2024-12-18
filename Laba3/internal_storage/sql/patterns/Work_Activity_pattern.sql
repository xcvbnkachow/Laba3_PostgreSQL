-- +goose Up

CREATE TABLE WorkActivity (
    Contract SERIAL PRIMARY KEY,
    Weekday VARCHAR(15) NOT NULL,
    MedicalID INTEGER NOT NULL REFERENCES MedicalStaff(ID) ON DELETE CASCADE,
    JobPlaceID INTEGER NOT NULL REFERENCES JobPlace(ID) ON DELETE CASCADE,
    OperationID INTEGER NOT NULL REFERENCES OperationTypes(ID) ON DELETE CASCADE,
    Amount INTEGER NOT NULL CHECK (Amount >= 0),
    Payment NUMERIC(10, 2) NOT NULL CHECK (Payment >= 0)
);
Contract, Weekday, , JobPlaceID, OperationID, Amount, Payment

-- +goose Down

DROP TABLE WorkActivity;
