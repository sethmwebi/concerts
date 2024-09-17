# Concerts Database

## Overview

This project consists of a simple database schema for managing concerts. The database includes three main tables: `bands`, `venues`, and `concerts`. The `concerts` table establishes relationships between bands and venues, capturing the details of each concert, including the date.

## Database Schema

### 1. Bands Table

The `bands` table stores information about different bands.

| Column   | Type                 |
| -------- | -------------------- |
| id       | SERIAL (Primary Key) |
| name     | String               |
| hometown | String               |

### 2. Venues Table

The `venues` table stores information about different venues.

| Column | Type                 |
| ------ | -------------------- |
| id     | SERIAL (Primary Key) |
| title  | String               |
| city   | String               |

### 3. Concerts Table

The `concerts` table establishes relationships between the `bands` and `venues` tables, with additional information about the date of each concert.

| Column   | Type                                    |
| -------- | --------------------------------------- |
| id       | SERIAL (Primary Key)                    |
| band_id  | Integer (Foreign Key references Bands)  |
| venue_id | Integer (Foreign Key references Venues) |
| date     | String                                  |

## Relationships

- A concert belongs to a band and a venue.
- The `concerts` table uses `band_id` and `venue_id` to establish foreign key relationships with the `bands` and `venues` tables, respectively.

### Prerequisites

- PostgreSQL or any SQL-based database system that supports `SERIAL`
- SQL client for executing SQL queries

### Setting Up the Database

1. **Create the Bands Table**:
   ```sql
   CREATE TABLE bands (
       id SERIAL PRIMARY KEY,
       name TEXT NOT NULL,
       hometown TEXT
   );
   ```
2. **Create the Venues Table**:
   ```sql
   CREATE TABLE venues (
       id SERIAL PRIMARY KEY,
       title TEXT NOT NULL,
       city TEXT
   );
   ```
3. **Create the Concerts Table**:
   ```sql
   CREATE TABLE concerts (
       id SERIAL PRIMARY KEY,
       band_id INTEGER NOT NULL,
       venue_id INTEGER NOT NULL,
       date TEXT NOT NULL,
       FOREIGN KEY (band_id) REFERENCES bands(id),
       FOREIGN KEY (venue_id) REFERENCES venues(id)
   );
   ```
