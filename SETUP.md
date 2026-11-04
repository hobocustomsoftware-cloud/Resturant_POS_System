# Setup Instructions

## Backend (Django)
```bash
cd apps/backend
cp .env.example .env
```

## Run with Docker
```bash
docker-compose up --build
```

In another terminal:
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py seed_initial
docker-compose exec backend python manage.py createsuperuser
```

## Frontend (React)
```bash
cd apps/web
npm install
npm run dev
```

URLs:
- Backend: http://localhost:8000
- Admin: http://localhost:8000/admin (or use custom React Admin at /admin)
- Frontend: http://localhost:5173
- POS: http://localhost:5173/pos
- KDS: http://localhost:5173/kds
