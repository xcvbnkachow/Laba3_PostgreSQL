-- +goose Up

CREATE TABLE JobPlace (
    ID SERIAL PRIMARY KEY,
    Office VARCHAR(50) NOT NULL,
    Address VARCHAR(70) NOT NULL,
    LocalBudgetTax NUMERIC(4, 2) NOT NULL CHECK (LocalBudgetTax >= 0)
);

-- +goose Down

DROP TABLE JobPlace;