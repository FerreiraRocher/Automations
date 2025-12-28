# Comprehensive Debt Payment Workbook - Specifications

## Overview

A professional Excel workbook designed to help users systematically track, plan, and eliminate debt using proven payoff strategies. Inspired by popular budget systems like [Abby Organizes](https://abbyorganizes.com/products/annual-budget-spreadsheet) and tools from [Vertex42](https://www.vertex42.com/Calculators/debt-reduction-calculator.html) and [Tiller](https://tiller.com/debt-snowball-spreadsheet/).

---

## Workbook Structure (8 Sheets)

### 1. Dashboard
**Purpose:** Central hub providing at-a-glance overview of entire debt situation

**Features:**
- Total debt summary (original vs. current balance)
- Total monthly minimum payments
- Projected debt-free date
- Total interest to be paid
- Progress bar/percentage visualization
- Monthly payment vs. interest breakdown chart
- Debt composition pie chart
- Key metrics cards:
  - Number of active debts
  - Average interest rate
  - Largest debt
  - Smallest debt
  - Next debt to be paid off

### 2. Debt Inventory
**Purpose:** Master list of all debts with complete details

**Fields per debt (up to 25 debts):**
| Field | Description |
|-------|-------------|
| Debt Name | Creditor/account name |
| Debt Type | Dropdown: Credit Card, Student Loan, Auto Loan, Mortgage, Personal Loan, Medical, Other |
| Original Balance | Starting debt amount |
| Current Balance | Current amount owed |
| Interest Rate (APR) | Annual percentage rate |
| Minimum Payment | Required monthly minimum |
| Due Date | Day of month payment is due |
| Account Number | Last 4 digits (optional) |
| Start Date | When debt was incurred |
| Notes | Additional information |

**Calculated Fields:**
- Monthly interest charge
- Months to payoff (minimum payments only)
- Total interest if minimum payments only
- Payoff date (minimum payments only)

### 3. Strategy Selector
**Purpose:** Compare and select debt payoff strategy

**Available Strategies:**
1. **Debt Snowball** (Lowest Balance First)
   - Psychological wins
   - Faster to see first debt eliminated
   - Popular Dave Ramsey method

2. **Debt Avalanche** (Highest Interest First)
   - Mathematically optimal
   - Saves most money on interest
   - May take longer for first payoff

3. **Custom Order**
   - User-defined priority ranking
   - Flexible based on personal circumstances

**Comparison Display:**
- Side-by-side comparison of all three methods
- Total interest paid under each strategy
- Time to debt-free under each strategy
- Interest savings vs. minimum payments
- Recommended strategy based on user's situation

### 4. Payment Schedule
**Purpose:** Month-by-month payment plan based on selected strategy

**Layout:**
- Rows: Each month from start to projected payoff
- Columns: Each debt + totals
- Shows for each debt per month:
  - Payment amount
  - Principal paid
  - Interest charged
  - Remaining balance

**Features:**
- Extra payment allocation field (monthly)
- Snowball rollover calculations (when debt paid off, payment rolls to next)
- Running totals for interest and principal
- Visual indicators when debt reaches $0
- Cumulative interest paid
- Cumulative principal paid

### 5. Payment Tracker
**Purpose:** Log actual payments made throughout the year

**Monthly Tracking Grid (12 months x all debts):**
| Field | Description |
|-------|-------------|
| Planned Payment | From payment schedule |
| Actual Payment | User-entered |
| Variance | Difference (over/under) |
| Payment Date | When paid |
| Confirmation # | Optional reference |

**Tracking Features:**
- Monthly summary totals
- Year-to-date progress
- Streak tracker (consecutive on-time payments)
- Comparison: planned vs. actual progress

### 6. Extra Payment Calculator
**Purpose:** Model impact of additional payments

**Scenario Modeling:**
- Input: Extra payment amount (one-time or monthly)
- Output:
  - New payoff date
  - Interest saved
  - Time saved (months)
  - Comparison chart: with vs. without extra payments

**Features:**
- Lump sum payment calculator
- Tax refund/bonus allocation planner
- Side income allocation tracker
- "What if" scenarios:
  - Extra $50/month
  - Extra $100/month
  - Extra $250/month
  - Extra $500/month
  - Custom amount

### 7. Progress & Milestones
**Purpose:** Celebrate wins and track achievements

**Visual Progress:**
- Debt payoff thermometer (goal visual)
- Percentage bars for each debt
- Monthly balance trend chart
- Interest vs. principal trend chart

**Milestones:**
- First debt paid off (date & celebration)
- 25% debt eliminated
- 50% debt eliminated
- 75% debt eliminated
- Halfway point (by number of debts)
- Each individual debt payoff date
- Debt-free date countdown

**Motivation Section:**
- Space for "Why I'm paying off debt" goal
- Reward planning for milestones
- Debt-free celebration plans

### 8. Annual Summary
**Purpose:** Year-over-year comparison and reporting

**Annual Metrics:**
- Starting balance (Jan 1)
- Ending balance (Dec 31)
- Total paid during year
- Total interest paid
- Total principal paid
- Number of debts eliminated
- Net worth impact

**Comparison Features:**
- Year-over-year progress chart
- Projected vs. actual performance
- Next year projections

---

## Technical Specifications

### Data Validation
- Dropdown lists for debt types
- Date pickers for due dates
- Percentage formatting for interest rates
- Currency formatting for all monetary values
- Input validation for realistic ranges

### Formulas & Calculations
- PMT function for payment calculations
- IPMT/PPMT for interest/principal splits
- Compound interest calculations
- Amortization schedule generation
- Conditional formatting for overdue/completed items

### Formatting & Design
- Professional color scheme (blue/green financial theme)
- Clear section headers
- Locked formula cells (protection)
- Print-friendly layouts
- Conditional formatting:
  - Red: Overdue/negative
  - Yellow: Warning/attention needed
  - Green: Paid off/on track
  - Gray: Future/projected

### Charts & Visualizations
1. Debt composition pie chart
2. Payment breakdown bar chart (interest vs. principal)
3. Balance trend line chart
4. Payoff timeline Gantt-style chart
5. Progress thermometer/gauge
6. Strategy comparison bar chart
7. Monthly payment waterfall chart

---

## User Experience Features

### Automation
- Auto-calculate totals and projections
- Auto-sort debts by selected strategy
- Auto-rollover payments when debt paid off
- Auto-update dashboard from source data

### Instructions
- Setup instructions on first sheet
- Tooltips/comments on complex fields
- Example data (can be cleared)
- Color-coded input vs. calculated cells:
  - Light blue: User input
  - Light gray: Calculated (do not edit)

### Protection
- Protected formula cells
- Unprotected input cells
- Optional password protection

---

## File Details

- **Format:** .xlsx (Excel 2016+ compatible)
- **Size:** Optimized for performance
- **Compatibility:** Microsoft Excel, Google Sheets (with some limitations)
- **Print Areas:** Defined for key sheets

---

## Implementation Priority

1. **Phase 1 (Core):**
   - Dashboard
   - Debt Inventory
   - Strategy Selector
   - Payment Schedule

2. **Phase 2 (Tracking):**
   - Payment Tracker
   - Progress & Milestones

3. **Phase 3 (Advanced):**
   - Extra Payment Calculator
   - Annual Summary

---

## Sources & Inspiration

- [Abby Organizes Annual Budget System](https://abbyorganizes.com/products/annual-budget-spreadsheet)
- [Vertex42 Debt Reduction Calculator](https://www.vertex42.com/Calculators/debt-reduction-calculator.html)
- [Tiller Debt Payoff Planner](https://tiller.com/debt-snowball-spreadsheet/)
- [Undebt.it Online Calculator](https://undebt.it/)
- [Moneyzine Debt Avalanche Spreadsheet](https://moneyzine.com/debt-consolidation/debt-avalanche-spreadsheet/)
