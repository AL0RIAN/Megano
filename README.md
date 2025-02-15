## Tech Stack
- **Backend**: Django
- **Frontend**: HTML/CSS + JavaScript
- **Database**: PostgreSQL
- **Payment Integration**: Stripe API
- **Containerization**: Docker

## Examples
This project is a team effort. My main contributions include:


<p align="center">
  <img src=https://github.com/user-attachments/assets/bd4936fb-b949-46fc-bfb2-d0dfc19bf68c width="800" alt="demo1" />
  <br>
  <i>Payment Integration with Stripe: Enables secure and seamless payments</i>
</p>
<p align="center">
  <img src=https://github.com/user-attachments/assets/7a0e2d9d-fde3-45e8-8d47-a6f9b854dc77 width="800" alt="demo1" />
  <br>
  <i>Product Comparison Service: Allows users to compare different products based on various attributes</i>
</p>

## How to run

### Step 1: Clone the Repository

First, clone the repository to your local machine by running the following command:

```bash
git clone https://gitlab.skillbox.ru/pythondjango_team41/teamproject_41.git
```

### Step 2: Configure Environment Variables

Create a `.env` file in the root directory of the project and add the necessary environment variables:
```
DEBUG = True
DJANGO_SECRET_KEY = 'django-insecure-xxxxxxxxxxxx'
DJANGO_ALLOWED_HOSTS = *

DB_ENGINE = "django.db.backends.postgresql"  # you can also use 'django.db.backends.sqlite3'
DB_HOST = 'db'
DB_PORT = '5433'
DB_NAME = megano
DB_USER = megano
DB_PASS = user1234!

DATABASE = postgress 

CACHES_BACKEND = "django_redis.cache.RedisCache"
CACHES_LOCATION = 'redis://redis:6379/1'

EMAIL_HOST='your_smpt_host'
EMAIL_PORT=465
EMAIL_HOST_USER='example@email.com'
EMAIL_HOST_PASSWORD='you_password'
DOMEN_APP='http://127.0.0.1:8000'

STRIPE_PUBLISHABLE_KEY = '' # Add your public Stripe API key
STRIPE_SECRET_KEY = '' # Add your private Stripe API key
```

### Step 3: Build and Start Docker Containers

Build and start the Docker containers using `docker-compose`:
```bash
docker compose -f docker-compose.yml up -d --build
```
This command will build the Docker images and start the containers as specified in docker-compose.yml.

### Step 4: Apply Database Migrations

Run the following commands to create and apply migrations:
```bash
docker compose -f docker-compose.yml exec web python manage.py makemigrations --no-input
```
```bash
docker compose -f docker-compose.yml exec web python manage.py migrate --no-input
```

### Step 5: Collect Static Files

Run the following command to collect static files:
```bash
docker compose -f docker-compose.yml exec web python manage.py collectstatic --no-input
```

### Step 6: Create a Superuser

Create a superuser to access the Django admin panel:
```bash
docker compose -f docker-compose.yml exec web python manage.py createsuperuser
```

### Step 7: Load Fixtures

Important:
- Load fixtures only after creating the superuser.
- Add other users only after loading fixtures.

To load the predefined fixtures, run:
```bash
docker compose -f docker-compose.yml exec web python manage.py loaddata fixtures/full-data.json
```
