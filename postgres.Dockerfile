FROM postgres:13.3-alpine

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB mydatabase

COPY create.sql /docker-entrypoint-initdb.d/