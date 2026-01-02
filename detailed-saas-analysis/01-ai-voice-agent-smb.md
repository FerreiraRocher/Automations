# AI Voice Agent Platform for SMBs - Detailed Analysis & Implementation Plan

## Executive Summary

An AI-powered voice agent platform enabling small and medium businesses to automate inbound phone calls, schedule appointments, answer FAQs, and integrate with existing business systems. This white-label solution targets restaurants, hotels, spas, medical clinics, and service businesses.

---

## 1. Market Analysis

### 1.1 Target Market Segments

| Segment | Size (US) | Pain Points | Willingness to Pay |
|---------|-----------|-------------|---------------------|
| Restaurants | 660,000+ | Missed reservations, staff answering phones during rush | High ($99-299/mo) |
| Medical/Dental Clinics | 200,000+ | Appointment scheduling, after-hours calls | Very High ($199-499/mo) |
| Salons & Spas | 1.2M+ | Booking management, no-shows | Medium ($49-149/mo) |
| Hotels & Hospitality | 60,000+ | Reservation inquiries, concierge requests | High ($199-399/mo) |
| Home Services | 500,000+ | Lead capture, scheduling estimates | High ($99-249/mo) |
| Auto Repair Shops | 160,000+ | Appointment scheduling, service inquiries | Medium ($79-199/mo) |

### 1.2 Competitive Landscape

| Competitor | Pricing | Strengths | Weaknesses |
|------------|---------|-----------|------------|
| Slang.ai | $199-499/mo | Restaurant-focused, good integrations | Limited to hospitality |
| Goodcall | $99-299/mo | Easy setup | Basic AI capabilities |
| Smith.ai | $140-600/mo | Human backup | Expensive, not fully AI |
| PolyAI | Enterprise | Advanced NLU | Not SMB-focused |
| Bland.ai | Usage-based | Developer-friendly | Requires technical setup |

### 1.3 Market Opportunity

- **TAM (Total Addressable Market):** $15B+ (voice AI services)
- **SAM (Serviceable Addressable Market):** $3B (SMB voice automation)
- **SOM (Serviceable Obtainable Market):** $50M (year 3 target)

---

## 2. Product Vision & Features

### 2.1 Core Value Proposition

> "Never miss a customer call again. Your AI receptionist works 24/7, speaks multiple languages, and costs less than a part-time employee."

### 2.2 Feature Matrix

#### Phase 1: MVP (Months 1-3)
| Feature | Priority | Complexity | User Story |
|---------|----------|------------|------------|
| Inbound call handling | P0 | High | As a business owner, I want AI to answer calls so I don't miss customers |
| Appointment scheduling | P0 | High | As a customer, I want to book appointments by phone |
| FAQ responses | P0 | Medium | As a business, I want common questions answered automatically |
| Calendar integration | P0 | Medium | As a business, I want bookings to sync with my calendar |
| Call transcription | P0 | Low | As a business, I want records of all conversations |
| Dashboard | P0 | Medium | As a business, I want to see call analytics |

#### Phase 2: Growth (Months 4-6)
| Feature | Priority | Complexity | User Story |
|---------|----------|------------|------------|
| Multi-language support | P1 | High | As a business, I want to serve Spanish-speaking customers |
| CRM integration | P1 | Medium | As a business, I want leads captured in my CRM |
| Custom voice cloning | P1 | Medium | As a business, I want the AI to sound like my brand |
| SMS follow-ups | P1 | Low | As a business, I want confirmation texts sent automatically |
| Call routing | P1 | Medium | As a business, I want complex calls transferred to staff |
| Waitlist management | P1 | Medium | As a restaurant, I want to manage walk-in waitlists |

#### Phase 3: Scale (Months 7-12)
| Feature | Priority | Complexity | User Story |
|---------|----------|------------|------------|
| Outbound calls | P2 | High | As a business, I want AI to make reminder calls |
| White-label reseller | P2 | High | As an agency, I want to resell under my brand |
| Industry templates | P2 | Medium | As a new user, I want pre-built scripts for my industry |
| Voice analytics | P2 | Medium | As a business, I want sentiment analysis on calls |
| Multi-location | P2 | Medium | As a chain, I want centralized management |
| API access | P2 | Low | As a developer, I want to integrate with my systems |

### 2.3 User Personas

#### Persona 1: Maria - Restaurant Owner
- **Age:** 45
- **Business:** Family Italian restaurant, 80 seats
- **Tech Savvy:** Low-Medium
- **Pain Points:**
  - Misses 30% of calls during dinner rush
  - Staff wastes 2 hours/day on phone
  - No-shows cost $500/week
- **Goals:**
  - Never miss a reservation
  - Reduce staff phone time
  - Automated confirmation calls
- **Budget:** $150-250/month

#### Persona 2: Dr. James - Dental Practice Owner
- **Age:** 52
- **Business:** 3-dentist practice, 15 staff
- **Tech Savvy:** Medium
- **Pain Points:**
  - Front desk overwhelmed
  - After-hours calls go to voicemail
  - New patient intake takes 15 min/call
- **Goals:**
  - 24/7 appointment scheduling
  - Insurance pre-qualification
  - Reduce front desk workload
- **Budget:** $300-500/month

#### Persona 3: Alex - Salon Chain Manager
- **Age:** 35
- **Business:** 5 salon locations, 40 stylists
- **Tech Savvy:** High
- **Pain Points:**
  - Inconsistent booking across locations
  - High no-show rate (20%)
  - Manual confirmation calls
- **Goals:**
  - Unified booking system
  - Automated reminders
  - Multi-location analytics
- **Budget:** $500-1000/month (all locations)

---

## 3. Technical Architecture

### 3.1 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT LAYER                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Web App    │  │  Mobile App  │  │   Widgets    │  │   Admin UI   │    │
│  │   (React)    │  │   (React     │  │  (Embeddable)│  │  (Dashboard) │    │
│  │              │  │    Native)   │  │              │  │              │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
└─────────┼─────────────────┼─────────────────┼─────────────────┼────────────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              API GATEWAY                                     │
│                    (Kong / AWS API Gateway / Nginx)                          │
│         ┌─────────────────────────────────────────────────────┐             │
│         │  Rate Limiting │ Auth │ Logging │ Load Balancing    │             │
│         └─────────────────────────────────────────────────────┘             │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CORE SERVICES                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   Voice Service  │  │  Booking Service │  │   User Service   │          │
│  │   ─────────────  │  │  ─────────────── │  │  ──────────────  │          │
│  │  • Call handling │  │  • Appointments  │  │  • Auth/AuthZ    │          │
│  │  • STT/TTS       │  │  • Availability  │  │  • Profiles      │          │
│  │  • Conversation  │  │  • Reminders     │  │  • Billing       │          │
│  │    management    │  │  • Calendar sync │  │  • Preferences   │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                     │                     │
│  ┌────────┴─────────┐  ┌────────┴─────────┐  ┌────────┴─────────┐          │
│  │ Analytics Service│  │Integration Service│  │ Notification Svc │          │
│  │  ─────────────── │  │  ─────────────── │  │  ──────────────  │          │
│  │  • Call metrics  │  │  • CRM sync      │  │  • SMS           │          │
│  │  • Sentiment     │  │  • POS sync      │  │  • Email         │          │
│  │  • Reporting     │  │  • Calendar      │  │  • Push          │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXTERNAL SERVICES                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │   Twilio    │ │   Vapi.ai   │ │  ElevenLabs │ │   OpenAI    │           │
│  │  (Telephony)│ │  (Voice AI) │ │   (TTS)     │ │   (LLM)     │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │   Stripe    │ │   Google    │ │  HubSpot    │ │   Twilio    │           │
│  │  (Payments) │ │  Calendar   │ │    CRM      │ │    SMS      │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
└─────────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA LAYER                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   PostgreSQL     │  │      Redis       │  │   Elasticsearch  │          │
│  │   (Primary DB)   │  │     (Cache)      │  │   (Search/Logs)  │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │       S3         │  │   TimescaleDB    │  │    ClickHouse    │          │
│  │ (Recordings)     │  │   (Time Series)  │  │   (Analytics)    │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Technology Stack

#### Backend
| Component | Technology | Rationale |
|-----------|------------|-----------|
| API Framework | Node.js + Express / FastAPI | Fast development, good async support |
| Language | TypeScript / Python | Type safety, AI library ecosystem |
| Database | PostgreSQL + Supabase | Relational data, real-time subscriptions |
| Cache | Redis | Session management, rate limiting |
| Queue | BullMQ / RabbitMQ | Background jobs, call processing |
| Search | Elasticsearch | Call transcription search |

#### Voice & AI
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Telephony | Twilio Voice | Industry standard, reliable |
| Voice AI | Vapi.ai / Retell.ai | Pre-built voice agents, low latency |
| STT (Speech-to-Text) | Deepgram / Whisper | High accuracy, real-time |
| TTS (Text-to-Speech) | ElevenLabs / PlayHT | Natural voices, low latency |
| LLM | OpenAI GPT-4 / Claude | Conversation intelligence |
| NLU | Custom + Rasa | Intent classification |

#### Frontend
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Web App | Next.js 14 | SSR, great DX |
| UI Library | Tailwind + shadcn/ui | Fast development |
| State Management | Zustand / TanStack Query | Simple, performant |
| Real-time | Socket.io | Live call monitoring |

#### Infrastructure
| Component | Technology | Rationale |
|-----------|------------|-----------|
| Cloud | AWS / GCP | Enterprise reliability |
| Container | Docker + Kubernetes | Scalability |
| CI/CD | GitHub Actions | Developer familiarity |
| Monitoring | Datadog / Grafana | Observability |
| CDN | CloudFlare | Performance, DDoS protection |

### 3.3 Database Schema

```sql
-- Core Tables

CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    industry VARCHAR(50),
    timezone VARCHAR(50) DEFAULT 'America/New_York',
    phone_number VARCHAR(20),
    twilio_phone_sid VARCHAR(50),
    settings JSONB DEFAULT '{}',
    subscription_tier VARCHAR(20) DEFAULT 'starter',
    subscription_status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    role VARCHAR(20) DEFAULT 'member',
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE voice_agents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    voice_id VARCHAR(100),
    voice_provider VARCHAR(50) DEFAULT 'elevenlabs',
    language VARCHAR(10) DEFAULT 'en-US',
    system_prompt TEXT,
    greeting_message TEXT,
    fallback_message TEXT,
    max_call_duration_seconds INTEGER DEFAULT 300,
    is_active BOOLEAN DEFAULT true,
    settings JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE knowledge_bases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    content TEXT,
    embedding_model VARCHAR(50),
    last_indexed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE faq_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    knowledge_base_id UUID REFERENCES knowledge_bases(id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category VARCHAR(100),
    embedding VECTOR(1536),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE calls (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    voice_agent_id UUID REFERENCES voice_agents(id),
    external_call_id VARCHAR(100),
    caller_phone VARCHAR(20),
    caller_name VARCHAR(255),
    direction VARCHAR(10) DEFAULT 'inbound',
    status VARCHAR(20),
    started_at TIMESTAMPTZ,
    ended_at TIMESTAMPTZ,
    duration_seconds INTEGER,
    recording_url TEXT,
    transcript TEXT,
    summary TEXT,
    sentiment_score DECIMAL(3,2),
    outcome VARCHAR(50),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE call_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    call_id UUID REFERENCES calls(id),
    event_type VARCHAR(50) NOT NULL,
    event_data JSONB,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    call_id UUID REFERENCES calls(id),
    customer_name VARCHAR(255),
    customer_phone VARCHAR(20),
    customer_email VARCHAR(255),
    service_type VARCHAR(100),
    scheduled_at TIMESTAMPTZ NOT NULL,
    duration_minutes INTEGER DEFAULT 60,
    status VARCHAR(20) DEFAULT 'confirmed',
    notes TEXT,
    reminder_sent BOOLEAN DEFAULT false,
    external_calendar_id VARCHAR(100),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE business_hours (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    day_of_week INTEGER NOT NULL, -- 0=Sunday, 6=Saturday
    open_time TIME,
    close_time TIME,
    is_closed BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE integrations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    provider VARCHAR(50) NOT NULL,
    credentials JSONB, -- encrypted
    settings JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    last_sync_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    stripe_subscription_id VARCHAR(100),
    stripe_customer_id VARCHAR(100),
    plan_id VARCHAR(50),
    status VARCHAR(20),
    current_period_start TIMESTAMPTZ,
    current_period_end TIMESTAMPTZ,
    cancel_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE usage_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    total_calls INTEGER DEFAULT 0,
    total_minutes DECIMAL(10,2) DEFAULT 0,
    total_appointments INTEGER DEFAULT 0,
    overage_minutes DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_calls_organization ON calls(organization_id);
CREATE INDEX idx_calls_started_at ON calls(started_at);
CREATE INDEX idx_appointments_organization ON appointments(organization_id);
CREATE INDEX idx_appointments_scheduled ON appointments(scheduled_at);
CREATE INDEX idx_faq_embedding ON faq_items USING ivfflat (embedding vector_cosine_ops);
```

### 3.4 API Design

#### RESTful Endpoints

```yaml
# Authentication
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh
POST   /api/v1/auth/forgot-password
POST   /api/v1/auth/reset-password

# Organizations
GET    /api/v1/organizations/:id
PUT    /api/v1/organizations/:id
GET    /api/v1/organizations/:id/settings
PUT    /api/v1/organizations/:id/settings

# Voice Agents
GET    /api/v1/voice-agents
POST   /api/v1/voice-agents
GET    /api/v1/voice-agents/:id
PUT    /api/v1/voice-agents/:id
DELETE /api/v1/voice-agents/:id
POST   /api/v1/voice-agents/:id/test-call
GET    /api/v1/voice-agents/:id/analytics

# Knowledge Base
GET    /api/v1/knowledge-bases
POST   /api/v1/knowledge-bases
GET    /api/v1/knowledge-bases/:id
PUT    /api/v1/knowledge-bases/:id
DELETE /api/v1/knowledge-bases/:id
POST   /api/v1/knowledge-bases/:id/faq
PUT    /api/v1/knowledge-bases/:id/faq/:faqId
DELETE /api/v1/knowledge-bases/:id/faq/:faqId
POST   /api/v1/knowledge-bases/:id/reindex

# Calls
GET    /api/v1/calls
GET    /api/v1/calls/:id
GET    /api/v1/calls/:id/transcript
GET    /api/v1/calls/:id/recording
GET    /api/v1/calls/analytics

# Appointments
GET    /api/v1/appointments
POST   /api/v1/appointments
GET    /api/v1/appointments/:id
PUT    /api/v1/appointments/:id
DELETE /api/v1/appointments/:id
POST   /api/v1/appointments/:id/cancel
POST   /api/v1/appointments/:id/reschedule
GET    /api/v1/appointments/availability

# Integrations
GET    /api/v1/integrations
POST   /api/v1/integrations
GET    /api/v1/integrations/:id
PUT    /api/v1/integrations/:id
DELETE /api/v1/integrations/:id
POST   /api/v1/integrations/:id/sync
GET    /api/v1/integrations/:id/status

# Webhooks (Twilio/Vapi callbacks)
POST   /api/v1/webhooks/twilio/voice
POST   /api/v1/webhooks/twilio/status
POST   /api/v1/webhooks/vapi/events
POST   /api/v1/webhooks/stripe

# Billing
GET    /api/v1/billing/subscription
POST   /api/v1/billing/subscribe
POST   /api/v1/billing/cancel
PUT    /api/v1/billing/update-payment
GET    /api/v1/billing/invoices
GET    /api/v1/billing/usage
```

---

## 4. Test-Driven Development (TDD) Approach

### 4.1 Testing Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                      Testing Pyramid                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                         ┌─────────┐                              │
│                        /   E2E    \        5-10% of tests       │
│                       /  (Cypress) \                             │
│                      ───────────────                             │
│                     /  Integration  \      20-30% of tests       │
│                    / (Supertest/Jest)\                           │
│                   ─────────────────────                          │
│                  /      Unit Tests      \   60-70% of tests      │
│                 /    (Jest/Vitest)       \                       │
│                ───────────────────────────                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Unit Test Specifications

#### Voice Agent Service Tests

```typescript
// tests/unit/services/voiceAgent.test.ts

describe('VoiceAgentService', () => {
  describe('createAgent', () => {
    it('should create a voice agent with default settings', async () => {
      // Arrange
      const orgId = 'org-123';
      const agentData = {
        name: 'Reception Bot',
        language: 'en-US',
        greeting: 'Hello, thank you for calling...'
      };

      // Act
      const agent = await voiceAgentService.create(orgId, agentData);

      // Assert
      expect(agent.id).toBeDefined();
      expect(agent.name).toBe('Reception Bot');
      expect(agent.isActive).toBe(true);
      expect(agent.maxCallDurationSeconds).toBe(300);
    });

    it('should validate required fields', async () => {
      // Arrange
      const orgId = 'org-123';
      const invalidData = { language: 'en-US' }; // missing name

      // Act & Assert
      await expect(voiceAgentService.create(orgId, invalidData))
        .rejects.toThrow('Name is required');
    });

    it('should reject unsupported languages', async () => {
      // Arrange
      const agentData = { name: 'Test', language: 'xx-YY' };

      // Act & Assert
      await expect(voiceAgentService.create('org-123', agentData))
        .rejects.toThrow('Unsupported language');
    });
  });

  describe('processIntent', () => {
    it('should correctly classify booking intent', async () => {
      // Arrange
      const utterance = "I'd like to make a reservation for tomorrow";

      // Act
      const intent = await voiceAgentService.classifyIntent(utterance);

      // Assert
      expect(intent.name).toBe('book_appointment');
      expect(intent.confidence).toBeGreaterThan(0.8);
    });

    it('should extract date entities from utterance', async () => {
      // Arrange
      const utterance = "Book me for next Tuesday at 3pm";

      // Act
      const entities = await voiceAgentService.extractEntities(utterance);

      // Assert
      expect(entities).toContainEqual({
        type: 'date',
        value: expect.any(Date)
      });
      expect(entities).toContainEqual({
        type: 'time',
        value: '15:00'
      });
    });

    it('should handle ambiguous requests by asking clarification', async () => {
      // Arrange
      const utterance = "I want to come in sometime";

      // Act
      const response = await voiceAgentService.generateResponse(
        'agent-123',
        utterance,
        { conversationId: 'conv-1' }
      );

      // Assert
      expect(response.requiresClarification).toBe(true);
      expect(response.text).toContain('What day');
    });
  });

  describe('handleCall', () => {
    it('should greet caller with configured message', async () => {
      // Arrange
      const agent = await createTestAgent({
        greeting: 'Welcome to Joes Pizza'
      });

      // Act
      const greeting = await voiceAgentService.getGreeting(agent.id);

      // Assert
      expect(greeting).toBe('Welcome to Joes Pizza');
    });

    it('should respect business hours', async () => {
      // Arrange
      jest.setSystemTime(new Date('2026-01-15T02:00:00Z')); // 2am
      const agent = await createTestAgentWithHours({
        openTime: '09:00',
        closeTime: '17:00'
      });

      // Act
      const response = await voiceAgentService.handleIncomingCall(
        agent.id,
        '+15551234567'
      );

      // Assert
      expect(response.action).toBe('after_hours_message');
      expect(response.message).toContain('currently closed');
    });

    it('should limit call duration to max configured time', async () => {
      // Arrange
      const agent = await createTestAgent({
        maxCallDurationSeconds: 180
      });
      const call = await startTestCall(agent.id);

      // Simulate call running for 180 seconds
      jest.advanceTimersByTime(180000);

      // Act
      const status = await voiceAgentService.getCallStatus(call.id);

      // Assert
      expect(status.shouldTerminate).toBe(true);
      expect(status.terminationReason).toBe('max_duration_exceeded');
    });
  });
});
```

#### Appointment Service Tests

```typescript
// tests/unit/services/appointment.test.ts

describe('AppointmentService', () => {
  describe('checkAvailability', () => {
    it('should return available slots for given date', async () => {
      // Arrange
      const orgId = 'org-123';
      const date = new Date('2026-01-20');
      await seedBusinessHours(orgId, {
        monday: { open: '09:00', close: '17:00' }
      });

      // Act
      const slots = await appointmentService.getAvailableSlots(orgId, date);

      // Assert
      expect(slots.length).toBe(16); // 30-min slots from 9am-5pm
      expect(slots[0].startTime).toBe('09:00');
      expect(slots[slots.length - 1].startTime).toBe('16:30');
    });

    it('should exclude booked slots', async () => {
      // Arrange
      const orgId = 'org-123';
      const date = new Date('2026-01-20');
      await createTestAppointment(orgId, {
        scheduledAt: new Date('2026-01-20T10:00:00'),
        durationMinutes: 60
      });

      // Act
      const slots = await appointmentService.getAvailableSlots(orgId, date);

      // Assert
      const tenAmSlot = slots.find(s => s.startTime === '10:00');
      const tenThirtySlot = slots.find(s => s.startTime === '10:30');
      expect(tenAmSlot).toBeUndefined();
      expect(tenThirtySlot).toBeUndefined();
    });

    it('should respect buffer time between appointments', async () => {
      // Arrange
      const orgId = 'org-123';
      await updateOrgSettings(orgId, { bufferMinutes: 15 });
      await createTestAppointment(orgId, {
        scheduledAt: new Date('2026-01-20T10:00:00'),
        durationMinutes: 30
      });

      // Act
      const slots = await appointmentService.getAvailableSlots(
        orgId,
        new Date('2026-01-20')
      );

      // Assert
      // 10:00-10:30 booked, 10:30-10:45 buffer, so 10:30 unavailable
      const tenThirtySlot = slots.find(s => s.startTime === '10:30');
      expect(tenThirtySlot).toBeUndefined();
    });
  });

  describe('createAppointment', () => {
    it('should create appointment and sync to calendar', async () => {
      // Arrange
      const appointmentData = {
        customerName: 'John Doe',
        customerPhone: '+15551234567',
        scheduledAt: new Date('2026-01-20T14:00:00'),
        serviceType: 'Haircut'
      };
      const calendarSyncSpy = jest.spyOn(calendarService, 'createEvent');

      // Act
      const appointment = await appointmentService.create('org-123', appointmentData);

      // Assert
      expect(appointment.id).toBeDefined();
      expect(appointment.status).toBe('confirmed');
      expect(calendarSyncSpy).toHaveBeenCalledWith(expect.objectContaining({
        title: 'Haircut - John Doe',
        startTime: appointmentData.scheduledAt
      }));
    });

    it('should prevent double-booking', async () => {
      // Arrange
      const scheduledAt = new Date('2026-01-20T14:00:00');
      await appointmentService.create('org-123', {
        customerName: 'Jane Doe',
        scheduledAt,
        serviceType: 'Haircut'
      });

      // Act & Assert
      await expect(
        appointmentService.create('org-123', {
          customerName: 'John Doe',
          scheduledAt,
          serviceType: 'Haircut'
        })
      ).rejects.toThrow('Time slot not available');
    });

    it('should send confirmation SMS', async () => {
      // Arrange
      const smsSpy = jest.spyOn(smsService, 'send');

      // Act
      await appointmentService.create('org-123', {
        customerName: 'John Doe',
        customerPhone: '+15551234567',
        scheduledAt: new Date('2026-01-20T14:00:00'),
        serviceType: 'Haircut'
      });

      // Assert
      expect(smsSpy).toHaveBeenCalledWith(
        '+15551234567',
        expect.stringContaining('confirmed')
      );
    });
  });

  describe('cancelAppointment', () => {
    it('should cancel and notify customer', async () => {
      // Arrange
      const appointment = await createTestAppointment('org-123', {
        customerPhone: '+15551234567',
        scheduledAt: new Date('2026-01-20T14:00:00')
      });
      const smsSpy = jest.spyOn(smsService, 'send');

      // Act
      await appointmentService.cancel(appointment.id, 'Customer request');

      // Assert
      const updated = await appointmentService.findById(appointment.id);
      expect(updated.status).toBe('cancelled');
      expect(smsSpy).toHaveBeenCalledWith(
        '+15551234567',
        expect.stringContaining('cancelled')
      );
    });

    it('should free up the time slot', async () => {
      // Arrange
      const scheduledAt = new Date('2026-01-20T14:00:00');
      const appointment = await createTestAppointment('org-123', {
        scheduledAt
      });

      // Act
      await appointmentService.cancel(appointment.id);

      // Assert
      const slots = await appointmentService.getAvailableSlots(
        'org-123',
        new Date('2026-01-20')
      );
      const slot = slots.find(s => s.startTime === '14:00');
      expect(slot).toBeDefined();
    });
  });

  describe('sendReminders', () => {
    it('should send reminder 24 hours before', async () => {
      // Arrange
      jest.setSystemTime(new Date('2026-01-19T14:00:00Z'));
      const appointment = await createTestAppointment('org-123', {
        customerPhone: '+15551234567',
        scheduledAt: new Date('2026-01-20T14:00:00Z'),
        reminderSent: false
      });
      const smsSpy = jest.spyOn(smsService, 'send');

      // Act
      await appointmentService.sendDueReminders();

      // Assert
      expect(smsSpy).toHaveBeenCalledWith(
        '+15551234567',
        expect.stringContaining('reminder')
      );
      const updated = await appointmentService.findById(appointment.id);
      expect(updated.reminderSent).toBe(true);
    });
  });
});
```

#### Integration Tests

```typescript
// tests/integration/api/calls.test.ts

describe('Calls API', () => {
  let app: Express;
  let authToken: string;

  beforeAll(async () => {
    app = await createTestApp();
    const { token } = await createTestUserWithOrg();
    authToken = token;
  });

  describe('GET /api/v1/calls', () => {
    it('should return paginated call list', async () => {
      // Arrange
      await createTestCalls(25);

      // Act
      const response = await request(app)
        .get('/api/v1/calls')
        .set('Authorization', `Bearer ${authToken}`)
        .query({ page: 1, limit: 10 });

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(10);
      expect(response.body.pagination.total).toBe(25);
      expect(response.body.pagination.hasMore).toBe(true);
    });

    it('should filter by date range', async () => {
      // Arrange
      await createTestCall({ startedAt: new Date('2026-01-10') });
      await createTestCall({ startedAt: new Date('2026-01-15') });
      await createTestCall({ startedAt: new Date('2026-01-20') });

      // Act
      const response = await request(app)
        .get('/api/v1/calls')
        .set('Authorization', `Bearer ${authToken}`)
        .query({
          startDate: '2026-01-12',
          endDate: '2026-01-18'
        });

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(1);
    });
  });

  describe('GET /api/v1/calls/:id/transcript', () => {
    it('should return call transcript', async () => {
      // Arrange
      const call = await createTestCall({
        transcript: 'Hello, I want to book an appointment...'
      });

      // Act
      const response = await request(app)
        .get(`/api/v1/calls/${call.id}/transcript`)
        .set('Authorization', `Bearer ${authToken}`);

      // Assert
      expect(response.status).toBe(200);
      expect(response.body.transcript).toContain('book an appointment');
    });
  });
});

// tests/integration/webhooks/twilio.test.ts

describe('Twilio Webhooks', () => {
  describe('POST /api/v1/webhooks/twilio/voice', () => {
    it('should handle incoming call', async () => {
      // Arrange
      const twilioPayload = {
        CallSid: 'CA123456',
        From: '+15551234567',
        To: '+15559876543',
        CallStatus: 'ringing'
      };
      const signature = generateTwilioSignature(twilioPayload);

      // Act
      const response = await request(app)
        .post('/api/v1/webhooks/twilio/voice')
        .set('X-Twilio-Signature', signature)
        .send(twilioPayload);

      // Assert
      expect(response.status).toBe(200);
      expect(response.headers['content-type']).toContain('application/xml');
      expect(response.text).toContain('<Response>');
    });

    it('should reject invalid signatures', async () => {
      // Arrange
      const twilioPayload = {
        CallSid: 'CA123456',
        From: '+15551234567'
      };

      // Act
      const response = await request(app)
        .post('/api/v1/webhooks/twilio/voice')
        .set('X-Twilio-Signature', 'invalid-signature')
        .send(twilioPayload);

      // Assert
      expect(response.status).toBe(401);
    });
  });
});
```

### 4.3 E2E Test Specifications

```typescript
// tests/e2e/booking-flow.test.ts

describe('Complete Booking Flow', () => {
  it('should handle end-to-end booking via phone call', async () => {
    // This test simulates a complete call flow using mock telephony

    // 1. Business setup
    const org = await createOrganization({
      name: 'Test Restaurant',
      timezone: 'America/New_York'
    });

    const agent = await createVoiceAgent(org.id, {
      name: 'Booking Assistant',
      greeting: 'Hello, thanks for calling Test Restaurant'
    });

    await setBusinessHours(org.id, {
      monday: { open: '11:00', close: '22:00' }
    });

    // 2. Simulate incoming call
    const call = await simulateIncomingCall({
      to: org.phoneNumber,
      from: '+15551234567'
    });

    // 3. Verify greeting played
    expect(call.audioPlayed).toContain('Hello, thanks for calling');

    // 4. Simulate user speech
    await simulateUserSpeech(call.id, "I'd like to make a reservation");

    // 5. Verify agent asks for details
    const response1 = await getAgentResponse(call.id);
    expect(response1).toContain('What day');

    // 6. Continue conversation
    await simulateUserSpeech(call.id, "Tomorrow at 7pm for 4 people");

    const response2 = await getAgentResponse(call.id);
    expect(response2).toContain('party of 4');
    expect(response2).toContain('7:00 PM');

    // 7. Confirm
    await simulateUserSpeech(call.id, "Yes, that's correct");

    // 8. Get name
    await simulateUserSpeech(call.id, "John Smith");

    // 9. Verify booking created
    const appointments = await getAppointments(org.id);
    expect(appointments).toHaveLength(1);
    expect(appointments[0].customerName).toBe('John Smith');
    expect(appointments[0].partySize).toBe(4);

    // 10. Verify confirmation SMS sent
    const smsLogs = await getSMSLogs('+15551234567');
    expect(smsLogs[0].body).toContain('confirmed');

    // 11. Verify call logged
    const callLog = await getCallById(call.id);
    expect(callLog.status).toBe('completed');
    expect(callLog.outcome).toBe('booking_created');
  });
});
```

---

## 5. Implementation Plan

### 5.1 Phase 1: Foundation (Weeks 1-4)

#### Week 1: Project Setup
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Initialize monorepo structure | Backend Dev | 2d | - |
| Setup CI/CD pipeline | DevOps | 2d | Monorepo |
| Configure development environments | DevOps | 1d | CI/CD |
| Setup PostgreSQL + Supabase | Backend Dev | 1d | Environments |
| Create initial database schema | Backend Dev | 2d | Database |

#### Week 2: Core API Development
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Implement authentication (JWT) | Backend Dev | 2d | Database |
| Build user/organization CRUD | Backend Dev | 2d | Auth |
| Create voice agent CRUD | Backend Dev | 2d | User/Org |
| Setup API documentation (OpenAPI) | Backend Dev | 1d | APIs |

#### Week 3: Voice Infrastructure
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Twilio account setup | DevOps | 0.5d | - |
| Implement Twilio webhook handlers | Backend Dev | 2d | Twilio |
| Integrate Vapi.ai for voice AI | Backend Dev | 3d | Webhooks |
| Build conversation state machine | Backend Dev | 2d | Vapi |

#### Week 4: Booking System
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Implement appointment CRUD | Backend Dev | 2d | Database |
| Build availability checking | Backend Dev | 2d | Appointments |
| Google Calendar integration | Backend Dev | 2d | Availability |
| SMS notification system | Backend Dev | 1d | Appointments |

### 5.2 Phase 2: Core Features (Weeks 5-8)

#### Week 5: Knowledge Base & FAQ
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Implement FAQ storage | Backend Dev | 1d | Database |
| Vector embedding generation | AI Dev | 2d | FAQ storage |
| Semantic search for FAQs | AI Dev | 2d | Embeddings |
| Context injection for voice agent | AI Dev | 2d | Search |

#### Week 6: Dashboard Frontend
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Setup Next.js project | Frontend Dev | 1d | - |
| Build authentication UI | Frontend Dev | 2d | Auth API |
| Create dashboard layout | Frontend Dev | 2d | Auth UI |
| Implement call logs view | Frontend Dev | 2d | Dashboard |

#### Week 7: Agent Configuration UI
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Voice agent setup wizard | Frontend Dev | 3d | Dashboard |
| Greeting/prompt editor | Frontend Dev | 2d | Wizard |
| FAQ management interface | Frontend Dev | 2d | Editor |
| Business hours configuration | Frontend Dev | 1d | Dashboard |

#### Week 8: Analytics & Reporting
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Implement analytics aggregation | Backend Dev | 2d | Calls data |
| Build analytics API endpoints | Backend Dev | 1d | Aggregation |
| Create analytics dashboard | Frontend Dev | 3d | Analytics API |
| Export functionality (CSV, PDF) | Backend Dev | 1d | Analytics |

### 5.3 Phase 3: Polish & Launch (Weeks 9-12)

#### Week 9: Integrations
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| HubSpot CRM integration | Backend Dev | 2d | - |
| GoHighLevel integration | Backend Dev | 2d | - |
| Toast POS integration | Backend Dev | 2d | - |
| Integration configuration UI | Frontend Dev | 2d | Backend integrations |

#### Week 10: Billing & Onboarding
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Stripe subscription setup | Backend Dev | 2d | - |
| Usage tracking & metering | Backend Dev | 2d | Stripe |
| Billing management UI | Frontend Dev | 2d | Usage tracking |
| Onboarding flow | Frontend Dev | 3d | All features |

#### Week 11: Testing & QA
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Complete unit test coverage | All Devs | 2d | - |
| Integration testing | QA | 2d | Unit tests |
| E2E testing | QA | 2d | Integration |
| Performance testing | DevOps | 1d | E2E |
| Security audit | Security | 2d | All testing |

#### Week 12: Launch Preparation
| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Documentation completion | Tech Writer | 2d | - |
| Marketing website | Frontend Dev | 2d | - |
| Beta user onboarding | Support | 3d | Onboarding flow |
| Production deployment | DevOps | 1d | All testing |
| Monitoring & alerting setup | DevOps | 1d | Production |

### 5.4 Gantt Chart (Simplified)

```
Week   1   2   3   4   5   6   7   8   9  10  11  12
       ┌───────────────────────────────────────────────
Setup  ████
Core API   ████
Voice          ████
Booking            ████
KB & FAQ               ████
Dashboard                  ████
Agent UI                       ████
Analytics                          ████
Integrations                           ████
Billing                                    ████
Testing                                        ████
Launch                                             ████
```

---

## 6. Business Model & Pricing

### 6.1 Pricing Tiers

| Feature | Starter ($99/mo) | Professional ($199/mo) | Enterprise ($399/mo) |
|---------|------------------|----------------------|---------------------|
| Monthly call minutes | 500 | 1,500 | 5,000 |
| Phone numbers | 1 | 3 | 10 |
| Voice agents | 1 | 3 | Unlimited |
| Languages | 1 | 3 | All |
| Calendar integrations | Google | Google, Outlook | All |
| CRM integrations | - | HubSpot | All |
| Custom voice | - | ✓ | ✓ |
| Analytics | Basic | Advanced | Advanced + API |
| Support | Email | Priority email | Dedicated CSM |
| White-label | - | - | ✓ |

### 6.2 Additional Charges

| Item | Cost |
|------|------|
| Additional minutes | $0.15/minute |
| Additional phone number | $15/month |
| SMS messages | $0.02/message |
| Custom voice cloning | $100 one-time |
| Premium support | $200/month |

### 6.3 Revenue Projections

| Month | Customers | MRR | Notes |
|-------|-----------|-----|-------|
| 1-3 | 10 | $1,500 | Beta customers (discounted) |
| 4-6 | 50 | $8,500 | Launch + initial marketing |
| 7-9 | 150 | $27,000 | Content + partnerships |
| 10-12 | 400 | $72,000 | Scaling marketing |
| Year 2 | 2,000 | $400,000 | Product-market fit |

---

## 7. Risk Assessment & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Voice AI quality issues | Medium | High | Multi-provider fallback (Vapi + Retell) |
| Telephony downtime | Low | High | Twilio backup + status monitoring |
| LLM cost overruns | Medium | Medium | Rate limiting, response caching |
| Integration complexity | High | Medium | Start with 2-3 key integrations |
| Customer churn | Medium | High | Focus on onboarding, quick time-to-value |
| Competition | High | Medium | Niche focus (specific verticals) |

---

## 8. Success Metrics

### 8.1 Product KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Call success rate | >90% | Calls completed without errors |
| Booking conversion | >60% | Booking calls → appointments |
| Customer satisfaction | >4.5/5 | Post-call surveys |
| Average call duration | <3 min | Efficiency |
| First response time | <500ms | AI latency |

### 8.2 Business KPIs

| Metric | Month 6 Target | Month 12 Target |
|--------|---------------|-----------------|
| MRR | $8,500 | $72,000 |
| Customers | 50 | 400 |
| Churn rate | <5% | <3% |
| CAC | <$200 | <$150 |
| LTV | >$1,500 | >$2,000 |

---

## 9. Go-to-Market Strategy

### 9.1 Launch Channels

1. **Upwork/Freelancer** - Offer implementation services, convert to SaaS
2. **Restaurant associations** - Partner with local restaurant groups
3. **Google Ads** - Target "restaurant reservation software"
4. **Content marketing** - Blog posts on restaurant efficiency
5. **LinkedIn outreach** - Direct to restaurant owners

### 9.2 Launch Timeline

- **Week 1-2:** Private beta with 10 restaurants
- **Week 3-4:** Collect feedback, iterate
- **Week 5:** Product Hunt launch
- **Week 6+:** Scale marketing

---

*Document Version: 1.0*
*Last Updated: January 2026*
