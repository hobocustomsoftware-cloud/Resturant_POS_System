# Restaurant POS - UTA Style Implementation Plan

Reference: https://pos.hobocustomsoftware.com

## Goal
Build Restaurant POS inspired by UTA POS. Support both Standalone and Multi-Tenant SaaS (configurable), Docker deployable, with subscription/license key monetization. Complete the existing Django scaffold.

## Decisions
- Frontend: API-first complete, then Next.js UI
- Receipt: HTML + ESC/POS ready
- Currency: MMK
- License: offline signed JWT
- Deploy: Docker

## Current State
Scaffold exists (models/core/middleware). Missing: serializers/views/urls/permissions, auth, business logic, migrations, reports, billing enforcement, KDS.

## Phases
1. Core Infra (permissions, utils, mixins, middleware)
2. Migrations & Seeds
3. Auth & Users/Roles
4. Catalog
5. Purchases & Inventory (stock movements)
6. Sales/POS (tables, orders, payments, stock deduction incl combos)
7. Expenses/Reports/Billing/License (P&L with COGS)
8. KDS (Channels)
9. Frontend scaffold

## Next Action
Implementation required. Switch to implementation agent.
