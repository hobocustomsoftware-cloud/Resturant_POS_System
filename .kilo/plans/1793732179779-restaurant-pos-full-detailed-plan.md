# Restaurant POS - Full Detailed Plan (UTA Style + Daily Cash/Stock Flow)

## Goal
Build UTA-style Restaurant POS with Django REST API + React (Vite + Tailwind + shadcn/ui) frontend. Replace Django default admin with custom React Admin panel. Support Standalone + Multi-Tenant SaaS, Docker deployable, with license/subscription.

## Requirements Summary
- React frontend (not Next.js) for POS + Custom Admin (replacing Django admin)
- Daily flow: Opening Balance (Opening Cash/Stock) -> Purchases/GRN (add to stock) -> Sales/POS -> End of Day (Close Shop) with stock check/reconciliation
- Track daily purchases (goods received), sales, expenses
- Show profit/loss by day and monthly summary
- Detailed expense tracking (Bar, Kitchen & BBQ + General)
- Stock reconciliation: compare system stock vs actual count
- Opening balance carries to next day
- Purchases added to stock, Sales deduct from stock (include combos/recipes)
- Can fill in missing details (stock adjustments with reason)

## Tech Stack
### Backend (Django)
- Django 5.x + DRF, SimpleJWT, django-filter, django-cors-headers
- PostgreSQL, Redis, Channels
- Celery (reports/alerts)
- Custom permissions + tenant middleware

### Frontend (React)
- Vite + React + TypeScript
- TailwindCSS + shadcn/ui
- React Router, TanStack Query, Axios
- Zustand (cart/state)
- date-fns, recharts
- react-hot-toast

## Database Design Additions
### Daily Operations
- `DaySession` (tenant, branch, date, opened_by, closed_by, opening_cash, opening_stock_snapshot, status: open/closed, closed_at)
- `StockCount` / `StockReconciliation` (day_session, item, system_qty, actual_qty, difference, reason)
- `PurchaseDaily` linked to GRN with `day_session`

### Purchases
- `Purchase` with `day_session`, `received_by`, `status: draft/received/cancelled`
- `PurchaseItem` with qty/unit/price/total

### Sales
- Link `Order` to `day_session`

### Expenses (detailed)
- `ExpenseCategory` (Bar, Kitchen, BBQ, General, etc with type/group)
- `Expense` with `day_session`, `branch`, `category`, `amount`, `payee`, `receipt`, `notes`

### Reports
- Daily Summary, P&L by day/session, Monthly Summary, Expense breakdown by group

## Frontend Structure
```
apps/web/
├── src/
│   ├── app/ (routes)
│   ├── components/
│   │   ├── pos/ (menu-grid, cart, tables, payment)
│   │   ├── admin/ (custom admin replacing django admin)
│   │   ├── daily/ (opening, purchases, close-shop)
│   │   └── reports/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   └── stores/
```

## Routes
- /pos - POS screen (UTA style)
- /kds - Kitchen Display
- /admin - Custom React Admin (dashboard, products, purchases, sales, expenses, stock, reports, users/roles, settings, license/subscription)
- /daily/opening - Start day / set opening
- /daily/purchases - Daily purchase entry
- /daily/close - Close shop with stock reconciliation
- /reports/daily, /reports/monthly

## API Additions Needed
- /api/daily/sessions/ (open/close/current)
- /api/daily/purchases/
- /api/stock/reconcile/
- /api/reports/daily-summary/, /api/reports/monthly-summary/, /api/reports/pnl/
- /api/admin/* (for custom admin panel)

## Phases
1. Setup React frontend (Vite) + connect to API
2. Core API completion (serializers/views for all models)
3. Daily session system (opening/close/reconcile)
4. Purchases flow with stock update
5. Sales/POS + stock deduction (combos)
6. Expenses detailed by groups
7. Custom React Admin (replace Django admin)
8. Reports (daily/monthly/P&L with COGS)
9. KDS + Docker integration
