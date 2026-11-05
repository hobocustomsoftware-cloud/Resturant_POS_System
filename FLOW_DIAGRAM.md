# Restaurant POS System - Flow Diagram

## 1. System Architecture Overview

```mermaid
graph TB
    subgraph "Client Apps"
        WEB[Web App - React/Vite]
        MOB[Mobile App - React Native]
        DESK[Desktop App - Electron]
    end
    
    subgraph "Backend"
        API[Django REST API]
        WS[WebSocket - Channels]
        AUTH[JWT Auth]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL)]
        REDIS[(Redis)]
        MEDIA[/Media Storage/]
    end
    
    WEB --> API
    MOB --> API
    DESK --> WEB
    API --> DB
    API --> REDIS
    WS --> REDIS
    API --> MEDIA
```

## 2. User Authentication Flow

```mermaid
sequenceDiagram
    participant User
    participant App
    participant API
    participant DB
    
    User->>App: Login (username/password)
    App->>API: POST /api/auth/login/
    API->>DB: Validate credentials
    DB-->>API: User data + tenant
    API-->>App: JWT access + refresh tokens
    App->>App: Store tokens
    App->>API: Requests with Bearer token
```

## 3. POS Order Flow

```mermaid
flowchart TD
    A[Open POS] --> B[Select Order Type<br/>Dine-in/Takeaway/Delivery]
    B --> C[Select Table if Dine-in]
    C --> D[Browse Menu by Category]
    D --> E[Add Items to Cart]
    E --> F{Hold Order?}
    F -->|Yes| G[Save to Hold]
    F -->|No| H[Proceed to Payment]
    G --> D
    H --> I[Apply Discount/Charges]
    I --> J[Select Payment Method]
    J --> K[Complete Payment]
    K --> L[Create Order via API]
    L --> M[Deduct Stock]
    M --> N[Send to KDS]
    N --> O[Print Receipt]
```

## 4. Kitchen Display System (KDS) Flow

```mermaid
sequenceDiagram
    participant POS
    participant API
    participant WS
    participant KDS
    participant Kitchen
    
    POS->>API: Create Order (POST /api/sales/orders/)
    API->>DB: Save Order (status: pending)
    API->>WS: Broadcast new order
    WS->>KDS: Real-time notification
    Kitchen->>KDS: Mark as Preparing
    KDS->>API: PUT /api/kds/orders/{id}/mark_preparing/
    API->>WS: Broadcast status update
    WS->>POS: Status update
    Kitchen->>KDS: Mark as Ready
    KDS->>API: PUT /api/kds/orders/{id}/mark_ready/
    API->>WS: Broadcast ready
    WS->>POS: Notify order ready
```

## 5. Purchase & Inventory Flow

```mermaid
flowchart TD
    A[Create Purchase Order] --> B[Add Items with Quantity/Price]
    B --> C[Save as Pending]
    C --> D[Receive Goods - GRN]
    D --> E[API: POST /api/purchases/{id}/receive/]
    E --> F[Increase Stock]
    F --> G[Create Stock Movement]
    G --> H[Update Purchase Status: received]
    H --> I[Stock Available for Sales]
```

## 6. Daily Operations Flow

```mermaid
flowchart TD
    A[Start of Day] --> B[Daily Opening<br/>Set Opening Cash]
    B --> C[Day Session Active]
    C --> D[Process Sales]
    C --> E[Record Purchases]
    C --> F[Record Expenses]
    D --> G[Stock Auto-Deducted]
    E --> H[Stock Auto-Increased]
    G --> I[End of Day]
    H --> I
    F --> I
    I --> J[Close Shop<br/>Stock Reconciliation]
    J --> K[Count Actual vs System Stock]
    K --> L[Enter Reasons for Differences]
    L --> M[Cash Count]
    M --> N[Generate Daily Report]
    N --> O[Day Session Closed]
```

## 7. License & Subscription Flow

```mermaid
flowchart TD
    A[New Tenant] --> B{Mode?}
    B -->|Standalone| C[Auto-generate Trial License<br/>37 days]
    B -->|SaaS| D[Auto-create Trial Subscription<br/>37 days]
    C --> E[Access Granted]
    D --> E
    E --> F{Trial Expired?}
    F -->|No| G[Normal Usage]
    F -->|Yes| H[Block Access<br/>Show Payment Required]
    H --> I[User Submits Payment<br/>Manual/Bank Transfer]
    I --> J[Admin Reviews Payment]
    J --> K{Approved?}
    K -->|Yes| L[Activate License/Subscription]
    K -->|No| M[Reject with Notes]
    L --> E
```

## 8. Notification Flow

```mermaid
sequenceDiagram
    participant Event
    participant Service
    participant WS
    participant Client
    
    Event->>Service: Trigger (New Order/KDS Update)
    Service->>Service: Create Notification in DB
    Service->>WS: Broadcast to tenant/user group
    WS->>Client: Push real-time notification
    Client->>Client: Show toast/bell update
```

## 9. Multi-Tenant Architecture

```mermaid
flowchart LR
    A[Request] --> B[TenantMiddleware]
    B --> C{Identify Tenant}
    C --> D[From User/Session/Header]
    D --> E[Set request.tenant]
    E --> F[Apply Tenant Filter]
    F --> G[All Queries Filtered by tenant_id]
    G --> H[Data Isolation]
```

## Platform Support

| Platform | Technology | Status | Notes |
|----------|-----------|--------|-------|
| Web | React + Vite + TypeScript | ✅ Complete | Primary platform |
| Desktop | Electron | ✅ Complete | Native GUI, Menu, Tray, EXE build ready |
| Mobile | React Native + Expo | ✅ Complete | APK build ready, Scanner, Notifications |
| Tablet | Responsive Web | ✅ Complete | Works via web app |

## Key Features Summary

- **POS**: Order management, tables, cart, payments
- **Kitchen Display**: Real-time order tracking
- **Inventory**: Stock tracking, purchases, movements
- **Reports**: Sales, P&L, daily/monthly summaries
- **Multi-tenant**: SaaS + Standalone modes
- **Billing**: Trial, manual payments, license management
- **Notifications**: Real-time push notifications
- **Backup**: System & per-tenant backups
- **Modern UI**: Clean, responsive design
