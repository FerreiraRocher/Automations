# NHS Login Strategic Roadmap
## A Patient-Centred Digital Identity Strategy for NHS Services

**Document Version:** 1.0
**Date:** January 2025
**Author:** NHS Digital Strategy Advisory

---

## Executive Summary

NHS login serves as the **digital front door** to the entire NHS ecosystem, providing citizens with secure, unified access to health and care services. This strategic roadmap positions NHS login not merely as an authentication mechanism, but as the foundational infrastructure enabling patient empowerment, service transformation, and healthcare equity.

Drawing from international best practices (Estonia, Denmark, Australia) and aligning with the **10 Year Health Plan's** vision for a "digital by default" NHS, this roadmap outlines a phased approach to transform NHS login into a world-leading healthcare identity platform.

---

## Table of Contents

1. [Current State Analysis](#1-current-state-analysis)
2. [Competitive Landscape & International Benchmarks](#2-competitive-landscape--international-benchmarks)
3. [Patient Journey Mapping](#3-patient-journey-mapping)
4. [Strategic Vision & Objectives](#4-strategic-vision--objectives)
5. [Phased Implementation Roadmap](#5-phased-implementation-roadmap)
6. [Key Features & Capabilities](#6-key-features--capabilities)
7. [Accessibility & Inclusion Strategy](#7-accessibility--inclusion-strategy)
8. [Security & Trust Framework](#8-security--trust-framework)
9. [Governance & Success Metrics](#9-governance--success-metrics)
10. [Risk Assessment & Mitigation](#10-risk-assessment--mitigation)

---

## 1. Current State Analysis

### 1.1 NHS Login Today

NHS login is an OpenID Connect-based authentication and identity verification service that enables citizens to access multiple NHS digital services with a single set of credentials.

**Current Capabilities:**
- FIDO UAF biometric authentication (fingerprint, facial recognition)
- iProov facial authentication for remote onboarding
- Multi-factor authentication (SMS OTP, biometric)
- Integration with NHS App (37.4+ million users)
- P9 (highest) identity verification level support
- Compliance with DAPB3051 and GPG45 standards

**Current Scale:**
- ~1.2 million biometric-enabled users
- 32,000 new users per week average growth
- 65% reduction in SMS OTP costs through biometric adoption
- 88% push notification opt-in rate

### 1.2 Identity Verification Levels

| Level | Description | Access Granted |
|-------|-------------|----------------|
| P0 | Basic - email/phone only | Limited public information |
| P5 | Medium - basic ID checks | Some personal health data |
| P9 | High - full identity verification | Full GP records, prescriptions, sensitive data |

### 1.3 Current Challenges

Based on analysis and user feedback:

1. **Onboarding Complexity** - Initial identity verification can be challenging for certain demographics
2. **Photo ID Requirements** - Excludes users without passports/driving licenses
3. **Face Scan Accessibility** - Difficulties for users with certain disabilities
4. **GP Linkage Delays** - Manual processes for GP surgery verification
5. **Legacy System Integration** - Inconsistent adoption across NHS trusts
6. **Proxy Access Limitations** - Complex setup for carers and parents

---

## 2. Competitive Landscape & International Benchmarks

### 2.1 Estonia: The Gold Standard

**e-Estonia Health Information System**

Estonia represents the most mature digital health identity ecosystem globally:

| Metric | Performance |
|--------|-------------|
| Digital identity coverage | 100% of residents (since 2002) |
| Healthcare provider adoption | 98% upload patient information |
| Monthly health portal logins | 900,000 |
| Health documents digitised | 40+ million |

**Key Success Factors:**
- Universal PKI-based digital identity (ID card, Mobile ID)
- X-Road secure data exchange infrastructure
- KSI Blockchain for data integrity
- Clear governance and legal framework
- Patient-controlled access permissions
- Transparent audit logs (who accessed your data)

**Lessons for NHS Login:**
- Invest in universal identity infrastructure
- Implement comprehensive audit trails visible to patients
- Ensure legal clarity on data ownership and access rights
- Standardise medical data exchange formats

### 2.2 Denmark: Sundhed.dk

**National Health Portal**

Denmark achieves exceptional penetration with its unified health portal:

| Metric | Performance |
|--------|-------------|
| Population recognition | 96% |
| Monthly unique visitors | 2.3 million |
| Historical data access | Records from 1977 |
| Data misuse incidents | 3-5 per year |

**Key Features:**
- CPR number-based unique identification from birth
- Two-factor authentication with digital signature
- Role-based personalised portal experience
- Complete health history visibility
- Real-time access monitoring

**Lessons for NHS Login:**
- Leverage NHS number as unique identifier more effectively
- Provide personalised, context-aware user experiences
- Implement comprehensive health history visualisation
- Build robust misuse detection and transparent reporting

### 2.3 Australia: My Health Record

**National Opt-Out System**

Australia's transition from opt-in to opt-out achieved 90% coverage:

| Metric | Performance |
|--------|-------------|
| Population coverage | 90% |
| Years without security breach | 7+ |
| Emergency department access rate | 19.6% |

**Key Learnings:**
- Opt-out model drives adoption but requires trust-building
- Community engagement essential for vulnerable populations
- Usability issues significantly impact adoption
- Clinical adoption requires active change management
- Security concerns must be addressed proactively

### 2.4 Epic MyChart (USA)

**Leading Patient Portal**

Epic serves 3,600+ US hospitals (38% market share):

**Key Innovations:**
- **MyChart Central** - Unified view across multiple providers
- **Epic ID** - Single login across all Epic accounts
- **Clear Integration** - Airport-style identity verification
- **TEFCA Compliance** - Federal health data exchange

**Lessons for NHS Login:**
- Single identity across disparate systems is achievable
- Third-party identity verification partnerships add value
- Interoperability standards enable ecosystem growth

### 2.5 GOV.UK One Login

**Government Digital Identity**

The UK government's flagship identity service provides relevant learning:

**Key Features:**
- OpenID Connect based (same as NHS login)
- Photo ID + biometric face matching
- GOV.UK Wallet for digital documents (planned)
- Mandatory for all government services

**Integration Opportunity:**
NHS login and GOV.UK One Login share technical standards. Strategic alignment could enable:
- Shared identity verification effort
- Cross-government service access
- Unified digital wallet for health + government documents

---

## 3. Patient Journey Mapping

### 3.1 Patient Personas

#### Persona 1: Sarah - Young Professional (28)
- **Needs:** Quick access to GP appointments, prescription management
- **Behaviour:** Mobile-first, expects banking-app experience
- **Pain Points:** Frustrated by multiple logins, wants instant access
- **Priority Features:** Push notifications, one-tap prescription reorder

#### Persona 2: James - Father of Two (42)
- **Needs:** Manage family health, children's appointments/vaccinations
- **Behaviour:** Time-poor, needs efficiency
- **Pain Points:** Cannot easily manage children's health digitally
- **Priority Features:** Proxy access, family health dashboard, red book digitisation

#### Persona 3: Margaret - Elderly Patient (78)
- **Needs:** Access test results, communicate with care team
- **Behaviour:** Less tech-confident, prefers larger text
- **Pain Points:** Complex verification, small interface elements
- **Priority Features:** Simplified interface, voice assistance, carer access

#### Persona 4: Ahmed - Carer (55)
- **Needs:** Manage health for elderly mother with dementia
- **Behaviour:** Requires delegate access across multiple services
- **Pain Points:** Must set up access at each provider separately
- **Priority Features:** Universal proxy access, care coordination tools

#### Persona 5: Lisa - Disabled User (35)
- **Needs:** Independent health management with accessibility support
- **Behaviour:** Uses screen readers, voice control
- **Pain Points:** Face scan verification, complex forms
- **Priority Features:** Alternative verification methods, WCAG AAA compliance

### 3.2 Patient Journey Stages

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NHS LOGIN PATIENT JOURNEY                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. AWARENESS    2. REGISTRATION    3. VERIFICATION    4. ACCESS           │
│  ───────────     ──────────────     ─────────────      ────────           │
│  • NHS App       • Create account   • Photo ID scan    • GP services       │
│  • GP surgery    • Email/phone      • Face match       • Prescriptions     │
│  • Hospital      • Password setup   • GP linkage       • Appointments      │
│  • Word of mouth • Terms consent    • P9 upgrade       • Health records    │
│                                                                             │
│                                                                             │
│  5. ONGOING USE     6. EXPANSION       7. ADVOCACY                         │
│  ─────────────      ──────────         ────────────                         │
│  • Regular login    • Proxy setup      • Recommend to others               │
│  • Multi-service    • Family access    • Provide feedback                  │
│  • Health mgmt      • New services     • Community support                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Critical Touchpoints & Pain Points

| Stage | Current Pain Point | Target Experience |
|-------|-------------------|-------------------|
| Registration | 15-20 minute process | 5 minutes or less |
| Verification | Photo ID required | Multiple pathways including no-ID options |
| GP Linkage | Manual approval delays | Instant digital verification |
| Proxy Setup | Per-practice setup | One-time national registration |
| Service Access | Inconsistent across trusts | Unified experience everywhere |
| Support | Limited help options | AI assistant + human escalation |

---

## 4. Strategic Vision & Objectives

### 4.1 Vision Statement

> **"NHS login will be the trusted, inclusive digital identity that empowers every person in England to seamlessly access, manage, and take control of their health and care - regardless of their circumstances, capabilities, or needs."**

### 4.2 Strategic Objectives

#### Objective 1: Universal Access
**Goal:** Ensure NHS login is accessible to 100% of the population, with alternative pathways for all user groups.

**Key Results:**
- 95% of adults have verified NHS login by 2028
- Zero reliance on single verification method
- Full WCAG AAA accessibility compliance
- Support for users without smartphones or photo ID

#### Objective 2: Seamless Integration
**Goal:** NHS login becomes the single authentication layer across all NHS digital services.

**Key Results:**
- 100% of NHS trusts integrated by 2026
- Single sign-on across primary, secondary, and social care
- Integration with approved third-party health apps
- Alignment with GOV.UK One Login where appropriate

#### Objective 3: Patient Empowerment
**Goal:** Enable patients to truly own and control their health identity and data.

**Key Results:**
- Comprehensive audit log visibility (who accessed your data)
- Granular consent management
- Data portability and sharing controls
- Proxy/delegate access for carers and family

#### Objective 4: Trust & Security
**Goal:** Maintain the highest security standards while minimising friction.

**Key Results:**
- Zero security breaches of core identity infrastructure
- <1% fraud rate on identity verification
- NCSC Cyber Essentials Plus certification
- Annual third-party security audits published

#### Objective 5: Operational Efficiency
**Goal:** Reduce NHS operational burden through digital identity automation.

**Key Results:**
- 80% reduction in manual identity verification at point of care
- 50% reduction in duplicate patient records
- £100M+ annual savings from reduced administrative overhead
- Eliminate "8am scramble" through digital-first appointment booking

---

## 5. Phased Implementation Roadmap

### Phase 1: Foundation Enhancement (2025)
**Theme: "Strengthen the Core"**

```
Q1 2025                    Q2 2025                    Q3-Q4 2025
─────────                  ─────────                  ──────────
• Accessibility audit      • Alternative ID paths     • Simplified onboarding
• User research refresh    • NHS number verification  • Biometric improvements
• Security baseline        • Performance optimisation • API gateway upgrade
• Trust integration push   • Helpdesk AI pilot        • Analytics dashboard
```

**Key Deliverables:**
- [ ] Complete WCAG AAA accessibility audit and remediation plan
- [ ] Launch bank-based identity verification pathway (no photo ID required)
- [ ] Implement NHS number + GP verification as alternative to photo ID
- [ ] Achieve 95% NHS trust integration
- [ ] Deploy AI-powered registration assistance
- [ ] Reduce average registration time to under 8 minutes

**Success Metrics:**
| Metric | Current | Target |
|--------|---------|--------|
| Registration completion rate | ~65% | 80% |
| Average registration time | 15 mins | 8 mins |
| Trust integration | 91% | 95% |
| User satisfaction (NPS) | +32 | +45 |

### Phase 2: Family & Proxy Access (2025-2026)
**Theme: "One Login, Whole Family"**

```
Q4 2025                    Q1 2026                    Q2 2026
─────────                  ─────────                  ─────────
• Proxy pilot expansion    • National proxy service   • Carer verification
• Parent verification      • Digital red book launch  • Cross-trust proxy
• Child profile linking    • Family dashboard MVP     • LPA integration
```

**Key Deliverables:**
- [ ] National rollout of proxy access (building on 68-surgery pilot)
- [ ] Launch digital 'red book' for child health records
- [ ] Implement one-time proxy registration (valid across all providers)
- [ ] Integrate Lasting Power of Attorney verification
- [ ] Deploy family health dashboard with unified view
- [ ] Enable proxy access across trust boundaries

**Success Metrics:**
| Metric | Current | Target |
|--------|---------|--------|
| Proxy access users | ~12,000 (pilot) | 2 million |
| Parent-child linkages | Manual | Automated |
| Carer verification time | Days | Hours |

### Phase 3: Intelligence & Personalisation (2026-2027)
**Theme: "Your Health, Your Way"**

```
Q3 2026                    Q4 2026                    2027
─────────                  ─────────                  ─────────
• My Companion AI launch   • Personalised dashboard   • Predictive access
• Health recommendations   • Contextual auth levels   • Risk-based security
• Smart notifications      • Wearable integration     • Voice authentication
```

**Key Deliverables:**
- [ ] Launch AI health companion (My Companion) integrated with login
- [ ] Implement adaptive authentication (context-aware security levels)
- [ ] Deploy personalised health dashboard based on conditions
- [ ] Enable wearable device data integration (Apple Health, Fitbit, etc.)
- [ ] Introduce voice-based authentication for accessibility
- [ ] Launch HealthStore for approved third-party app access

**Success Metrics:**
| Metric | Current | Target |
|--------|---------|--------|
| Personalised recommendations | None | 80% of users |
| Wearable integrations | None | 5+ platforms |
| AI assistant usage | N/A | 40% of sessions |

### Phase 4: Single Patient Record Integration (2027-2028)
**Theme: "One Record, Complete Picture"**

```
Q1-Q2 2027                 Q3-Q4 2027                 2028
──────────                 ──────────                 ─────────
• SPR pilot launch         • Secondary care records   • Full SPR access
• GP record consolidation  • Social care integration  • Genomics integration
• Lab results unification  • Mental health records    • Lifetime health passport
```

**Key Deliverables:**
- [ ] NHS login becomes gateway to Single Patient Record
- [ ] Unified view of primary, secondary, and community care records
- [ ] Integration with social care records (with appropriate consent)
- [ ] Mental health record access with enhanced consent controls
- [ ] Genomics data integration for personalised medicine
- [ ] Launch "lifetime health passport" - portable health identity

**Success Metrics:**
| Metric | Target |
|--------|--------|
| SPR access via NHS login | 100% |
| Records unified per patient | All care settings |
| Patient record views/month | 50 million |

### Phase 5: Ecosystem Leadership (2028+)
**Theme: "The NHS as Platform"**

```
2028                       2029                       2030+
─────────                  ─────────                  ─────────
• International standards  • Research data consent    • Cross-border health ID
• API marketplace launch   • Clinical trial matching  • Preventive health AI
• Third-party innovation   • Population health tools  • Genomic medicine scale
```

**Key Deliverables:**
- [ ] NHS login as platform for approved third-party innovation
- [ ] API marketplace for health app developers
- [ ] Consent-based research data sharing
- [ ] Clinical trial matching through identity platform
- [ ] Cross-border health identity (European interoperability)
- [ ] Population health analytics (anonymised, consented)

---

## 6. Key Features & Capabilities

### 6.1 Authentication Methods Roadmap

| Method | Current | 2025 | 2026 | 2027+ |
|--------|---------|------|------|-------|
| Password + SMS OTP | ✅ | ✅ | ✅ | ⚠️ Deprecate |
| Biometric (Face/Fingerprint) | ✅ | ✅ | ✅ | ✅ |
| FIDO2/Passkeys | ⚠️ Limited | ✅ | ✅ | ✅ Primary |
| Voice Authentication | ❌ | ⚠️ Pilot | ✅ | ✅ |
| NHS Smartcard Integration | ❌ | ✅ | ✅ | ✅ |
| Behavioural Biometrics | ❌ | ❌ | ⚠️ Pilot | ✅ |

### 6.2 Identity Verification Pathways

**Current State:** Photo ID + Face Match (or GP registration details)

**Future State (Multiple Pathways):**

```
                         ┌─────────────────────────────────────┐
                         │     NHS LOGIN VERIFICATION          │
                         │         PATHWAY OPTIONS             │
                         └─────────────────────────────────────┘
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        │                                 │                                 │
        ▼                                 ▼                                 ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   DIGITAL     │               │  IN-PERSON    │               │   ASSISTED    │
│   PATHWAYS    │               │   PATHWAYS    │               │   PATHWAYS    │
├───────────────┤               ├───────────────┤               ├───────────────┤
│ • Photo ID    │               │ • GP surgery  │               │ • Video call  │
│   + face scan │               │   verification│               │   with agent  │
│ • Bank-based  │               │ • NHS trust   │               │ • Telephone   │
│   verification│               │   identity hub│               │   verification│
│ • GOV.UK One  │               │ • Pharmacy    │               │ • Home visit  │
│   Login link  │               │   verification│               │   (vulnerable)│
│ • NHS number  │               │ • Post Office │               │ • Trusted     │
│   + knowledge │               │   Verify      │               │   referee     │
│   questions   │               │               │               │               │
└───────────────┘               └───────────────┘               └───────────────┘
```

### 6.3 Core Feature Set

#### My Identity
- Secure credential management
- Multi-device support
- Biometric enrollment
- Recovery options
- Audit log access

#### My Access
- Service connection management
- Consent dashboard
- Third-party app permissions
- Data sharing controls
- Access history

#### My Family
- Proxy access management
- Child profile linking
- Carer delegation
- Family health dashboard
- Shared appointment booking

#### My Preferences
- Communication preferences
- Language selection
- Accessibility settings
- Notification management
- Privacy controls

---

## 7. Accessibility & Inclusion Strategy

### 7.1 The Inclusion Imperative

The NHS serves everyone. NHS login must therefore be accessible to:

- **26% of population** with disabilities
- **18% of population** aged 65+
- **7.5 million people** with low literacy
- **5 million people** without smartphones
- **2 million people** without photo ID
- **Millions** with limited English proficiency

### 7.2 Accessibility Standards

| Standard | Current | Target |
|----------|---------|--------|
| WCAG Compliance | AA | AAA |
| Screen Reader Support | Partial | Full |
| Voice Navigation | None | Complete |
| Cognitive Accessibility | Limited | Comprehensive |
| Multi-language Support | 2 languages | 20+ languages |

### 7.3 Inclusive Design Principles

**1. Multiple Verification Pathways**
- No single method should be mandatory
- In-person options for those who cannot verify digitally
- Telephone support for non-digital users

**2. Adaptive Interface**
- Large text options (up to 300% zoom)
- High contrast modes
- Dyslexia-friendly fonts
- Simplified interface option
- Voice-guided navigation

**3. Language & Literacy**
- Plain English (reading age 12)
- British Sign Language videos
- Audio descriptions
- 20+ language translations
- Easy Read versions

**4. Device Agnostic**
- Works on older smartphones
- Desktop/laptop support
- Feature phone SMS fallback
- Offline capability for poor connectivity

### 7.4 Vulnerable User Protections

| User Group | Specific Accommodations |
|------------|------------------------|
| Elderly | Larger UI, voice support, carer access, phone support |
| Visually Impaired | Screen reader optimised, audio cues, voice auth |
| Hearing Impaired | Visual notifications, BSL videos, text chat support |
| Cognitive Disabilities | Simplified flows, picture-based options, easy read |
| Homeless/No Address | Alternative verification, trusted referee system |
| Domestic Abuse Survivors | Enhanced privacy, address protection, separate accounts |
| Mental Health Crisis | Crisis team access controls, advanced directive support |

---

## 8. Security & Trust Framework

### 8.1 Security Architecture Principles

**Zero Trust Model**
- Never trust, always verify
- Least privilege access
- Continuous authentication
- Micro-segmentation

**Privacy by Design**
- Data minimisation
- Purpose limitation
- Storage limitation
- User control

### 8.2 Security Controls

| Layer | Controls |
|-------|----------|
| Identity | Multi-factor auth, biometrics, liveness detection |
| Application | OWASP compliance, penetration testing, code review |
| Data | Encryption at rest/transit, tokenisation, masking |
| Network | DDoS protection, WAF, intrusion detection |
| Operations | SOC monitoring, incident response, threat intelligence |

### 8.3 Compliance Framework

| Requirement | Status |
|-------------|--------|
| UK GDPR | ✅ Compliant |
| NHS Data Security Standards | ✅ Compliant |
| DAPB3051 Identity Standard | ✅ Compliant |
| GPG45 Identity Proofing | ✅ Compliant |
| Cyber Essentials Plus | ✅ Certified |
| ISO 27001 | ✅ Certified |
| NIST Cybersecurity Framework | ✅ Aligned |

### 8.4 Trust Building Measures

**Transparency**
- Public security audit summaries
- Real-time service status
- Incident notification policy
- Clear privacy policy (plain English)

**User Control**
- Visible access audit logs
- Easy consent withdrawal
- Data export/deletion rights
- Granular sharing controls

**Accountability**
- Independent oversight board
- Annual public reporting
- Whistleblowing channels
- Regulatory engagement

---

## 9. Governance & Success Metrics

### 9.1 Governance Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    NHS LOGIN GOVERNANCE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              NHS ENGLAND BOARD                               │   │
│  │         (Strategic Oversight & Accountability)               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │         NHS LOGIN PROGRAMME BOARD                            │   │
│  │   (Cross-functional leadership, budget, priorities)         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│      ┌───────────────────────┼───────────────────────┐             │
│      │                       │                       │             │
│      ▼                       ▼                       ▼             │
│ ┌──────────┐          ┌──────────┐          ┌──────────┐          │
│ │ PRODUCT  │          │ SECURITY │          │ USER     │          │
│ │ COUNCIL  │          │ COUNCIL  │          │ ADVISORY │          │
│ │          │          │          │          │ GROUP    │          │
│ └──────────┘          └──────────┘          └──────────┘          │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              DELIVERY TEAMS                                  │   │
│  │  • Identity & Auth  • Integration  • Accessibility          │   │
│  │  • Security & Ops   • User Research  • Support              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 9.2 Key Performance Indicators

#### User Adoption Metrics

| KPI | 2025 Target | 2026 Target | 2028 Target |
|-----|-------------|-------------|-------------|
| Registered Users | 45 million | 50 million | 55 million |
| Monthly Active Users | 15 million | 25 million | 40 million |
| P9 Verified Users | 30 million | 40 million | 50 million |
| Proxy Access Users | 500,000 | 2 million | 5 million |

#### Experience Metrics

| KPI | 2025 Target | 2026 Target | 2028 Target |
|-----|-------------|-------------|-------------|
| Registration Completion Rate | 80% | 85% | 90% |
| Average Registration Time | 8 mins | 5 mins | 3 mins |
| User Satisfaction (NPS) | +45 | +55 | +65 |
| Accessibility Score | WCAG AA | WCAG AAA | WCAG AAA+ |

#### Operational Metrics

| KPI | 2025 Target | 2026 Target | 2028 Target |
|-----|-------------|-------------|-------------|
| Service Availability | 99.9% | 99.95% | 99.99% |
| Average Login Time | <3 sec | <2 sec | <1 sec |
| Support Ticket Volume | -20% | -40% | -60% |
| Cost per Verification | -15% | -30% | -50% |

#### Security Metrics

| KPI | 2025 Target | 2026 Target | 2028 Target |
|-----|-------------|-------------|-------------|
| Security Incidents (Critical) | 0 | 0 | 0 |
| Fraud Detection Rate | 99% | 99.5% | 99.9% |
| MFA Adoption Rate | 90% | 95% | 99% |
| Phishing Resistance | 95% | 98% | 99% |

### 9.3 Review Cadence

| Review Type | Frequency | Participants |
|-------------|-----------|--------------|
| Programme Board | Monthly | Senior leadership |
| Product Council | Fortnightly | Product, tech, design |
| Security Review | Weekly | Security, compliance |
| User Advisory | Quarterly | Patient representatives |
| External Audit | Annual | Third-party auditors |

---

## 10. Risk Assessment & Mitigation

### 10.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Security breach of identity data | Low | Critical | Zero trust architecture, encryption, monitoring, incident response |
| Low adoption among elderly/vulnerable | Medium | High | Multiple verification paths, assisted onboarding, carer access |
| Trust integration delays | Medium | Medium | Dedicated integration team, incentives, mandate timeline |
| GOV.UK One Login competition/overlap | Medium | Medium | Strategic alignment discussions, interoperability standards |
| Budget constraints | Medium | High | Phased delivery, business case for each phase, efficiency savings |
| Technology obsolescence | Low | Medium | Open standards, modular architecture, regular refresh cycles |
| Regulatory changes | Low | Medium | Regulatory engagement, flexible architecture, compliance monitoring |
| Staff capability gaps | Medium | Medium | Training, recruitment, partnerships |
| Third-party supplier failure | Low | High | Multi-vendor strategy, escrow arrangements, contingency planning |
| Cyber attack/state actor threat | Medium | Critical | NCSC partnership, threat intelligence, resilience testing |

### 10.2 Dependencies

| Dependency | Owner | Status | Risk if Delayed |
|------------|-------|--------|-----------------|
| Single Patient Record | NHS England | In Progress | Phase 4 delayed |
| NHS Trust EPR Integration | Individual Trusts | 91% complete | Inconsistent experience |
| GOV.UK One Login Alignment | GDS | Discussions | Duplicate effort |
| National Proxy Service | NHS England | Pilot | Phase 2 delayed |
| AI Governance Framework | DHSC | In Development | Phase 3 delayed |

---

## Appendix A: International System Comparison

| Feature | NHS Login | Estonia | Denmark | Australia | Epic MyChart |
|---------|-----------|---------|---------|-----------|--------------|
| **National Coverage** | England | 100% | 96% | 90% | N/A (provider) |
| **Auth Methods** | Biometric, MFA | PKI, Mobile ID | CPR + Digital Sig | myGov link | OAuth, Epic ID |
| **Health Records Access** | ✅ | ✅ | ✅ (since 1977) | ✅ | ✅ |
| **Proxy Access** | Pilot | ✅ | ✅ | ✅ | ✅ |
| **Audit Log Visibility** | Limited | ✅ Full | ✅ Full | ✅ | Partial |
| **Blockchain Integrity** | ❌ | ✅ KSI | ❌ | ❌ | ❌ |
| **Cross-Provider** | Developing | ✅ | ✅ | ✅ | Via MyChart Central |
| **API Ecosystem** | Developing | ✅ X-Road | ✅ | ✅ | ✅ |

---

## Appendix B: Glossary

| Term | Definition |
|------|------------|
| **DAPB3051** | NHS identity verification and authentication standard |
| **FIDO UAF** | Fast Identity Online Universal Authentication Framework |
| **GPG45** | Government guidance on identity proofing |
| **LPA** | Lasting Power of Attorney |
| **MFA** | Multi-Factor Authentication |
| **NPS** | National Proxy Service |
| **OIDC** | OpenID Connect authentication protocol |
| **P9** | Highest NHS login identity verification level |
| **PKI** | Public Key Infrastructure |
| **SPR** | Single Patient Record |
| **WCAG** | Web Content Accessibility Guidelines |

---

## Appendix C: References & Sources

### NHS & Government Sources
- [NHS Digital - NHS login](https://digital.nhs.uk/services/nhs-app)
- [NHS England - 10 Year Health Plan](https://www.england.nhs.uk/)
- [NHS App Roadmap](https://digital.nhs.uk/services/nhs-app/roadmap)
- [GOV.UK One Login](https://www.sign-in.service.gov.uk/)
- [NHS Identity Standards](https://standards.nhs.uk/published-standards/identity-verification-and-authentication-standard-for-digital-health-and-care-services)

### International Systems
- [e-Estonia Digital Healthcare](https://e-estonia.com/solutions/e-health-2/)
- [Denmark Sundhed.dk](https://www.sundhed.dk/borger/service/om-sundheddk/om-organisationen/ehealth-in-denmark/background/)
- [Australia My Health Record](https://www.digitalhealth.gov.au/initiatives-and-programs/my-health-record)
- [Epic MyChart](https://www.mychart.org/)

### Research & Analysis
- [HTN - NHS App Roadmap Analysis](https://htn.co.uk/2025/05/01/nhs-app-roadmap-outlines-health-records-appointments-prescriptions-integrated-services-and-messaging-plans/)
- [FIDO Alliance - NHS Case Study](https://fidoalliance.org/national-health-service-uses-fido-authentication-for-enhanced-login/)
- [PMC - Ageism in Healthcare Technology](https://pmc.ncbi.nlm.nih.gov/articles/PMC9277451/)
- [Digital Health - 10 Year Plan Analysis](https://www.digitalhealth.net/2025/07/what-does-the-10-year-plan-mean-for-digital/)

---

*Document prepared for NHS strategic planning purposes. This roadmap should be reviewed quarterly and updated based on policy changes, technology developments, and user feedback.*
