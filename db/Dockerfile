# Dockerfile for PostgreSQL
FROM postgres:13-alpine

ENV POSTGRES_DB your_database
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

COPY database_setup.py /docker-entrypoint-initdb.d/

EXPOSE 5432
