# backoffice
**BackOffice CRM system.**

<div style="display: flex; justify-content: space-between;">
    <img src="./images/logo.webp" alt="Image 1" style="width: 80%;"/>
</div>

## How to run
1. Configure `.env` file from `.env.sample`.<br/>
2. Run command:<br/>
`docker compose up --build`<br/>
3. Find containers ID:<br/>
`docker ps`<br/>
4. Open sh for web service and migrate:<br/>
`docker exec -it <container id> sh`<br/>
`cd backoffice_crm`<br/>
`python manage.py migrate`<br/>
5. Create super-user:<br/>
`python manage.py createsuperuser`
6. Run command to create roles:<br/>
`python manage.py create_roles`
Check if db in container is migrated:<br/>
`docker exec -it <container id> sh`<br/>
`psql -U <user login> <dbname>`<br/>
`\dt`<br/>
You'll see new tables.
## Usage
1. Open `127.0.0.1:8000/admin` and log in as a superuser. Create user, place him to the group "administrator" and set staff status.
2. Go to profiles and set to new user role administrator. 
3. Log in as a new user. Using him you can access to admin panel and create other users with roles operator, manager, marketer.
## Powered by Django, PostgreSQL and Docker
<div style="display: flex; justify-content: space-between;">
    <img src="./images/docker.webp" alt="Image 1" style="width: 30%;"/>
    <img src="./images/django.png" alt="Image 2" style="width: 30%;"/>
    <img src="./images/postgres.png" alt="Image 3" style="width: 30%;"/>
</div>