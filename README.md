# Restaurant POS System (UTA Style)

Django REST + React (Vite) POS with multi-branch, daily operations, stock reconciliation.

## Quick Start (Docker)
```bash
cp apps/backend/.env.example apps/backend/.env
docker-compose up --build
```

In another terminal:
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py seed_initial
docker-compose exec backend python manage.py createsuperuser
```

## URLs
- Frontend: http://localhost:5173
- POS: http://localhost:5173/pos
- KDS: http://localhost:5173/kds
- Custom Admin: http://localhost:5173/admin
- Backend API: http://localhost:8000/api
- Django Admin: http://localhost:8000/admin

## Features
- POS (Dine-in/Takeaway/Delivery, Tables, Hold/Resume, Payment)
- Purchases/GRN with stock update
- Daily Opening/Purchases/Close Shop with stock reconciliation
- Expenses by group (Bar/Kitchen/BBQ/General)
- Reports (Daily/Monthly, P&L with COGS)
- KDS Realtime
- Custom React Admin (replaces Django admin)
- Multi-tenant SaaS + Standalone with license/subscription

## Platforms
- Web: http://localhost:5173
- Desktop: Electron app (apps/desktop) - opens web POS
- Mobile: Expo app (apps/mobile) - iOS/Android
- Tablet: Responsive web app works on tablets
