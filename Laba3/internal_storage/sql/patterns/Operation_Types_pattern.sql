-- +goose Up

CREATE TABLE OperationTypes (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    StrongPoint VARCHAR(70) NOT NULL,
    Stocks INTEGER NOT NULL CHECK (Stocks >= 0),
    Cost NUMERIC(10, 2) NOT NULL CHECK (Cost >= 0)
);

-- +goose Down

DROP TABLE OperationTypes;