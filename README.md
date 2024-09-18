# backoffice
BackOffice CRM
## How to run
Configure `.env` file from `.env.sample`.<br/>
Run command:<br/>
`docker compose up --build`<br/>
Find containers ID:<br/>
`docker ps -a`<br/>
Open sh for web service and migrate:<br/>
`docker exec -it <container id> sh`<br/>
`cd backoffice_crm`<br/>
`python manage.py migrate`<br/>
Check if db in container is migrated:<br/>
`docker exec -it <container id> sh`<br/>
`psql -U <user login> <dbname>`<br/>
`\dt`<br/>
You'll see new tables.