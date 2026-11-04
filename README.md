# Restaurant POS System

Multi-tenant SaaS + Standalone Restaurant POS System with Django REST Framework backend.

## Features
- POS (Orders, Payments, Tables)
- Menu/Catalog with Units & Conversions
- Purchases (PO/GRN) & Inventory with Stock Movements
- Expenses & Reports (P&L, COGS)
- Multi-branch Support
- Role-based Permissions
- Subscription & License Key System
- Docker Deployment Ready

## Quick Start (Docker)
```bash
cp apps/backend/.env.example apps/backend/.env
docker-compose up --build
```

Backend: http://localhost:8000
Admin: http://localhost:8000/admin

## Modes
- `APP_MODE=standalone` - Single installation, license key required
- `APP_MODE=saas` - Multi-tenant with subscriptions

## Tech Stack
- Backend: Django 5 + DRF + PostgreSQL + Redis + Channels
- Frontend: Next.js (to be added)
- Deployment: Docker

## Frontend (React + Vite)
```bash
cd apps/web
npm install
npm run dev
```
App: http://localhost:5173

## Features
- UTA-style POS
- Custom React Admin (replacing Django admin)
- Daily Opening/Purchases/Close Shop with stock reconciliation
- Detailed Expenses (Bar, Kitchen & BBQ)
- Daily & Monthly Reports with P&L
- Multi-branch, Multi-tenant (SaaS/Standalone)
