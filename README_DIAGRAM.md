# Architecture Diagram

![Restaurant POS System Architecture](diagram.svg)

## Overview
- **Multi-platform**: Web, Mobile (Android/iOS), Desktop (Windows/Mac/Linux)
- **Backend**: Django REST API with JWT authentication
- **Real-time**: WebSocket via Django Channels for KDS notifications
- **Database**: PostgreSQL with Redis caching
- **Features**: POS, Kitchen Display, Inventory, Reports, Billing with 37-day trial
- **Payment**: Manual payment (Bank/KPay/Wave) with admin approval
- **Multi-tenant**: Support for Standalone and SaaS modes
