# Restaurant POS System - Plan & Architecture

## 1) Goals
- ဘယ်စားသောက်ဆိုင်ပဲဖြစ်ဖြစ် အသုံးပြုနိုင်တဲ့ **အထွေထွေ POS** (Full Service / QSR / Cafe / Food Truck စသည်)
- **အဝယ် (Purchases)**၊ **အရောင်း (Sales)**၊ **ကုန်ကျစရိတ် (Expenses/COGS)**၊ **အမြတ်အရှုံး (P&L)** တိကျစွာတွက်ချက်ပြသနိုင်ခြင်း
- **Unit (ယူနစ်)** ကို Dynamic သတ်မှတ်နိုင်ခြင်း (pcs, bottle, kg, g, ml, l, box, pack, tray စသည်) + Unit Conversion
- **Multi-Tenancy SaaS** နှင့် **Standalone (Dedicated)** နှစ်မျိုးလုံး Support
- **Docker** ဖြင့် Deploy လုပ်နိုင်ခြင်း
- **Subscription / License Key** စနစ်ပါဝင်ခြင်း
- **Role/Permission**၊ **Branch/Outlet**၊ **User Management** ပါဝင်ခြင်း

## 2) Core Features

| Module | Details | Priority |
|---|---|---|
| **POS (Point of Sale)** | Order taking, Cart, Modifier/Add-ons, Table selection, Split bill, Merge table, Hold/Resume, Discounts, Service charge, Tax/VAT, Multiple payments (Cash/Card/QR) | P0 |
| **Menu/Catalog** | Categories, Items, Variants, Modifiers, Recipe/BOM (Combo item များအတွက်), Pricing, Item Availability | P0 |
| **Purchases (GRN/PO)** | Supplier, Purchase Order, Goods Received Note, Purchase Invoice, Return, Due/Payment, Purchase Price History | P0 |
| **Inventory/Stock** | Real-time stock, Low stock alert, Stock adjustment, Wastage, Transfer between branches, Batch/Expiry (လိုအပ်ပါက) | P0 |
| **Sales & Returns** | Invoice/Receipt, Sales Return/Credit Note, Customer (optional), Sales by user/shift/counter | P0 |
| **Expenses** | Daily expenses, Expense categories, Payee, Attachment, Linked to branch/user | P0 |
| **Units & Conversions** | Unit Master (Base/Derived), Conversion factors, Buy in different unit / Sell in different unit, Auto stock deduction by base unit | P0 |
| **Reports (P&L Focus)** | Sales Report, Purchase Report, COGS, Gross Profit, Expense Summary, Net Profit/Loss, Top selling, Stock Report, Valuation, Shift/End-of-day (Z/X Report) | P0 |
| **Users/Roles/Permissions** | Role-based access (Cashier, Waiter, Kitchen, Manager, Admin), Permission per module/action | P0 |
| **Branch/Outlet** | Multi-branch support, per-branch stock/pricing/users, branch transfer | P1 |
| **Kitchen Display System (KDS)** | Order queue by station, Status (New/Preparing/Ready/Served), Notifications | P1 |
| **Tables & Reservations** | Table layout, Status, Waitlist, Reservation (size/time) | P1 |
| **Customers & Loyalty** | Customer DB, Credit (tab), Loyalty points (optional) | P2 |
| **Integrations** | Thermal printer (ESC/POS), Cash drawer, Barcode/QR, E-commerce/Delivery (Grab/Foodpanda) later | P2 |

## 3) Unit System Design (Dynamic)

`Unit` ကို Flexible ဖြစ်အောင် ဒီပုံစံနဲ့ရေးသင့်ပါတယ်။

| Entity | Purpose |
|---|---|
| `unit_groups` | Category by type (Weight, Volume, Count, Length) |
| `units` | Master list (name, code, group_id, is_base, symbol) |
| `item_units` | Per item အတွက် အသုံးပြုမည့် units (purchase/sell allowed flags) |
| `unit_conversions` | `(from_unit_id, to_unit_id, factor)` eg. 1 Box = 12 pcs, 1 kg = 1000 g |
| `item_recipes` | BOM - raw item ကို base unit နဲ့တွက်ချက် |

**Logic:** Stock ကို **Base Unit** ဖြင့်သာ သိမ်း။ Purchase/Sale အချိန်မှာ Conversion ဖြင့် Base Unit သို့ ပြောင်းလဲပြီး Deduct/Add လုပ်မည်။

## 4) Multi-Tenancy Strategy

၂မျိုးအတွက် တစ်ခုတည်း Codebase ကနေ Config ဖြင့် ခွဲခြားမည်။

| Approach | Description | Notes |
|---|---|---|
| **Shared DB + `tenant_id`** | Table အားလုံးတွင် `tenant_id` ထည့်ပြီး Row-level filtering | SaaS အများအပြားအတွက် သင့်တော်ဆုံး၊ Cost/Infra အရ ချိုသာ၊ Migration လွယ် |
| **Schema-per-tenant** | Tenant တစ်ခုချင်း Schema ခွဲ | Isolation ပိုကောင်းသော်လည်း Migration/Scaling က ပိုရှုပ်ထွေး |
| **DB-per-tenant** | DB အပြည့်ခွဲ | အလွန် High Isolation (Enterprise) နောက်ပိုင်းတွင်သာ စဉ်းစား |

**Recommendation:** `Shared DB + tenant_id` (with strict middleware + row level security) စတင်ရန်။ `APP_MODE=saas|standalone` ဖြင့် ခွဲခြား။

**Standalone Mode:** `tenant_id = default` သတ်မှတ်ပြီး Billing/Subscription UI/Middleware ကို Disable လုပ်မည်။

## 5) Subscription, License Key & Access Control

| Feature | SaaS | Standalone |
|---|---|---|
| **Onboarding** | Tenant registration, Owner user, Plan selection | First-time setup wizard (Business info, Admin user) |
| **Plans** | Free/Basic/Pro/Enterprise (Module limits, branches, users) | N/A or "Licensed" |
| **Billing** | Stripe/PayMongo/2C2P (local) + Webhook, Invoice, Trial | None |
| **License Key** | Optional | **Required** - Signed JWT/Ed25519 signed key with `expiry`, `max_branches`, `features`, `hardware_id` (optional) |
| **Enforcement** | Middleware - check subscription status (active/trial/past_due/suspended) | Middleware - validate license key (online check or offline grace) |
| **Grace Period** | Configurable (e.g. 3-7 days) before read-only/block | Configurable grace for offline validation |

**License Design Suggestion:**

```json
{
  "lic_id": "LIC-XXXX-XXXX",
  "tenant_name": "Business Name",
  "issued_at": "...",
  "expires_at": "...",
  "features": ["pos","inventory","reports","multi_branch"],
  "limits": {"branches": 2, "users": 10},
  "sig": "..."
}
```

Server-side မှ Private Key နဲ့ Sign၊ App မှ Public Key နဲ့ Verify။

## 6) Tech Stack Recommendation

| Layer | Recommendation | Reason |
|---|---|---|
| **Frontend (POS UI)** | **Next.js (App Router) + TypeScript + Tailwind CSS + shadcn/ui** | Fast, component reusable, PWA friendly, tablet optimized |
| **Backend API** | **NestJS (TypeScript) + REST/JSON** or **tRPC** | Modular, DI, Guards/Interceptors, Validation, Scalable structure |
| **DB** | **PostgreSQL 16** | Relational, JSONB, Transactions, RLS, Mature |
| **ORM** | **Prisma** (DX ကောင်း) သို့မဟုတ် **Drizzle ORM** (Type-safe + SQL closer) | နှစ်မျိုးလုံးအဆင်ပြေ။ Drizzle က Migration/Performance ပိုထိရောက်တတ် |
| **Auth** | **JWT (access+refresh)** + RBAC/ABAC, HttpOnly cookies | Standard, Stateless |
| **Cache/Queue** | **Redis** (Sessions, rate-limit, reports cache, KDS realtime) | အရေးကြီးသောအပိုင်းများအတွက် |
| **Realtime** | **Socket.IO** or **WebSocket** | KDS, multi-counter sync |
| **Validation** | **Zod** | Schema validation end-to-end |
| **File/Upload** | Local volume or S3-compatible (MinIO) | Logos/receipts/attachments |

**Monorepo:** `apps/web`, `apps/api`, `packages/ui`, `packages/types`, `packages/db`, `packages/config`

## 7) High-Level Data Model (Key Entities)

| Entity | Notes |
|---|---|
| `tenants` | id, name, slug, mode(standalone/saas), status, plan_id, license_key_id, settings(JSON) |
| `users` | tenant_id, role_id, branch_id, name, email/phone, password_hash, status |
| `roles` / `permissions` | RBAC mapping |
| `branches` | tenant_id, name, address, tax_id, receipt_settings(JSON) |
| `units`, `unit_groups`, `unit_conversions` | Unit system |
| `categories`, `items`, `item_variants`, `item_modifiers`, `item_recipes` | Catalog + BOM |
| `suppliers`, `purchases`, `purchase_items`, `purchase_payments` | Purchases |
| `stock` / `stock_movements` | tenant_id, branch_id, item_id, base_unit_id, qty, cost_price, movement_type, ref_type/ref_id |
| `orders`, `order_items`, `order_modifiers`, `payments` | Sales/POS |
| `tables` | branch_id, name/number, status, capacity |
| `expenses`, `expense_categories` | Expenses |
| `shifts` | cashier_id, branch_id, start/end, cash_in/out, z_report_no |
| `plans`, `subscriptions`, `invoices`, `licenses` | Billing/License |

> `stock_movements` ကို **Audit Trail** အဖြစ် မဖြစ်မနေ ထားသင့် (Purchase/Return/Sale/Adjust/Waste/Transfer)

## 8) Deployment with Docker

Docker အခြေခံပြီး Flexible ဖြစ်အောင် ဒီပုံစံဖြစ်စေမယ်။

### docker-compose (Standalone / Self-host)
```yaml
services:
  app:
    build: .
    env_file: .env
    ports: ["8080:3000"]
    depends_on: [postgres, redis]
  postgres:
    image: postgres:16
    volumes: [pg_data:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
    volumes: [redis_data:/data]
volumes:
  pg_data:
  redis_data:
```

### Environment Split
- `.env.standalone` - `APP_MODE=standalone`, `LICENSE_REQUIRED=true`, billing disabled
- `.env.saas` - `APP_MODE=saas`, `STRIPE_*`, subscription middleware enabled

**Single Image, Multiple Modes:** Build တစ်ကြိမ်၊ Config မှာ Mode ပြောင်းသုံးနိုင်အောင်ထားရန် အကောင်းဆုံး။

**Reverse Proxy:** Traefik/Nginx ပါဝင်နိုင်ရန် ထည့်သ consideration။

## 9) Implementation Plan (Phased)

| Phase | Tasks | Goal |
|---|---|---|
| **Phase 0: Setup** | Monorepo, Docker, DB setup, Env, Lint/Typecheck, Base auth | Foundation |
| **Phase 1: Core POS** | Catalog, POS UI (cart/order), Payments, Receipts, Users/Roles, Branches | Minimal working POS |
| **Phase 2: Units + Purchases + Inventory** | Unit master/conversion, Suppliers, PO/GRN, Stock by base unit, Stock movements, Low stock | COGS အတွက် အခြေခံပြည့်စုံ |
| **Phase 3: Expenses + Reports + P&L** | Expenses, Shift/Z-Report, Sales/Purchase/Stock reports, COGS/Gross/Net P&L | ဘဏ္ဍာရေးဆိုင်ရာ တိကျမှု ရရှိ |
| **Phase 4: Multi-tenant + Billing/License** | Tenant isolation, Plans, Subscription (Stripe), License key generator/validator, Feature flags, Enforcement | SaaS + Standalone Monetization |
| **Phase 5: KDS/Tables + Polish** | KDS, Tables, Printer, UX polish, Migrations, Backup guide, Docs | Production ready |

## 10) Recommendations (Plan ရွေးချယ်မှုအကြံပြုချက်)

| Topic | Recommendation | Rationale |
|---|---|---|
| **Start** | **Monolith** (API + Web same repo) | MVP အတွက် မြန်ဆန်၊ Deploy ရိုးရှင်း၊ Docker တစ်ခုတည်းနဲ့ လုပ်လို့ရ |
| **Tenancy** | **Shared DB + tenant_id + Global Query Filter** | Balance between simplicity & scalability |
| **Units** | **Always convert to base unit for stock** | ပမာဏအခြေခံမှားယွင်းမှု နည်းစေမယ် |
| **Pricing** | **Purchase price history keep** | COGS calculation မှန်ကန်စေမယ် (weighted average or FIFO စတင်တော့ Weighted Average သင့်တော်) |
| **Licensing** | **Signed key + online optional + offline grace** | Standalone အတွက် လက်တွေ့ကျ၊ Crack ရန် ခက်ခဲစေ |
| **Config** | **Feature flags by plan/license** | UI မှာ အပို module ပြခြင်း/မပြခြင်းကို အလွယ်ထိန်းနိုင် |
| **Migrations** | **Prisma Migrate/Drizzle Kit** + seed scripts | Version control လုပ်ရလွယ် |
| **Security** | **RBAC + tenant scoping everywhere + CSRF/Rate limit** | Cross-tenant leak မဖြစ်အောင် အရေးအကြီးဆုံး |

## 11) Open Questions (သေချာစေချင်သော အချက်များ)

Plan ကို Implementation အတွက် ပြီးပြည့်စုံစေရန် အောက်ပါများကို သေချာဖြေကြားပေးပါ။

| Question | Options/Notes |
|---|---|
| **Currency** | ဘယ်ငွေကြေး သုံးမလဲ? (MMK, THB, USD) |
| **Language** | မြန်မာ/အင်္ဂလိပ် သို့မဟုတ် နှစ်မျိုးလုံး? |
| **Receipt** | Thermal printer (58mm/80mm) အဓိကလား? Template customize လုပ်ချင်လား? |
| **COGS Method** | **Weighted Average** (လွယ်) vs **FIFO** (ပိုတိကျ) ဘယ်ဟာ စတင်လိုသလဲ? |
| **License Offline** | Internet မရှိဘဲ အသုံးပြုခွင့်ရှိမလား? (ရှိရင် grace period ဘယ်လောက်?) |
| **Local Billing** | မြန်မာနိုင်ငံအတွက် Payment Gateway ဘယ်ဟာ သုံးစွဲနိုင်မလဲ? (KBZPay, AYA Pay, WavePay) |
| **Tax** | Service Charge / VAT / အခြား အခွန်တွေ ပါမလား? Calculation နည်းလည်း? |
| **Hardware ID** | License ကို Machine တစ်လုံးတည်းနဲ့ ချိတ်ချင်လား? |
| **KDS Priority** | KDS ကို MVP မှာ ထည့်မလား ထားမလား? |

## 12) Suggested First Action

၁) **Repo Structure တည်ဆောက်** - Monorepo + Docker Compose  
၂) **DB Schema Design** - Tenants/Users/Roles + Units + Items + Orders အခြေခံ  
၃) **Auth + Tenant Middleware** - `APP_MODE` အပေါ်မူတည်ပြီး Scoping  
၄) **POS Minimal Flow** - Order -> Payment -> Receipt (အောင်မြင်မှတဆင့် ကျယ်ပြန့်အောင် တိုးချဲ့)

**အကြံပြုချက်:** အစပိုင်းမှာ **"Config-driven"** (standalone/saas toggle) အဖြစ်စတင်ပြီး၊ Billing/License ကို Phase 4 မှာသာ အာရုံစိုက်ပါ။ အဓိက Focus က **Sales + Purchase + Stock + P&L တိကျမှု** ဖြစ်ရမယ်။
