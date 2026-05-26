# Scaffold

A minimal Django + PostgreSQL starter. Build your solution on top of this.

## Run

```bash
docker compose up --build
```

Server will be available at `http://localhost:8000`.

## Test

```bash
docker compose run --rm web python manage.py test
```

## Health check

```bash
curl http://localhost:8000/api/health/
# {"status": "ok"}
```

The health endpoint reads from the database — if it returns `{"status": "ok"}`, both the server and DB are up.
