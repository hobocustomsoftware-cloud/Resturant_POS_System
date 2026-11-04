# Restaurant POS - UTA Style Plan (Simple, Practical)

Reference: https://pos.hobocustomsoftware.com

## Goal
Simple, easy-to-use POS matching UTA flow. Focus on stock checking/reconciliation, daily operations.

## Core Requirements
- POS: categories, items, cart, order type (Dine In/Take Away/Delivery), table, hold/resume
- Tables: visual layout by area
- Payment: cash/card, discount, service charge/tax, change
- Daily: Opening balance -> Purchases (add stock) -> Sales (deduct stock) -> Close shop with stock check/reconciliation
- Purchases/GRN with stock update
- Expenses by group (Bar, Kitchen, BBQ, General)
- Reports: Daily/Monthly, P&L with COGS
- Custom React Admin (replace Django admin)
- KDS realtime
- Multi-branch, Standalone/SaaS ready

## Current State
Scaffold done (models/APIs/React routes/UI). Need to make it practical and easy for normal users.

## Key Focus Areas
1. **POS** - Clean layout, fast order taking, hold/resume
2. **Daily Operations** - Simple opening/close flow, stock reconciliation checklist
3. **Stock Check** - Compare system vs actual, enter counted qty, show difference, require reason if adjusted
4. **Reports** - Clear daily summary, expense breakdown
5. **Admin** - Simple CRUD, replace Django admin

## Implementation Plan
1. **POS UI** - UTA-style clean layout, order type, tables, hold/resume, payment modal
2. **Tables UI** - Visual grid by area/floor
3. **Payment Modal** - Amount, discount, change, methods
4. **Daily Opening** - Set opening cash, show previous day closing
5. **Daily Purchases** - Quick GRN entry, auto update stock
6. **Close Shop** - Stock reconciliation form (item, system qty, actual qty, diff, reason), cash count vs expected
7. **Custom React Admin** - Full CRUD for products/categories/purchases/expenses/stock/users/roles/settings
8. **Reports** - Daily summary + monthly + P&L
9. **KDS** - Realtime status updates

## Next Steps
Implement UTA-style simple POS + daily stock reconciliation flow first.
