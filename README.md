## Flow
* Run ```docker run -p 5432:5432 my-postgres``` to start db
* Run ```docker run -p 5000:5000 -e DB_USER=postgres -e DB_PASSWORD=password -e DB_HOST=localhost my-app``` to start app