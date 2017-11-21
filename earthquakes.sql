sudo -u postgres psql postgres

CREATE USER "gme205user";
ALTER ROLE "gme205user" WITH PASSWORD '';
CREATE DATABASE "earthquakesdb" owner "gme205user";
GRANT ALL PRIVILEGES ON DATABASE earthquakesdb TO gme205user;

\c earthquakesdb;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
