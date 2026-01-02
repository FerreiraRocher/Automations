# Restaurant QR Menu & Ordering Platform - Detailed Analysis & Implementation Plan

## Executive Summary

A white-label SaaS platform enabling restaurants to create digital menus accessible via QR codes, with integrated online ordering, payment processing, and kitchen management. This solution targets restaurants, cafes, food trucks, and hospitality businesses seeking to modernize their customer experience.

---

## 1. Market Analysis

### 1.1 Market Size & Opportunity

| Metric | Value | Source |
|--------|-------|--------|
| Global restaurant count | 15+ million | Industry reports |
| US restaurants | 1+ million | NRA |
| QR menu adoption (post-2020) | 52% | Technomic |
| Digital ordering growth | 23% CAGR | Mordor Intelligence |
| TAM (Digital ordering) | $28B by 2028 | Research & Markets |

### 1.2 Target Market Segments

| Segment | Size (US) | Pain Points | Price Sensitivity |
|---------|-----------|-------------|-------------------|
| Quick Service Restaurants | 350,000+ | Order accuracy, speed, labor costs | Medium |
| Full-Service Restaurants | 250,000+ | Menu updates, table turnover | Low |
| Cafes & Coffee Shops | 200,000+ | Order queue management | Medium-High |
| Food Trucks | 35,000+ | Limited POS options, menu visibility | High |
| Hotels (F&B) | 60,000+ | Room service modernization | Low |
| Ghost Kitchens | 10,000+ | Multi-brand menus | Low |

### 1.3 Competitive Landscape

| Competitor | Pricing | Strengths | Weaknesses |
|------------|---------|-----------|------------|
| Toast | $69-165+/mo | Full POS, strong brand | Expensive, complex |
| Square for Restaurants | $60+/mo | Easy payments | Limited QR features |
| Grubhub/DoorDash | Commission | Large audience | High fees (15-30%) |
| TouchBistro | $69+/mo | iPad-based | Limited customization |
| GloriaFood | Free-$29/mo | Free tier | Basic features |
| me&u | Custom | Table ordering focus | Not SMB-focused |
| Ordermark | Usage-based | Multi-platform | Delivery focus only |

### 1.4 Market Trends

1. **Contactless dining** - Permanent shift post-pandemic
2. **Labor shortage** - Restaurants need automation
3. **Direct ordering** - Avoiding third-party commissions
4. **Personalization** - Allergen filters, recommendations
5. **Sustainability** - Paper menu elimination

---

## 2. Product Vision & Features

### 2.1 Core Value Proposition

> "Turn your menu into a revenue engine. Beautiful digital menus, seamless ordering, zero commissions."

### 2.2 Product Modules

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        RESTAURANT QR MENU PLATFORM                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   MENU BUILDER  │  │  ORDER MANAGER  │  │ KITCHEN DISPLAY │             │
│  │   ───────────── │  │  ────────────── │  │  ────────────── │             │
│  │ • Drag-drop     │  │ • Real-time     │  │ • Order queue   │             │
│  │ • Multi-language│  │ • Status        │  │ • Prep timing   │             │
│  │ • Photos/videos │  │ • History       │  │ • Item routing  │             │
│  │ • Modifiers     │  │ • Analytics     │  │ • Bump bar      │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │    PAYMENTS     │  │   QR CODES      │  │   ANALYTICS     │             │
│  │   ───────────── │  │  ────────────── │  │  ────────────── │             │
│  │ • Stripe/Square │  │ • Table-specific│  │ • Sales reports │             │
│  │ • Apple/Google  │  │ • Takeaway/Dine │  │ • Popular items │             │
│  │ • Split bills   │  │ • Custom design │  │ • Peak hours    │             │
│  │ • Tip handling  │  │ • Print/download│  │ • Customer data │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   INTEGRATIONS  │  │  RESERVATIONS   │  │   WHITE-LABEL   │             │
│  │   ───────────── │  │  ────────────── │  │  ────────────── │             │
│  │ • Toast POS     │  │ • Table booking │  │ • Custom domain │             │
│  │ • Square        │  │ • Waitlist      │  │ • Branding      │             │
│  │ • Clover        │  │ • SMS alerts    │  │ • Mobile app    │             │
│  │ • Delivery apps │  │ • Deposits      │  │ • Reseller API  │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Feature Matrix by Phase

#### Phase 1: MVP (Months 1-3)

| Feature | Priority | User Story | Acceptance Criteria |
|---------|----------|------------|---------------------|
| Menu creation | P0 | As a restaurant owner, I want to create a digital menu | Can add categories, items, prices, descriptions |
| Menu customization | P0 | As a restaurant, I want my menu to match my brand | Logo, colors, fonts configurable |
| QR code generation | P0 | As a restaurant, I want QR codes for each table | Unique codes per table, downloadable |
| Customer menu view | P0 | As a customer, I want to view the menu on my phone | Mobile-responsive, fast loading |
| Item availability | P0 | As a restaurant, I want to mark items unavailable | Toggle on/off, real-time update |
| Basic ordering | P0 | As a customer, I want to place orders from my phone | Add to cart, submit order |
| Order notifications | P0 | As a restaurant, I want to receive new orders | Push/sound notification |
| Admin dashboard | P0 | As a restaurant, I want to manage everything | Orders, menu, settings in one place |

#### Phase 2: Core Features (Months 4-6)

| Feature | Priority | User Story | Acceptance Criteria |
|---------|----------|------------|---------------------|
| Payment processing | P1 | As a customer, I want to pay on my phone | Card, Apple Pay, Google Pay |
| Item modifiers | P1 | As a customer, I want to customize my order | Size, add-ons, special requests |
| Multi-language | P1 | As a tourist, I want to read the menu in my language | Auto-detect + manual selection |
| Kitchen display | P1 | As a chef, I want to see incoming orders | Order queue, status updates |
| Order history | P1 | As a restaurant, I want to see past orders | Searchable, filterable |
| Customer accounts | P1 | As a repeat customer, I want to save favorites | Optional registration |
| Allergen filters | P1 | As someone with allergies, I want to filter items | Tags for common allergens |
| Scheduled ordering | P1 | As a customer, I want to order for later | Select pickup/delivery time |

#### Phase 3: Growth (Months 7-12)

| Feature | Priority | User Story | Acceptance Criteria |
|---------|----------|------------|---------------------|
| POS integration | P2 | As a restaurant with Toast, I want orders synced | Two-way sync with major POS |
| Delivery integration | P2 | As a restaurant, I want to offer delivery | DoorDash Drive, Uber Direct |
| Table management | P2 | As a host, I want to see table status | Table map, occupancy, orders |
| Loyalty program | P2 | As a restaurant, I want to reward regulars | Points, rewards, tiers |
| Staff management | P2 | As a manager, I want to track server performance | Orders per server, ratings |
| Inventory tracking | P2 | As a restaurant, I want stock alerts | Low stock warnings, 86'd items |
| Multi-location | P2 | As a chain, I want centralized management | Multiple venues, shared menus |
| White-label reseller | P2 | As an agency, I want to resell | API access, custom branding |

### 2.4 User Personas

#### Persona 1: Sofia - Independent Restaurant Owner
- **Age:** 38
- **Business:** Mediterranean restaurant, 60 seats, 8 staff
- **Tech Savvy:** Medium
- **Current Setup:** Paper menus, Toast POS, phone orders
- **Pain Points:**
  - Menu printing costs $200/month
  - 20 min average to update specials
  - Servers waste time explaining menu
  - Third-party apps take 25% commission
- **Goals:**
  - Reduce operational costs
  - Increase direct orders
  - Modernize customer experience
- **Budget:** $50-150/month

#### Persona 2: Marcus - Food Truck Operator
- **Age:** 29
- **Business:** Gourmet burger food truck, 2 staff
- **Tech Savvy:** High
- **Current Setup:** Chalkboard menu, Square POS
- **Pain Points:**
  - Menu hard to see from queue
  - Long lines, lost customers
  - No pre-ordering capability
  - Weather damages paper menus
- **Goals:**
  - Speed up ordering
  - Reduce queue abandonment
  - Accept pre-orders for pickup
- **Budget:** $25-75/month

#### Persona 3: Jennifer - Multi-Location Cafe Manager
- **Age:** 45
- **Business:** 5 cafe locations, 35 staff total
- **Tech Savvy:** Medium
- **Current Setup:** Inconsistent across locations
- **Pain Points:**
  - Menu inconsistency between locations
  - No visibility into location performance
  - Difficult to roll out new items
  - Training staff on menu changes
- **Goals:**
  - Centralized menu management
  - Consistent customer experience
  - Better analytics
- **Budget:** $200-500/month (all locations)

### 2.5 Customer Journey Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DINE-IN CUSTOMER JOURNEY                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ARRIVAL        SCAN QR         BROWSE           ORDER           PAY        │
│     │              │              │               │              │          │
│     ▼              ▼              ▼               ▼              ▼          │
│  ┌─────┐       ┌─────┐       ┌─────┐         ┌─────┐        ┌─────┐        │
│  │Seated│──────│Scan │──────│View │─────────│Build │───────│Pay  │        │
│  │at   │       │table│       │menu │         │cart  │       │bill │        │
│  │table│       │code │       │items│         │submit│       │     │        │
│  └─────┘       └─────┘       └─────┘         └─────┘        └─────┘        │
│     │              │              │               │              │          │
│  No wait      <2 seconds     Filter,          Modifiers,      Split,       │
│  for menu     to load        search,          notes,          tip,         │
│               📱             photos           quantity        Apple Pay    │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TAKEAWAY CUSTOMER JOURNEY                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DISCOVER       BROWSE         ORDER          NOTIFY         PICKUP         │
│     │              │              │               │              │          │
│     ▼              ▼              ▼               ▼              ▼          │
│  ┌─────┐       ┌─────┐       ┌─────┐         ┌─────┐        ┌─────┐        │
│  │Scan │──────│View │──────│Submit│─────────│Receive│──────│Pickup│        │
│  │flyer│       │menu │       │order│         │"ready"│       │food │        │
│  │code │       │     │       │pay  │         │SMS    │       │     │        │
│  └─────┘       └─────┘       └─────┘         └─────┘        └─────┘        │
│     │              │              │               │              │          │
│  From flyer    Schedule      Prepay          Real-time       Show          │
│  or window     pickup time   + tip           tracking        order #       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Technical Architecture

### 3.1 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT APPS                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  Customer    │  │   Admin      │  │   Kitchen    │  │   Kiosk      │    │
│  │  Menu Web    │  │   Dashboard  │  │   Display    │  │   Mode       │    │
│  │  (PWA)       │  │   (React)    │  │   (React)    │  │   (React)    │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                 │                 │             │
│         └────────────────┬┴─────────────────┴────────────────┘             │
│                          │                                                   │
└──────────────────────────┼───────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CDN + LOAD BALANCER                                │
│                      (CloudFlare / AWS CloudFront)                           │
└─────────────────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              API GATEWAY                                     │
│                    Rate Limiting │ Auth │ Caching │ Routing                  │
└─────────────────────────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│   MENU SERVICE   │ │  ORDER SERVICE   │ │ PAYMENT SERVICE  │
│  ──────────────  │ │  ──────────────  │ │  ──────────────  │
│ • CRUD menus     │ │ • Cart management│ │ • Stripe         │
│ • Categories     │ │ • Order lifecycle│ │ • Square         │
│ • Items          │ │ • Status updates │ │ • Refunds        │
│ • Modifiers      │ │ • Notifications  │ │ • Tips           │
│ • Availability   │ │ • Kitchen sync   │ │ • Split payments │
└────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
         │                    │                    │
         │    ┌───────────────┼───────────────┐    │
         │    │               │               │    │
         ▼    ▼               ▼               ▼    ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ RESTAURANT SVC   │ │ NOTIFICATION SVC │ │  ANALYTICS SVC   │
│  ──────────────  │ │  ──────────────  │ │  ──────────────  │
│ • Settings       │ │ • Push           │ │ • Order metrics  │
│ • Staff          │ │ • SMS            │ │ • Item popularity│
│ • Tables         │ │ • Email          │ │ • Revenue        │
│ • Hours          │ │ • WebSocket      │ │ • Trends         │
│ • Integrations   │ │ • Webhooks       │ │ • Customer data  │
└────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MESSAGE QUEUE                                      │
│                    (Redis Streams / RabbitMQ / SQS)                          │
│         order.created │ order.updated │ payment.received │ etc.             │
└─────────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATA LAYER                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   PostgreSQL     │  │      Redis       │  │   S3 / Cloudinary│          │
│  │   (Primary DB)   │  │     (Cache +     │  │   (Images/Assets)│          │
│  │                  │  │     Real-time)   │  │                  │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐                                 │
│  │   ClickHouse     │  │  Elasticsearch   │                                 │
│  │   (Analytics)    │  │   (Menu Search)  │                                 │
│  └──────────────────┘  └──────────────────┘                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        EXTERNAL INTEGRATIONS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │   Stripe    │ │   Square    │ │  Toast POS  │ │   Twilio    │           │
│  │  (Payments) │ │  (Payments) │ │ (POS Sync)  │ │    (SMS)    │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │  DoorDash   │ │   Google    │ │  SendGrid   │ │   Clover    │           │
│  │   Drive     │ │  Translate  │ │   (Email)   │ │    (POS)    │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Technology Stack

#### Backend
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Framework | Node.js + Fastify | Performance, simplicity |
| Language | TypeScript | Type safety |
| Database | PostgreSQL (Supabase) | Real-time, hosted |
| Cache | Redis | Session, real-time pub/sub |
| Queue | BullMQ | Job processing |
| Search | Meilisearch | Fast menu search |
| Storage | Cloudinary | Image optimization CDN |

#### Frontend
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Customer Menu | Next.js 14 (App Router) | SSR, performance |
| Admin Dashboard | Next.js 14 | Shared codebase |
| Kitchen Display | Next.js + WebSockets | Real-time updates |
| UI Library | Tailwind + Radix UI | Accessibility, speed |
| State | Zustand + React Query | Simple, cache-first |
| PWA | next-pwa | Offline capability |

#### Infrastructure
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Hosting | Vercel (frontend) | Easy deployment |
| API Hosting | Railway / Fly.io | Container support |
| Database | Supabase | Managed Postgres |
| CDN | CloudFlare | Edge caching |
| Monitoring | Sentry + Vercel Analytics | Error tracking |

### 3.3 Database Schema

```sql
-- Core Restaurant Tables

CREATE TABLE restaurants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    logo_url TEXT,
    cover_image_url TEXT,
    address JSONB,
    phone VARCHAR(20),
    email VARCHAR(255),
    timezone VARCHAR(50) DEFAULT 'America/New_York',
    currency VARCHAR(3) DEFAULT 'USD',
    tax_rate DECIMAL(5,4) DEFAULT 0.0825,
    service_charge_rate DECIMAL(5,4) DEFAULT 0,
    settings JSONB DEFAULT '{}',
    theme JSONB DEFAULT '{"primaryColor": "#000000"}',
    subscription_tier VARCHAR(20) DEFAULT 'starter',
    subscription_status VARCHAR(20) DEFAULT 'active',
    stripe_account_id VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE restaurant_hours (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    day_of_week INTEGER NOT NULL, -- 0=Sunday
    open_time TIME,
    close_time TIME,
    is_closed BOOLEAN DEFAULT false,
    UNIQUE(restaurant_id, day_of_week)
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    role VARCHAR(20) DEFAULT 'staff', -- owner, manager, staff
    pin_code VARCHAR(6), -- for POS login
    is_active BOOLEAN DEFAULT true,
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Menu Tables

CREATE TABLE menu_categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url TEXT,
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    available_start_time TIME,
    available_end_time TIME,
    available_days INTEGER[] DEFAULT '{0,1,2,3,4,5,6}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE menu_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    category_id UUID REFERENCES menu_categories(id) ON DELETE SET NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    compare_at_price DECIMAL(10,2), -- for showing discounts
    image_url TEXT,
    images TEXT[], -- additional images
    prep_time_minutes INTEGER,
    calories INTEGER,
    allergens TEXT[],
    dietary_tags TEXT[], -- vegan, vegetarian, gluten-free
    spicy_level INTEGER, -- 0-3
    is_featured BOOLEAN DEFAULT false,
    is_popular BOOLEAN DEFAULT false,
    is_available BOOLEAN DEFAULT true,
    display_order INTEGER DEFAULT 0,
    sku VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE modifier_groups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL, -- e.g., "Size", "Toppings"
    selection_type VARCHAR(20) DEFAULT 'single', -- single, multiple
    min_selections INTEGER DEFAULT 0,
    max_selections INTEGER,
    is_required BOOLEAN DEFAULT false,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE modifier_options (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    modifier_group_id UUID REFERENCES modifier_groups(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    price_adjustment DECIMAL(10,2) DEFAULT 0,
    is_default BOOLEAN DEFAULT false,
    is_available BOOLEAN DEFAULT true,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE item_modifier_groups (
    item_id UUID REFERENCES menu_items(id) ON DELETE CASCADE,
    modifier_group_id UUID REFERENCES modifier_groups(id) ON DELETE CASCADE,
    display_order INTEGER DEFAULT 0,
    PRIMARY KEY (item_id, modifier_group_id)
);

-- Menu Translations

CREATE TABLE menu_translations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type VARCHAR(20) NOT NULL, -- category, item, modifier_group, modifier_option
    entity_id UUID NOT NULL,
    language_code VARCHAR(5) NOT NULL, -- en, es, zh, etc.
    field VARCHAR(50) NOT NULL, -- name, description
    value TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_type, entity_id, language_code, field)
);

-- Table & QR Management

CREATE TABLE tables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id) ON DELETE CASCADE,
    table_number VARCHAR(20) NOT NULL,
    name VARCHAR(50), -- e.g., "Patio 1", "Bar Seat 5"
    capacity INTEGER DEFAULT 4,
    section VARCHAR(50), -- indoor, outdoor, bar
    qr_code_id VARCHAR(100) UNIQUE,
    qr_code_url TEXT,
    status VARCHAR(20) DEFAULT 'available', -- available, occupied, reserved
    current_order_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(restaurant_id, table_number)
);

-- Order Tables

CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    table_id UUID REFERENCES tables(id),
    order_number VARCHAR(20) NOT NULL,
    order_type VARCHAR(20) NOT NULL, -- dine_in, takeaway, delivery
    status VARCHAR(20) DEFAULT 'pending',
    -- pending, confirmed, preparing, ready, completed, cancelled
    customer_name VARCHAR(100),
    customer_phone VARCHAR(20),
    customer_email VARCHAR(255),

    -- Pricing
    subtotal DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) DEFAULT 0,
    service_charge DECIMAL(10,2) DEFAULT 0,
    tip_amount DECIMAL(10,2) DEFAULT 0,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    total DECIMAL(10,2) NOT NULL,

    -- Timing
    scheduled_at TIMESTAMPTZ, -- for future orders
    confirmed_at TIMESTAMPTZ,
    preparing_at TIMESTAMPTZ,
    ready_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    estimated_ready_at TIMESTAMPTZ,

    -- Payment
    payment_status VARCHAR(20) DEFAULT 'unpaid',
    payment_method VARCHAR(20),
    payment_intent_id VARCHAR(100),

    -- Metadata
    notes TEXT,
    source VARCHAR(20) DEFAULT 'qr_menu', -- qr_menu, kiosk, pos, website
    device_info JSONB,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id UUID REFERENCES menu_items(id),
    name VARCHAR(255) NOT NULL, -- snapshot of item name
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    modifiers JSONB DEFAULT '[]', -- snapshot of selected modifiers
    special_instructions TEXT,
    status VARCHAR(20) DEFAULT 'pending', -- pending, preparing, ready
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Analytics & Tracking

CREATE TABLE page_views (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    table_id UUID REFERENCES tables(id),
    session_id VARCHAR(100),
    page VARCHAR(100), -- menu, category, item, cart, checkout
    referrer TEXT,
    user_agent TEXT,
    ip_address INET,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE item_views (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    menu_item_id UUID REFERENCES menu_items(id),
    session_id VARCHAR(100),
    duration_seconds INTEGER,
    added_to_cart BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Integrations

CREATE TABLE pos_integrations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    provider VARCHAR(50) NOT NULL, -- toast, square, clover
    credentials JSONB, -- encrypted
    settings JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    last_sync_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE delivery_integrations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    restaurant_id UUID REFERENCES restaurants(id),
    provider VARCHAR(50) NOT NULL, -- doordash_drive, uber_direct
    credentials JSONB, -- encrypted
    settings JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes

CREATE INDEX idx_menu_items_restaurant ON menu_items(restaurant_id);
CREATE INDEX idx_menu_items_category ON menu_items(category_id);
CREATE INDEX idx_orders_restaurant ON orders(restaurant_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created ON orders(created_at);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_tables_restaurant ON tables(restaurant_id);
CREATE INDEX idx_page_views_restaurant_date ON page_views(restaurant_id, created_at);

-- Full text search for menu items
CREATE INDEX idx_menu_items_search ON menu_items
USING gin(to_tsvector('english', name || ' ' || COALESCE(description, '')));
```

### 3.4 API Design

```yaml
# Authentication
POST   /api/v1/auth/register              # Restaurant signup
POST   /api/v1/auth/login                 # Admin login
POST   /api/v1/auth/pin-login             # Staff PIN login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh

# Restaurants
GET    /api/v1/restaurants/:id            # Get restaurant info
PUT    /api/v1/restaurants/:id            # Update restaurant
GET    /api/v1/restaurants/:id/settings
PUT    /api/v1/restaurants/:id/settings
PUT    /api/v1/restaurants/:id/theme
GET    /api/v1/restaurants/:id/hours
PUT    /api/v1/restaurants/:id/hours

# Menu Categories
GET    /api/v1/restaurants/:id/categories
POST   /api/v1/restaurants/:id/categories
GET    /api/v1/categories/:id
PUT    /api/v1/categories/:id
DELETE /api/v1/categories/:id
PUT    /api/v1/categories/reorder

# Menu Items
GET    /api/v1/restaurants/:id/items
POST   /api/v1/restaurants/:id/items
GET    /api/v1/items/:id
PUT    /api/v1/items/:id
DELETE /api/v1/items/:id
PUT    /api/v1/items/:id/availability
PUT    /api/v1/items/bulk-availability
POST   /api/v1/items/:id/image

# Modifiers
GET    /api/v1/restaurants/:id/modifier-groups
POST   /api/v1/restaurants/:id/modifier-groups
PUT    /api/v1/modifier-groups/:id
DELETE /api/v1/modifier-groups/:id
POST   /api/v1/modifier-groups/:id/options
PUT    /api/v1/modifier-options/:id
DELETE /api/v1/modifier-options/:id

# Tables & QR Codes
GET    /api/v1/restaurants/:id/tables
POST   /api/v1/restaurants/:id/tables
PUT    /api/v1/tables/:id
DELETE /api/v1/tables/:id
GET    /api/v1/tables/:id/qr-code
POST   /api/v1/restaurants/:id/tables/bulk
GET    /api/v1/restaurants/:id/qr-codes/download

# Public Menu (Customer-facing)
GET    /api/v1/menu/:restaurantSlug                    # Full menu
GET    /api/v1/menu/:restaurantSlug/categories/:id     # Category with items
GET    /api/v1/menu/:restaurantSlug/items/:id          # Item detail
GET    /api/v1/menu/:restaurantSlug/search?q=          # Search items

# Orders
POST   /api/v1/orders                     # Create order (customer)
GET    /api/v1/orders/:id                 # Get order details
PUT    /api/v1/orders/:id/status          # Update status (staff)
POST   /api/v1/orders/:id/items           # Add items to order
DELETE /api/v1/orders/:id/items/:itemId   # Remove item
GET    /api/v1/restaurants/:id/orders     # List orders (admin)
GET    /api/v1/restaurants/:id/orders/live # Real-time orders

# Payments
POST   /api/v1/orders/:id/payment-intent  # Create Stripe payment intent
POST   /api/v1/orders/:id/confirm-payment # Confirm payment
POST   /api/v1/orders/:id/refund          # Process refund
GET    /api/v1/orders/:id/receipt         # Get receipt

# Kitchen Display
GET    /api/v1/restaurants/:id/kitchen/orders  # Active orders for kitchen
PUT    /api/v1/order-items/:id/status          # Update item status
POST   /api/v1/orders/:id/bump                 # Bump entire order

# Analytics
GET    /api/v1/restaurants/:id/analytics/overview
GET    /api/v1/restaurants/:id/analytics/sales
GET    /api/v1/restaurants/:id/analytics/items
GET    /api/v1/restaurants/:id/analytics/hourly
GET    /api/v1/restaurants/:id/analytics/customers

# Integrations
GET    /api/v1/restaurants/:id/integrations
POST   /api/v1/restaurants/:id/integrations/:provider
PUT    /api/v1/integrations/:id
DELETE /api/v1/integrations/:id
POST   /api/v1/integrations/:id/sync

# Webhooks
POST   /api/v1/webhooks/stripe
POST   /api/v1/webhooks/square
POST   /api/v1/webhooks/toast
```

### 3.5 Real-time Architecture

```typescript
// WebSocket Events for Kitchen Display & Order Updates

// Server -> Client Events
interface ServerToClientEvents {
  'order:new': (order: Order) => void;
  'order:updated': (order: Order) => void;
  'order:cancelled': (orderId: string) => void;
  'item:status': (data: { orderId: string; itemId: string; status: string }) => void;
  'table:status': (data: { tableId: string; status: string }) => void;
}

// Client -> Server Events
interface ClientToServerEvents {
  'subscribe:restaurant': (restaurantId: string) => void;
  'subscribe:kitchen': (restaurantId: string) => void;
  'subscribe:table': (tableId: string) => void;
  'order:acknowledge': (orderId: string) => void;
  'item:update-status': (data: { itemId: string; status: string }) => void;
}

// Room Structure
// restaurant:{restaurantId} - All staff for restaurant
// kitchen:{restaurantId} - Kitchen display only
// table:{tableId} - Customer at specific table
```

---

## 4. Test-Driven Development (TDD) Approach

### 4.1 Testing Strategy

```
Testing Pyramid for QR Menu Platform
─────────────────────────────────────

                    ┌─────────┐
                   /   E2E    \         5%
                  /  Playwright \
                 ─────────────────
                /   Integration   \     25%
               / (Supertest/MSW)   \
              ─────────────────────────
             /       Unit Tests         \   70%
            /    (Vitest + Testing Lib)  \
           ───────────────────────────────
```

### 4.2 Unit Test Specifications

#### Menu Service Tests

```typescript
// tests/unit/services/menu.test.ts

describe('MenuService', () => {
  describe('getMenu', () => {
    it('should return full menu with categories and items', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      const category = await createTestCategory(restaurant.id, { name: 'Appetizers' });
      await createTestItem(restaurant.id, category.id, { name: 'Spring Rolls', price: 8.99 });
      await createTestItem(restaurant.id, category.id, { name: 'Soup', price: 6.99 });

      // Act
      const menu = await menuService.getFullMenu(restaurant.id);

      // Assert
      expect(menu.categories).toHaveLength(1);
      expect(menu.categories[0].name).toBe('Appetizers');
      expect(menu.categories[0].items).toHaveLength(2);
    });

    it('should exclude unavailable items by default', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      const category = await createTestCategory(restaurant.id);
      await createTestItem(restaurant.id, category.id, {
        name: 'Available',
        isAvailable: true
      });
      await createTestItem(restaurant.id, category.id, {
        name: 'Unavailable',
        isAvailable: false
      });

      // Act
      const menu = await menuService.getFullMenu(restaurant.id);

      // Assert
      expect(menu.categories[0].items).toHaveLength(1);
      expect(menu.categories[0].items[0].name).toBe('Available');
    });

    it('should respect category time availability', async () => {
      // Arrange
      jest.setSystemTime(new Date('2026-01-15T08:00:00')); // 8am
      const restaurant = await createTestRestaurant();
      await createTestCategory(restaurant.id, {
        name: 'Lunch',
        availableStartTime: '11:00',
        availableEndTime: '15:00'
      });
      await createTestCategory(restaurant.id, {
        name: 'Breakfast',
        availableStartTime: '06:00',
        availableEndTime: '11:00'
      });

      // Act
      const menu = await menuService.getFullMenu(restaurant.id);

      // Assert
      expect(menu.categories).toHaveLength(1);
      expect(menu.categories[0].name).toBe('Breakfast');
    });

    it('should include translations when language specified', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      const category = await createTestCategory(restaurant.id, { name: 'Drinks' });
      await createTestTranslation({
        entityType: 'category',
        entityId: category.id,
        languageCode: 'es',
        field: 'name',
        value: 'Bebidas'
      });

      // Act
      const menu = await menuService.getFullMenu(restaurant.id, { language: 'es' });

      // Assert
      expect(menu.categories[0].name).toBe('Bebidas');
    });
  });

  describe('searchItems', () => {
    it('should find items by name', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      await createTestItem(restaurant.id, null, { name: 'Margherita Pizza' });
      await createTestItem(restaurant.id, null, { name: 'Pepperoni Pizza' });
      await createTestItem(restaurant.id, null, { name: 'Caesar Salad' });

      // Act
      const results = await menuService.searchItems(restaurant.id, 'pizza');

      // Assert
      expect(results).toHaveLength(2);
      expect(results.every(r => r.name.toLowerCase().includes('pizza'))).toBe(true);
    });

    it('should filter by allergens', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      await createTestItem(restaurant.id, null, {
        name: 'Pasta',
        allergens: ['gluten', 'dairy']
      });
      await createTestItem(restaurant.id, null, {
        name: 'Salad',
        allergens: []
      });

      // Act
      const results = await menuService.searchItems(restaurant.id, '', {
        excludeAllergens: ['gluten']
      });

      // Assert
      expect(results).toHaveLength(1);
      expect(results[0].name).toBe('Salad');
    });

    it('should filter by dietary preferences', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      await createTestItem(restaurant.id, null, {
        name: 'Veggie Burger',
        dietaryTags: ['vegetarian']
      });
      await createTestItem(restaurant.id, null, {
        name: 'Beef Burger',
        dietaryTags: []
      });

      // Act
      const results = await menuService.searchItems(restaurant.id, '', {
        dietaryTags: ['vegetarian']
      });

      // Assert
      expect(results).toHaveLength(1);
      expect(results[0].name).toBe('Veggie Burger');
    });
  });

  describe('toggleItemAvailability', () => {
    it('should mark item as unavailable', async () => {
      // Arrange
      const item = await createTestItem(defaultRestaurantId, null, {
        isAvailable: true
      });

      // Act
      await menuService.setItemAvailability(item.id, false);

      // Assert
      const updated = await menuService.getItem(item.id);
      expect(updated.isAvailable).toBe(false);
    });

    it('should emit real-time update event', async () => {
      // Arrange
      const item = await createTestItem(defaultRestaurantId, null);
      const eventSpy = jest.spyOn(eventEmitter, 'emit');

      // Act
      await menuService.setItemAvailability(item.id, false);

      // Assert
      expect(eventSpy).toHaveBeenCalledWith('menu:item-updated', {
        restaurantId: defaultRestaurantId,
        itemId: item.id,
        changes: { isAvailable: false }
      });
    });
  });
});
```

#### Order Service Tests

```typescript
// tests/unit/services/order.test.ts

describe('OrderService', () => {
  describe('createOrder', () => {
    it('should create order with valid items', async () => {
      // Arrange
      const restaurant = await createTestRestaurant();
      const item1 = await createTestItem(restaurant.id, null, { price: 12.99 });
      const item2 = await createTestItem(restaurant.id, null, { price: 8.99 });

      const orderData = {
        restaurantId: restaurant.id,
        orderType: 'dine_in',
        tableId: 'table-123',
        items: [
          { menuItemId: item1.id, quantity: 2 },
          { menuItemId: item2.id, quantity: 1 }
        ]
      };

      // Act
      const order = await orderService.createOrder(orderData);

      // Assert
      expect(order.id).toBeDefined();
      expect(order.status).toBe('pending');
      expect(order.items).toHaveLength(2);
      expect(order.subtotal).toBe(34.97); // (12.99 * 2) + 8.99
    });

    it('should apply modifiers and calculate correct price', async () => {
      // Arrange
      const item = await createTestItem(defaultRestaurantId, null, { price: 10.00 });
      const modifierGroup = await createTestModifierGroup(defaultRestaurantId, {
        name: 'Size'
      });
      const largeModifier = await createTestModifierOption(modifierGroup.id, {
        name: 'Large',
        priceAdjustment: 2.50
      });
      await linkItemToModifierGroup(item.id, modifierGroup.id);

      const orderData = {
        restaurantId: defaultRestaurantId,
        orderType: 'takeaway',
        items: [{
          menuItemId: item.id,
          quantity: 1,
          modifiers: [{ optionId: largeModifier.id }]
        }]
      };

      // Act
      const order = await orderService.createOrder(orderData);

      // Assert
      expect(order.items[0].unitPrice).toBe(12.50); // 10 + 2.50
      expect(order.items[0].modifiers[0].name).toBe('Large');
    });

    it('should validate required modifiers', async () => {
      // Arrange
      const item = await createTestItem(defaultRestaurantId, null);
      const modifierGroup = await createTestModifierGroup(defaultRestaurantId, {
        name: 'Size',
        isRequired: true
      });
      await linkItemToModifierGroup(item.id, modifierGroup.id);

      const orderData = {
        restaurantId: defaultRestaurantId,
        orderType: 'dine_in',
        items: [{
          menuItemId: item.id,
          quantity: 1,
          modifiers: [] // Missing required modifier
        }]
      };

      // Act & Assert
      await expect(orderService.createOrder(orderData))
        .rejects.toThrow('Size is required');
    });

    it('should reject unavailable items', async () => {
      // Arrange
      const item = await createTestItem(defaultRestaurantId, null, {
        isAvailable: false
      });

      const orderData = {
        restaurantId: defaultRestaurantId,
        orderType: 'takeaway',
        items: [{ menuItemId: item.id, quantity: 1 }]
      };

      // Act & Assert
      await expect(orderService.createOrder(orderData))
        .rejects.toThrow('Item is currently unavailable');
    });

    it('should generate unique order number', async () => {
      // Arrange & Act
      const order1 = await orderService.createOrder(validOrderData);
      const order2 = await orderService.createOrder(validOrderData);

      // Assert
      expect(order1.orderNumber).toBeDefined();
      expect(order2.orderNumber).toBeDefined();
      expect(order1.orderNumber).not.toBe(order2.orderNumber);
    });

    it('should calculate tax correctly', async () => {
      // Arrange
      const restaurant = await createTestRestaurant({ taxRate: 0.0825 });
      const item = await createTestItem(restaurant.id, null, { price: 100.00 });

      const orderData = {
        restaurantId: restaurant.id,
        orderType: 'dine_in',
        items: [{ menuItemId: item.id, quantity: 1 }]
      };

      // Act
      const order = await orderService.createOrder(orderData);

      // Assert
      expect(order.subtotal).toBe(100.00);
      expect(order.taxAmount).toBe(8.25);
      expect(order.total).toBe(108.25);
    });
  });

  describe('updateOrderStatus', () => {
    it('should transition from pending to confirmed', async () => {
      // Arrange
      const order = await createTestOrder({ status: 'pending' });

      // Act
      const updated = await orderService.updateStatus(order.id, 'confirmed');

      // Assert
      expect(updated.status).toBe('confirmed');
      expect(updated.confirmedAt).toBeDefined();
    });

    it('should not allow invalid status transitions', async () => {
      // Arrange
      const order = await createTestOrder({ status: 'completed' });

      // Act & Assert
      await expect(orderService.updateStatus(order.id, 'pending'))
        .rejects.toThrow('Invalid status transition');
    });

    it('should emit status update event', async () => {
      // Arrange
      const order = await createTestOrder({ status: 'pending' });
      const eventSpy = jest.spyOn(eventEmitter, 'emit');

      // Act
      await orderService.updateStatus(order.id, 'confirmed');

      // Assert
      expect(eventSpy).toHaveBeenCalledWith('order:status-changed', {
        orderId: order.id,
        previousStatus: 'pending',
        newStatus: 'confirmed'
      });
    });

    it('should send SMS when order ready for pickup', async () => {
      // Arrange
      const order = await createTestOrder({
        status: 'preparing',
        orderType: 'takeaway',
        customerPhone: '+15551234567'
      });
      const smsSpy = jest.spyOn(smsService, 'send');

      // Act
      await orderService.updateStatus(order.id, 'ready');

      // Assert
      expect(smsSpy).toHaveBeenCalledWith(
        '+15551234567',
        expect.stringContaining('ready for pickup')
      );
    });
  });

  describe('getOrdersForKitchen', () => {
    it('should return orders sorted by time', async () => {
      // Arrange
      const order1 = await createTestOrder({
        status: 'confirmed',
        confirmedAt: new Date('2026-01-15T10:00:00')
      });
      const order2 = await createTestOrder({
        status: 'confirmed',
        confirmedAt: new Date('2026-01-15T09:50:00')
      });

      // Act
      const orders = await orderService.getKitchenQueue(defaultRestaurantId);

      // Assert
      expect(orders[0].id).toBe(order2.id); // Earlier order first
      expect(orders[1].id).toBe(order1.id);
    });

    it('should only return active orders', async () => {
      // Arrange
      await createTestOrder({ status: 'confirmed' });
      await createTestOrder({ status: 'preparing' });
      await createTestOrder({ status: 'completed' });
      await createTestOrder({ status: 'cancelled' });

      // Act
      const orders = await orderService.getKitchenQueue(defaultRestaurantId);

      // Assert
      expect(orders).toHaveLength(2);
      expect(orders.every(o => ['confirmed', 'preparing'].includes(o.status))).toBe(true);
    });
  });
});
```

#### Payment Service Tests

```typescript
// tests/unit/services/payment.test.ts

describe('PaymentService', () => {
  describe('createPaymentIntent', () => {
    it('should create Stripe payment intent', async () => {
      // Arrange
      const order = await createTestOrder({ total: 54.99 });
      const stripeMock = jest.spyOn(stripe.paymentIntents, 'create')
        .mockResolvedValue({ id: 'pi_123', client_secret: 'secret_123' });

      // Act
      const result = await paymentService.createPaymentIntent(order.id);

      // Assert
      expect(stripeMock).toHaveBeenCalledWith({
        amount: 5499, // cents
        currency: 'usd',
        metadata: { orderId: order.id }
      });
      expect(result.clientSecret).toBe('secret_123');
    });

    it('should use restaurant Stripe Connect account', async () => {
      // Arrange
      const restaurant = await createTestRestaurant({
        stripeAccountId: 'acct_restaurant123'
      });
      const order = await createTestOrder({
        restaurantId: restaurant.id,
        total: 100.00
      });
      const stripeMock = jest.spyOn(stripe.paymentIntents, 'create');

      // Act
      await paymentService.createPaymentIntent(order.id);

      // Assert
      expect(stripeMock).toHaveBeenCalledWith(
        expect.objectContaining({
          transfer_data: {
            destination: 'acct_restaurant123'
          }
        })
      );
    });
  });

  describe('processRefund', () => {
    it('should refund full amount', async () => {
      // Arrange
      const order = await createTestOrder({
        total: 50.00,
        paymentIntentId: 'pi_123',
        paymentStatus: 'paid'
      });
      const refundMock = jest.spyOn(stripe.refunds, 'create')
        .mockResolvedValue({ id: 're_123', amount: 5000 });

      // Act
      const result = await paymentService.refund(order.id);

      // Assert
      expect(refundMock).toHaveBeenCalledWith({
        payment_intent: 'pi_123',
        amount: 5000
      });
      expect(result.refundId).toBe('re_123');
    });

    it('should support partial refund', async () => {
      // Arrange
      const order = await createTestOrder({
        total: 50.00,
        paymentIntentId: 'pi_123',
        paymentStatus: 'paid'
      });
      const refundMock = jest.spyOn(stripe.refunds, 'create');

      // Act
      await paymentService.refund(order.id, { amount: 10.00 });

      // Assert
      expect(refundMock).toHaveBeenCalledWith({
        payment_intent: 'pi_123',
        amount: 1000 // $10 in cents
      });
    });
  });

  describe('calculateTip', () => {
    it('should calculate percentage tip', async () => {
      // Arrange
      const subtotal = 50.00;

      // Act
      const tip15 = paymentService.calculateTip(subtotal, { percentage: 15 });
      const tip20 = paymentService.calculateTip(subtotal, { percentage: 20 });

      // Assert
      expect(tip15).toBe(7.50);
      expect(tip20).toBe(10.00);
    });

    it('should use custom amount', async () => {
      // Arrange
      const subtotal = 50.00;

      // Act
      const tip = paymentService.calculateTip(subtotal, { amount: 12.00 });

      // Assert
      expect(tip).toBe(12.00);
    });
  });
});
```

### 4.3 Integration Test Specifications

```typescript
// tests/integration/api/orders.test.ts

describe('Orders API', () => {
  let app: Express;
  let restaurant: Restaurant;
  let authToken: string;

  beforeAll(async () => {
    app = await createTestApp();
    const { token, restaurant: r } = await createAuthenticatedRestaurant();
    authToken = token;
    restaurant = r;
  });

  describe('POST /api/v1/orders', () => {
    it('should create order and return order number', async () => {
      // Arrange
      const item = await createTestItem(restaurant.id, null, { price: 15.99 });

      // Act
      const response = await request(app)
        .post('/api/v1/orders')
        .send({
          restaurantId: restaurant.id,
          orderType: 'dine_in',
          tableId: 'table-1',
          items: [{ menuItemId: item.id, quantity: 2 }]
        });

      // Assert
      expect(response.status).toBe(201);
      expect(response.body.orderNumber).toMatch(/^[A-Z0-9]{6}$/);
      expect(response.body.status).toBe('pending');
      expect(response.body.subtotal).toBe(31.98);
    });

    it('should notify kitchen via WebSocket', async () => {
      // Arrange
      const item = await createTestItem(restaurant.id, null);
      const wsClient = await connectWebSocket(restaurant.id);
      const messagePromise = waitForMessage(wsClient, 'order:new');

      // Act
      await request(app)
        .post('/api/v1/orders')
        .send({
          restaurantId: restaurant.id,
          orderType: 'dine_in',
          items: [{ menuItemId: item.id, quantity: 1 }]
        });

      // Assert
      const message = await messagePromise;
      expect(message.order).toBeDefined();
      expect(message.order.status).toBe('pending');
    });
  });

  describe('PUT /api/v1/orders/:id/status', () => {
    it('should update order status', async () => {
      // Arrange
      const order = await createTestOrder({
        restaurantId: restaurant.id,
        status: 'pending'
      });

      // Act
      const response = await request(app)
        .put(`/api/v1/orders/${order.id}/status`)
        .set('Authorization', `Bearer ${authToken}`)
        .send({ status: 'confirmed' });

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.status).toBe('confirmed');
      expect(response.body.confirmedAt).toBeDefined();
    });

    it('should require authentication', async () => {
      // Arrange
      const order = await createTestOrder({ restaurantId: restaurant.id });

      // Act
      const response = await request(app)
        .put(`/api/v1/orders/${order.id}/status`)
        .send({ status: 'confirmed' });

      // Assert
      expect(response.status).toBe(401);
    });
  });

  describe('GET /api/v1/restaurants/:id/orders', () => {
    it('should return paginated orders', async () => {
      // Arrange
      await createTestOrders(restaurant.id, 25);

      // Act
      const response = await request(app)
        .get(`/api/v1/restaurants/${restaurant.id}/orders`)
        .set('Authorization', `Bearer ${authToken}`)
        .query({ page: 1, limit: 10 });

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(10);
      expect(response.body.pagination.total).toBe(25);
    });

    it('should filter by status', async () => {
      // Arrange
      await createTestOrder({ restaurantId: restaurant.id, status: 'pending' });
      await createTestOrder({ restaurantId: restaurant.id, status: 'completed' });
      await createTestOrder({ restaurantId: restaurant.id, status: 'completed' });

      // Act
      const response = await request(app)
        .get(`/api/v1/restaurants/${restaurant.id}/orders`)
        .set('Authorization', `Bearer ${authToken}`)
        .query({ status: 'completed' });

      // Assert
      expect(response.body.data).toHaveLength(2);
    });

    it('should filter by date range', async () => {
      // Arrange
      await createTestOrder({
        restaurantId: restaurant.id,
        createdAt: new Date('2026-01-10')
      });
      await createTestOrder({
        restaurantId: restaurant.id,
        createdAt: new Date('2026-01-15')
      });

      // Act
      const response = await request(app)
        .get(`/api/v1/restaurants/${restaurant.id}/orders`)
        .set('Authorization', `Bearer ${authToken}`)
        .query({
          startDate: '2026-01-12',
          endDate: '2026-01-20'
        });

      // Assert
      expect(response.body.data).toHaveLength(1);
    });
  });
});

// tests/integration/api/menu.test.ts

describe('Public Menu API', () => {
  let restaurant: Restaurant;

  beforeAll(async () => {
    restaurant = await createTestRestaurant({ slug: 'test-restaurant' });
  });

  describe('GET /api/v1/menu/:slug', () => {
    it('should return full menu for restaurant', async () => {
      // Arrange
      const category = await createTestCategory(restaurant.id, { name: 'Mains' });
      await createTestItem(restaurant.id, category.id, { name: 'Burger', price: 12.99 });

      // Act
      const response = await request(app)
        .get('/api/v1/menu/test-restaurant');

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.restaurant.name).toBe(restaurant.name);
      expect(response.body.categories).toHaveLength(1);
      expect(response.body.categories[0].items[0].name).toBe('Burger');
    });

    it('should return 404 for non-existent restaurant', async () => {
      // Act
      const response = await request(app)
        .get('/api/v1/menu/non-existent');

      // Assert
      expect(response.status).toBe(404);
    });

    it('should return translated menu', async () => {
      // Arrange
      const category = await createTestCategory(restaurant.id, { name: 'Drinks' });
      await createTestTranslation({
        entityType: 'category',
        entityId: category.id,
        languageCode: 'es',
        field: 'name',
        value: 'Bebidas'
      });

      // Act
      const response = await request(app)
        .get('/api/v1/menu/test-restaurant')
        .query({ lang: 'es' });

      // Assert
      expect(response.body.categories[0].name).toBe('Bebidas');
    });
  });

  describe('GET /api/v1/menu/:slug/search', () => {
    it('should search menu items', async () => {
      // Arrange
      await createTestItem(restaurant.id, null, { name: 'Veggie Burger' });
      await createTestItem(restaurant.id, null, { name: 'Cheese Burger' });
      await createTestItem(restaurant.id, null, { name: 'Salad' });

      // Act
      const response = await request(app)
        .get('/api/v1/menu/test-restaurant/search')
        .query({ q: 'burger' });

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.items).toHaveLength(2);
    });
  });
});
```

### 4.4 E2E Test Specifications

```typescript
// tests/e2e/ordering-flow.spec.ts

import { test, expect } from '@playwright/test';

test.describe('Complete Ordering Flow', () => {
  test('should complete dine-in order with payment', async ({ page }) => {
    // 1. Scan QR code (simulate by navigating)
    await page.goto('/menu/joes-pizza?table=5');

    // 2. Verify menu loads
    await expect(page.getByRole('heading', { name: "Joe's Pizza" })).toBeVisible();
    await expect(page.getByText('Table 5')).toBeVisible();

    // 3. Browse categories
    await page.getByRole('button', { name: 'Pizzas' }).click();
    await expect(page.getByText('Margherita')).toBeVisible();

    // 4. Add item with modifiers
    await page.getByText('Margherita').click();
    await expect(page.getByRole('dialog')).toBeVisible();

    await page.getByRole('radio', { name: 'Large (+$4.00)' }).click();
    await page.getByRole('checkbox', { name: 'Extra Cheese (+$2.00)' }).click();
    await page.getByRole('button', { name: 'Add to Cart - $20.99' }).click();

    // 5. Verify cart
    await page.getByTestId('cart-button').click();
    await expect(page.getByText('Margherita (Large)')).toBeVisible();
    await expect(page.getByText('$20.99')).toBeVisible();

    // 6. Add another item
    await page.getByRole('button', { name: 'Continue Shopping' }).click();
    await page.getByRole('button', { name: 'Drinks' }).click();
    await page.getByText('Coca-Cola').click();
    await page.getByRole('button', { name: 'Add to Cart - $2.99' }).click();

    // 7. Proceed to checkout
    await page.getByTestId('cart-button').click();
    await page.getByRole('button', { name: 'Checkout' }).click();

    // 8. Verify totals
    await expect(page.getByText('Subtotal: $23.98')).toBeVisible();
    await expect(page.getByText('Tax: $1.98')).toBeVisible();
    await expect(page.getByText('Total: $25.96')).toBeVisible();

    // 9. Add tip
    await page.getByRole('button', { name: '20%' }).click();
    await expect(page.getByText('Tip: $4.80')).toBeVisible();
    await expect(page.getByText('Total: $30.76')).toBeVisible();

    // 10. Enter payment (Stripe test card)
    await page.frameLocator('iframe[name*="stripe"]')
      .getByPlaceholder('Card number')
      .fill('4242424242424242');
    await page.frameLocator('iframe[name*="stripe"]')
      .getByPlaceholder('MM / YY')
      .fill('12/28');
    await page.frameLocator('iframe[name*="stripe"]')
      .getByPlaceholder('CVC')
      .fill('123');

    // 11. Submit order
    await page.getByRole('button', { name: 'Pay $30.76' }).click();

    // 12. Verify confirmation
    await expect(page.getByText('Order Confirmed!')).toBeVisible({ timeout: 10000 });
    await expect(page.getByText(/Order #[A-Z0-9]{6}/)).toBeVisible();
    await expect(page.getByText('Your order is being prepared')).toBeVisible();

    // 13. Verify order appears in kitchen display (separate tab)
    const kitchenPage = await page.context().newPage();
    await kitchenPage.goto('/kitchen/joes-pizza');
    await expect(kitchenPage.getByText('Margherita (Large)')).toBeVisible();
  });

  test('should handle takeaway order with scheduled pickup', async ({ page }) => {
    // 1. Navigate to menu
    await page.goto('/menu/joes-pizza?type=takeaway');

    // 2. Add items
    await page.getByText('Pepperoni Pizza').click();
    await page.getByRole('button', { name: 'Add to Cart' }).click();

    // 3. Proceed to checkout
    await page.getByTestId('cart-button').click();
    await page.getByRole('button', { name: 'Checkout' }).click();

    // 4. Enter customer info
    await page.getByPlaceholder('Name').fill('John Doe');
    await page.getByPlaceholder('Phone').fill('555-123-4567');

    // 5. Schedule pickup time
    await page.getByRole('button', { name: 'Schedule for Later' }).click();
    await page.getByRole('combobox', { name: 'Pickup Time' }).selectOption('18:30');

    // 6. Complete payment and verify scheduled time
    await page.getByRole('button', { name: 'Pay' }).click();
    await expect(page.getByText('Pickup at 6:30 PM')).toBeVisible();
  });
});

// tests/e2e/kitchen-display.spec.ts

test.describe('Kitchen Display System', () => {
  test('should show orders in queue and allow status updates', async ({ browser }) => {
    // Create two browser contexts - one for kitchen, one for customer
    const kitchenContext = await browser.newContext();
    const customerContext = await browser.newContext();

    const kitchenPage = await kitchenContext.newPage();
    const customerPage = await customerContext.newPage();

    // Kitchen staff logs in and views display
    await kitchenPage.goto('/login');
    await kitchenPage.getByPlaceholder('PIN').fill('1234');
    await kitchenPage.getByRole('button', { name: 'Login' }).click();
    await kitchenPage.goto('/kitchen');

    // Customer places order
    await customerPage.goto('/menu/test-restaurant?table=1');
    await customerPage.getByText('Burger').click();
    await customerPage.getByRole('button', { name: 'Add to Cart' }).click();
    await customerPage.getByTestId('cart-button').click();
    await customerPage.getByRole('button', { name: 'Place Order' }).click();

    // Kitchen sees new order appear
    await expect(kitchenPage.getByText('New Order')).toBeVisible({ timeout: 5000 });
    await expect(kitchenPage.getByText('Burger')).toBeVisible();
    await expect(kitchenPage.getByText('Table 1')).toBeVisible();

    // Kitchen confirms order
    await kitchenPage.getByRole('button', { name: 'Start' }).click();
    await expect(kitchenPage.getByText('Preparing')).toBeVisible();

    // Kitchen marks order ready
    await kitchenPage.getByRole('button', { name: 'Ready' }).click();
    await expect(kitchenPage.getByText('Ready for pickup')).toBeVisible();

    // Customer sees status update
    await expect(customerPage.getByText('Your order is ready!')).toBeVisible();

    await kitchenContext.close();
    await customerContext.close();
  });
});
```

---

## 5. Implementation Plan

### 5.1 Phase 1: Foundation (Weeks 1-4)

#### Week 1: Project Setup & Core Infrastructure
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Initialize Next.js monorepo | Frontend | 1d | - |
| Setup Supabase project | Backend | 1d | - |
| Configure CI/CD (GitHub Actions) | DevOps | 1d | Monorepo |
| Create initial database schema | Backend | 2d | Supabase |
| Setup Stripe & Square accounts | Business | 1d | - |
| Design system & component library | Frontend | 2d | Next.js |

#### Week 2: Authentication & Restaurant Management
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Implement Supabase Auth | Backend | 1d | Schema |
| Build restaurant signup flow | Full-stack | 2d | Auth |
| Create restaurant settings API | Backend | 1d | Signup |
| Build admin dashboard layout | Frontend | 2d | Auth |
| Restaurant profile management UI | Frontend | 1d | Dashboard |

#### Week 3: Menu Builder
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Menu categories CRUD API | Backend | 1d | Restaurant |
| Menu items CRUD API | Backend | 2d | Categories |
| Image upload to Cloudinary | Backend | 1d | Items |
| Drag-drop menu builder UI | Frontend | 3d | APIs |
| Item modifiers system | Backend | 1d | Items |
| Modifier UI in builder | Frontend | 1d | Modifiers |

#### Week 4: QR Codes & Public Menu
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Table management API | Backend | 1d | Restaurant |
| QR code generation | Backend | 1d | Tables |
| QR download/print UI | Frontend | 1d | QR gen |
| Public menu page | Frontend | 2d | Menu API |
| Mobile-responsive menu | Frontend | 1d | Menu page |
| Search & filtering | Full-stack | 1d | Menu page |

### 5.2 Phase 2: Ordering System (Weeks 5-8)

#### Week 5: Cart & Order Creation
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Shopping cart (client-side) | Frontend | 2d | Menu |
| Order creation API | Backend | 2d | Cart |
| Order number generation | Backend | 0.5d | Order API |
| Checkout flow UI | Frontend | 2d | Cart |
| Order confirmation page | Frontend | 1d | Checkout |

#### Week 6: Payment Integration
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Stripe payment intent API | Backend | 1d | Order |
| Stripe Elements integration | Frontend | 2d | Payment API |
| Apple Pay / Google Pay | Frontend | 1d | Stripe |
| Tip selection UI | Frontend | 0.5d | Payment |
| Square payments (alternative) | Backend | 1d | - |
| Payment confirmation handling | Full-stack | 1d | Payments |

#### Week 7: Order Management
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Order list API (admin) | Backend | 1d | Orders |
| Real-time updates (WebSocket) | Backend | 2d | Orders |
| Admin order management UI | Frontend | 2d | Order API |
| Status update flow | Full-stack | 1d | WebSocket |
| Order receipt generation | Backend | 1d | Orders |

#### Week 8: Kitchen Display System
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Kitchen display API | Backend | 1d | Orders |
| Kitchen display UI | Frontend | 2d | Kitchen API |
| Item status updates | Full-stack | 1d | Display |
| Bump bar functionality | Frontend | 1d | Status |
| Audio notifications | Frontend | 0.5d | Orders |
| Prep time tracking | Backend | 1d | Orders |

### 5.3 Phase 3: Polish & Launch (Weeks 9-12)

#### Week 9: Customer Experience
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Multi-language support | Full-stack | 2d | Menu |
| Allergen filtering | Full-stack | 1d | Menu |
| Order tracking (customer) | Frontend | 1d | WebSocket |
| SMS notifications (Twilio) | Backend | 1d | Orders |
| Email receipts | Backend | 1d | Orders |

#### Week 10: Analytics & Reporting
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Order analytics API | Backend | 2d | Orders |
| Sales dashboard | Frontend | 2d | Analytics |
| Popular items tracking | Backend | 1d | Analytics |
| Export to CSV/PDF | Backend | 1d | Reports |
| Real-time metrics | Frontend | 1d | Analytics |

#### Week 11: Testing & QA
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Unit test completion (80%+ coverage) | All | 2d | - |
| Integration tests | Backend | 1d | Unit tests |
| E2E tests (Playwright) | QA | 2d | Integration |
| Performance testing | DevOps | 1d | All tests |
| Security audit | Security | 1d | All tests |
| Bug fixes | All | 2d | Testing |

#### Week 12: Launch
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Documentation | Tech Writer | 2d | - |
| Marketing website | Frontend | 2d | - |
| Beta restaurant onboarding | Support | 2d | All features |
| Production deployment | DevOps | 1d | Testing |
| Monitoring setup | DevOps | 0.5d | Production |
| Launch announcement | Marketing | 0.5d | Production |

### 5.4 Development Timeline (Gantt Chart)

```
Week    1    2    3    4    5    6    7    8    9   10   11   12
        ┌────────────────────────────────────────────────────────
Setup   ████
Auth         ████
Menu              ████████
QR/Public               ████
Cart                         ████
Payments                          ████
Order Mgmt                             ████
Kitchen                                     ████
Experience                                       ████
Analytics                                             ████
Testing                                                    ████
Launch                                                          ████
```

---

## 6. Business Model & Pricing

### 6.1 Pricing Tiers

| Feature | Free | Starter ($29/mo) | Pro ($79/mo) | Enterprise ($199/mo) |
|---------|------|------------------|--------------|----------------------|
| Menu items | 25 | Unlimited | Unlimited | Unlimited |
| QR codes | 5 | 25 | 100 | Unlimited |
| Orders/month | 100 | 1,000 | 5,000 | Unlimited |
| Payment processing | 3.5% + 30¢ | 2.9% + 30¢ | 2.5% + 30¢ | Custom |
| Languages | 1 | 3 | 10 | Unlimited |
| Team members | 1 | 3 | 10 | Unlimited |
| Kitchen display | - | ✓ | ✓ | ✓ |
| Analytics | Basic | Standard | Advanced | Custom |
| Integrations | - | 1 | 3 | All |
| White-label | - | - | - | ✓ |
| API access | - | - | ✓ | ✓ |
| Support | Community | Email | Priority | Dedicated |

### 6.2 Revenue Model

| Revenue Stream | % of Revenue | Description |
|----------------|--------------|-------------|
| Subscriptions | 60% | Monthly SaaS fees |
| Transaction fees | 30% | Percentage on payments |
| Setup/Onboarding | 5% | One-time fees |
| Add-ons | 5% | Extra features, integrations |

### 6.3 Unit Economics

| Metric | Value |
|--------|-------|
| Average Revenue Per User (ARPU) | $65/month |
| Customer Acquisition Cost (CAC) | $120 |
| Lifetime Value (LTV) | $1,560 (24-month avg tenure) |
| LTV:CAC Ratio | 13:1 |
| Gross Margin | 75% |
| Churn Rate | 4%/month |

### 6.4 Revenue Projections

| Month | Restaurants | MRR | ARR Run Rate |
|-------|-------------|-----|--------------|
| 3 | 25 | $1,625 | $19,500 |
| 6 | 100 | $6,500 | $78,000 |
| 12 | 500 | $32,500 | $390,000 |
| 18 | 1,500 | $97,500 | $1,170,000 |
| 24 | 4,000 | $260,000 | $3,120,000 |

---

## 7. Risk Assessment & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Payment processing issues | Medium | High | Multi-provider (Stripe + Square) |
| Restaurant churn | High | Medium | Focus on value, onboarding |
| POS integration complexity | High | Medium | Start with 1-2 major POS |
| Menu data migration | Medium | Low | CSV import, manual entry option |
| Peak load handling | Medium | High | CDN, auto-scaling, load testing |
| Competition from POS providers | High | Medium | Specialize in QR/mobile experience |
| Security breaches | Low | High | Regular audits, PCI compliance |

---

## 8. Success Metrics

### 8.1 Product KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Menu load time | <2s | P95 latency |
| Order completion rate | >80% | Orders / cart opens |
| Customer reorder rate | >40% | Returning customers |
| Kitchen order accuracy | >99% | Correct orders / total |
| Payment success rate | >98% | Successful / attempted |
| App crash rate | <0.1% | Crashes / sessions |

### 8.2 Business KPIs

| Metric | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|----------|
| Active restaurants | 25 | 100 | 500 |
| MRR | $1,625 | $6,500 | $32,500 |
| Churn rate | <10% | <6% | <4% |
| NPS | >30 | >40 | >50 |
| Orders processed | 5K | 50K | 500K |

---

## 9. Go-to-Market Strategy

### 9.1 Launch Phases

1. **Week 1-2:** Private beta (5 restaurants, personal network)
2. **Week 3-4:** Closed beta (20 restaurants, local area)
3. **Week 5-6:** Public beta (open signups, free tier)
4. **Week 7+:** General availability

### 9.2 Marketing Channels

| Channel | Strategy | Budget |
|---------|----------|--------|
| Local restaurants | Door-to-door, local BNI | Low |
| Google Ads | "restaurant QR menu" keywords | Medium |
| Restaurant associations | Partnerships, sponsorships | Medium |
| Content marketing | SEO, YouTube tutorials | Low |
| Referral program | $50 credit per referral | Per-acquisition |
| Trade shows | NRA Show, local expos | High (selective) |

### 9.3 Early Adopter Incentives

- **Free first 3 months** for beta participants
- **Lifetime 50% discount** for first 100 restaurants
- **Free setup & onboarding** (normally $199)
- **Featured case study** with backlink

---

## 10. Future Roadmap (Post-Launch)

### Q2 2026 (Months 4-6)
- [ ] Toast POS integration
- [ ] Square POS integration
- [ ] Customer loyalty program
- [ ] Table management & reservations
- [ ] Delivery integration (DoorDash Drive)

### Q3 2026 (Months 7-9)
- [ ] Multi-location support
- [ ] White-label reseller program
- [ ] Native iOS/Android apps
- [ ] AI menu recommendations
- [ ] Inventory management

### Q4 2026 (Months 10-12)
- [ ] API marketplace
- [ ] Advanced analytics (ClickHouse)
- [ ] A/B testing for menus
- [ ] Voice ordering integration
- [ ] International expansion

---

*Document Version: 1.0*
*Last Updated: January 2026*
