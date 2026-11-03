# Restaurant POS - Django Backend Plan

## 1) Tech Stack (Backend)
- **Framework**: Django 5.x + Django REST Framework (DRF)
- **Auth**: djangorestframework-simplejwt (access+refresh, HttpOnly cookie option)
- **DB**: PostgreSQL
- **Cache/Queue**: Redis + Celery (reports, low-stock alerts)
- **Realtime**: Django Channels (KDS sync)
- **Validation**: DRF serializers + custom validators
- **CORS**: django-cors-headers
- **Filtering/Pagination**: django-filter
- **Settings**: django-environ (env based config)

## 2) Project Structure
```
apps/backend/
├── core/           # settings, wsgi/asgi, urls, permissions, utils
├── tenants/        # multi-tenant logic, middleware, models
├── users/          # users, roles, permissions
├── accounts/       # auth
├── catalog/        # categories, items, units, conversions, recipes
├── purchases/      # suppliers, PO, GRN, payments
├── inventory/      # stock, movements, adjustments
├── sales/          # orders, POS, payments, tables
├── expenses/       # expenses, categories
├── reports/        # P&L, sales/purchase/stock reports
├── billing/        # plans, subscriptions, license
├── kds/            # kitchen display
└── utils/          # helpers, base models
```

## 3) Multi-Tenancy (Django)
- **Shared DB + tenant_id** on tenant-scoped models
- **Middleware**: `TenantMiddleware` - get tenant from subdomain/header/user
- **BaseModel**: `tenant = ForeignKey(Tenant, ...)`
- **Managers/QuerySets**: auto-filter by tenant
- **APP_MODE**: `standalone|saas` from env

## 4) Apps & Key Models

### tenants
```python
Tenant(id, name, slug, mode, status, plan, settings, created_at)
License(id, tenant, license_key, issued_at, expires_at, max_branches, max_users, features, status, hardware_id)
Plan(id, name, price, interval, features, limits)
Subscription(id, tenant, plan, status, starts_at, ends_at, stripe_id)
```

### users
```python
Role(id, tenant, name, permissions)
User(AbstractUser) - add tenant, branch, role, phone
```

### catalog
```python
UnitGroup(id, name)
Unit(id, group, name, code, symbol, is_base)
UnitConversion(id, from_unit, to_unit, factor)
Category(id, tenant, name)
Item(id, tenant, category, name, sku, price, cost_price, track_stock, type)
ItemUnit(id, item, unit, is_default, is_purchase, is_sell)
ItemRecipe(id, item, raw_item, quantity, unit)
```

### purchases/inventory
```python
Supplier(id, tenant, name, phone, email)
Purchase(id, tenant, branch, supplier, invoice_no, date, subtotal, tax, total, paid_amount, status)
PurchaseItem(id, purchase, item, quantity, unit, unit_price, total)
Stock(id, tenant, branch, item, unit, quantity)
StockMovement(id, tenant, branch, item, unit, quantity, type, ref_type, ref_id, cost_price, created_by)
```

### sales
```python
Table(id, tenant, branch, name, capacity, status)
Order(id, tenant, branch, user, table, order_no, status, type, subtotal, discount, tax, service_charge, total)
OrderItem(id, order, item, quantity, unit, price, total, modifiers)
Payment(id, order, amount, method, ref_no)
```

### expenses
```python
ExpenseCategory(id, tenant, name)
Expense(id, tenant, branch, category, amount, date, payee, notes)
```

### billing/license
Validation logic for license key (signed JWT) - verify signature, expiry, limits.

## 5) API Endpoints (DRF)
- Auth: POST /api/auth/login/, refresh/, logout/
- Catalog: /api/catalog/items/, categories/, units/
- POS: /api/sales/orders/, create-order/, pay/, hold/
- Purchases: /api/purchases/
- Inventory: /api/inventory/stock/, movements/
- Reports: /api/reports/sales/, p&l/, stock/
- Billing: /api/billing/plans/, subscribe/, license/validate/

## 6) Permissions & Middleware
- `TenantRequiredMixin` / custom permissions
- Role-based permissions (cashier/waiter/kitchen/manager/admin)
- License/subscription enforcement in middleware
- Feature flags by plan/license

## 7) Docker Setup
- `Dockerfile` (multi-stage: build + runtime)
- `docker-compose.yml` (web/api, postgres, redis, celery, channels)
- `.env.example` with APP_MODE, DATABASE_URL, REDIS_URL, SECRET_KEY, LICENSE_PUBLIC_KEY

## 8) Implementation Steps
1. Django project setup (core/settings split)
2. Tenant middleware + base models
3. Auth + users/roles
4. Catalog + Units
5. Purchases + Inventory + Stock movements
6. Sales/POS + Tables
7. Expenses
8. Reports (P&L with COGS)
9. Billing/License
10. KDS + Channels
11. Dockerization + docs
