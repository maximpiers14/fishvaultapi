# FishVault API

This is the backend API for the **FishVault** android application, for the course *Mobile Security*. It server the fish catalogue and images used in the Android client.

## Project structure

```
fishvault-api/
├── main.py # App factory, registers blueprints
├── api_routes.py # /api/fish and /api/fish/<id>
├── image_routes.py # /assets/<file> (fish images)
├── fish_data.py # Fish demo data (FISH variable)
├── assets/ # Fish images
├── requirements.txt
└── README.md
```

## API endpoints
```
| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | `/api/health`       | Health check (`{"status":"ok"}`)  |
| GET    | `/api/fish`         | All fish                          |
| GET    | `/api/fish/<id>`    | One fish by id (404 if not found) |
| GET    | `/assets/<file>`    | A fish image                      |
```

## Vulnerabilities

### IDOR

This API can be used with IDOR (for the project) but there is not sensitive data hidden here.

### Path Traversal

The image part of this API is not vulnerable to path traversal.

## Deployement

This API has been deployed on render (https://fishvaultapi.onrender.com).