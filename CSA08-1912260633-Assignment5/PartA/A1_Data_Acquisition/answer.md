# A1 — Data Acquisition Design (7 marks)

## A1.1 Source inspection
Each station CSV is expected to contain date, hour, station, PM2.5, PM10, NO2 and temperature. Issues: missing values (`NA`/blank), negative readings, impossible values, duplicate rows, Fahrenheit mixed with Celsius, inconsistent station names, invalid dates, malformed rows, and non-numeric text. Example: `Adyar,2026-10-02,NA`.

## A1.2 SQLite design
- `stations(station_id INTEGER PRIMARY KEY, station_name TEXT UNIQUE NOT NULL)`
- `readings(reading_id INTEGER PRIMARY KEY, station_id INTEGER NOT NULL, date TEXT NOT NULL, hour INTEGER, pm25 REAL, pm10 REAL, no2 REAL, temperature_c REAL, FOREIGN KEY(station_id) REFERENCES stations(station_id))`
- Index: `CREATE INDEX idx_readings_station_date ON readings(station_id, date);`
CSV station/date/hour/readings map to station name, date/hour and numeric columns. A station ID is used as a foreign key.

## A1.3 Example board questions and SQL
1. Average PM2.5 for Adyar: `SELECT AVG(pm25) FROM readings JOIN stations USING(station_id) WHERE station_name=?;`
2. Highest PM2.5 station: `SELECT station_name, MAX(pm25) FROM readings JOIN stations USING(station_id) GROUP BY station_name ORDER BY MAX(pm25) DESC LIMIT 1;`
3. Daily average PM2.5: `SELECT date, AVG(pm25) FROM readings GROUP BY date ORDER BY date;`

## CSV vs SQLite
Loading CSV and scanning for every question costs O(n) time per query and requires the data in memory (roughly O(n)). SQLite stores records on disk and indexes station/date; indexed lookup is approximately O(log n), while disk usage is O(n). CSV is easy to exchange, but SQLite is preferable for repeated queries and persistent daily data.
