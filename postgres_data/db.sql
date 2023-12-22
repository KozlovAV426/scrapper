
CREATE TABLE flight (
     id SERIAL PRIMARY KEY,
     departure_airport TEXT NOT NULL,
     arrival_airport TEXT NOT NULL,
     departure_time TIMESTAMP NOT NULL,
     arrival_time TIMESTAMP NOT NULL,
     price INTEGER NOT NULL,
     flight_time INTEGER NOT NULL
);
