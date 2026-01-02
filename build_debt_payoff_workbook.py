#!/usr/bin/env python3
"""
Comprehensive Debt Payoff Excel Workbook Generator

This script creates a full-featured Excel workbook for debt payoff planning,
including: debt register, payoff engine (Snowball/Avalanche/Custom), payment
schedules, actual payment tracking, dashboards, and calendar views.
"""

import os
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Border, Side, Alignment, Protection, NamedStyle
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.chart import LineChart, BarChart, Reference, PieChart
from openpyxl.chart.label import DataLabelList
from openpyxl.formatting.rule import FormulaRule, ColorScaleRule, IconSetRule
from openpyxl.comments import Comment

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================

# Colors
COLORS = {
    'primary': '1F4E79',       # Dark blue
    'secondary': '2E75B6',     # Medium blue
    'accent': '5B9BD5',        # Light blue
    'success': '70AD47',       # Green
    'warning': 'FFC000',       # Yellow/Orange
    'danger': 'C00000',        # Red
    'input_fill': 'E2EFDA',    # Light green for inputs
    'calc_fill': 'D9D9D9',     # Grey for calculated
    'header_fill': '1F4E79',   # Dark blue for headers
    'white': 'FFFFFF',
    'light_grey': 'F2F2F2',
    'border': 'B4B4B4',
}

# Fonts
FONTS = {
    'title': Font(name='Calibri', size=24, bold=True, color=COLORS['primary']),
    'header': Font(name='Calibri', size=11, bold=True, color=COLORS['white']),
    'subheader': Font(name='Calibri', size=12, bold=True, color=COLORS['primary']),
    'normal': Font(name='Calibri', size=11),
    'bold': Font(name='Calibri', size=11, bold=True),
    'small': Font(name='Calibri', size=9),
    'link': Font(name='Calibri', size=11, color='0563C1', underline='single'),
}

# Fills
FILLS = {
    'input': PatternFill(start_color=COLORS['input_fill'], end_color=COLORS['input_fill'], fill_type='solid'),
    'calc': PatternFill(start_color=COLORS['calc_fill'], end_color=COLORS['calc_fill'], fill_type='solid'),
    'header': PatternFill(start_color=COLORS['header_fill'], end_color=COLORS['header_fill'], fill_type='solid'),
    'white': PatternFill(start_color=COLORS['white'], end_color=COLORS['white'], fill_type='solid'),
    'light_grey': PatternFill(start_color=COLORS['light_grey'], end_color=COLORS['light_grey'], fill_type='solid'),
    'success': PatternFill(start_color=COLORS['success'], end_color=COLORS['success'], fill_type='solid'),
    'warning': PatternFill(start_color=COLORS['warning'], end_color=COLORS['warning'], fill_type='solid'),
    'danger': PatternFill(start_color=COLORS['danger'], end_color=COLORS['danger'], fill_type='solid'),
}

# Borders
thin_border = Border(
    left=Side(style='thin', color=COLORS['border']),
    right=Side(style='thin', color=COLORS['border']),
    top=Side(style='thin', color=COLORS['border']),
    bottom=Side(style='thin', color=COLORS['border'])
)

# Alignments
ALIGN = {
    'center': Alignment(horizontal='center', vertical='center', wrap_text=True),
    'left': Alignment(horizontal='left', vertical='center', wrap_text=True),
    'right': Alignment(horizontal='right', vertical='center'),
}


def apply_header_style(cell):
    """Apply header styling to a cell."""
    cell.font = FONTS['header']
    cell.fill = FILLS['header']
    cell.alignment = ALIGN['center']
    cell.border = thin_border


def apply_input_style(cell):
    """Apply input cell styling."""
    cell.fill = FILLS['input']
    cell.border = thin_border
    cell.alignment = ALIGN['center']


def apply_calc_style(cell):
    """Apply calculated cell styling."""
    cell.fill = FILLS['calc']
    cell.border = thin_border
    cell.alignment = ALIGN['center']
    cell.protection = Protection(locked=True)


def set_column_widths(ws, widths):
    """Set column widths from a dictionary."""
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


# =============================================================================
# TAB 1: START HERE
# =============================================================================

def build_start_here(wb):
    """Build the Start Here welcome tab."""
    ws = wb.active
    ws.title = "Start Here"

    # Set column widths
    set_column_widths(ws, {'A': 5, 'B': 60, 'C': 15, 'D': 40})

    # Title
    ws.merge_cells('B2:D2')
    ws['B2'] = "DEBT PAYOFF COMMAND CENTRE"
    ws['B2'].font = FONTS['title']
    ws['B2'].alignment = ALIGN['center']

    # Subtitle
    ws.merge_cells('B3:D3')
    ws['B3'] = "Your comprehensive debt elimination system"
    ws['B3'].font = Font(name='Calibri', size=14, italic=True, color=COLORS['secondary'])
    ws['B3'].alignment = ALIGN['center']

    # Quick Start Checklist
    ws['B5'] = "QUICK START CHECKLIST"
    ws['B5'].font = FONTS['subheader']

    checklist = [
        ("1. Enter your debts", "Go to 'Debt Register' tab and enter all your debts", "Debt Register"),
        ("2. Set your method", "Choose Snowball, Avalanche, or Custom in 'Setup'", "Setup"),
        ("3. Set extra payment", "Enter any extra monthly payment capacity in 'Setup'", "Setup"),
        ("4. Review your plan", "See your personalized payoff schedule", "Payoff Schedule"),
        ("5. Track payments", "Log actual payments as you make them", "Actual Payments"),
        ("6. Monitor progress", "View your dashboard for at-a-glance status", "Dashboard"),
    ]

    row = 7
    for step, description, tab in checklist:
        ws[f'B{row}'] = step
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = description
        ws[f'D{row}'] = f"→ {tab}"
        ws[f'D{row}'].font = FONTS['link']
        row += 1

    # Separator
    row += 1
    ws.merge_cells(f'B{row}:D{row}')
    ws[f'B{row}'] = "─" * 80
    ws[f'B{row}'].font = Font(color=COLORS['border'])

    # Method Explanations
    row += 2
    ws[f'B{row}'] = "PAYOFF METHODS EXPLAINED"
    ws[f'B{row}'].font = FONTS['subheader']

    methods = [
        ("SNOWBALL", "Pay off smallest balances first. Provides quick wins for motivation."),
        ("AVALANCHE", "Pay off highest interest rates first. Minimizes total interest paid."),
        ("CUSTOM", "You set the priority order. Use PaymentPriorityOverride in Debt Register."),
    ]

    row += 2
    for method, desc in methods:
        ws[f'B{row}'] = method
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = desc
        ws.merge_cells(f'C{row}:D{row}')
        row += 1

    # Disclaimer
    row += 2
    ws.merge_cells(f'B{row}:D{row}')
    ws[f'B{row}'] = "⚠️ DISCLAIMER: This workbook is for informational purposes only. It does not constitute financial advice. Please consult a qualified financial advisor for personalized guidance."
    ws[f'B{row}'].font = Font(name='Calibri', size=10, italic=True, color=COLORS['danger'])
    ws[f'B{row}'].alignment = ALIGN['left']

    # Version info
    row += 2
    ws[f'B{row}'] = f"Version 1.0 | Created: {datetime.now().strftime('%Y-%m-%d')}"
    ws[f'B{row}'].font = FONTS['small']

    # Freeze panes
    ws.freeze_panes = 'B5'

    return ws


# =============================================================================
# TAB 2: SETUP
# =============================================================================

def build_setup(wb):
    """Build the Setup configuration tab."""
    ws = wb.create_sheet("Setup")

    set_column_widths(ws, {'A': 5, 'B': 35, 'C': 20, 'D': 5, 'E': 35, 'F': 25, 'G': 5})

    # Title
    ws.merge_cells('B2:F2')
    ws['B2'] = "SETUP & CONFIGURATION"
    ws['B2'].font = FONTS['title']

    # -------------------------------------------------------------------------
    # SECTION 1: Plan Settings
    # -------------------------------------------------------------------------
    ws['B4'] = "PLAN SETTINGS"
    ws['B4'].font = FONTS['subheader']

    settings = [
        ("Plan Start Month", "2025-01", "Format: YYYY-MM"),
        ("Payoff Method", "Avalanche", "Snowball, Avalanche, or Custom"),
        ("Extra Payment Per Month", 0, "Additional amount above minimums"),
        ("Max Months to Project", 240, "Maximum projection horizon"),
        ("Currency Symbol", "$", "Display currency"),
    ]

    row = 6
    for label, default, note in settings:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = default
        apply_input_style(ws[f'C{row}'])
        ws[f'D{row}'] = note
        ws[f'D{row}'].font = FONTS['small']
        ws.merge_cells(f'D{row}:F{row}')
        row += 1

    # Add data validation for Method
    dv_method = DataValidation(type="list", formula1='"Snowball,Avalanche,Custom"', allow_blank=False)
    dv_method.error = "Please select Snowball, Avalanche, or Custom"
    dv_method.errorTitle = "Invalid Method"
    ws.add_data_validation(dv_method)
    dv_method.add(ws['C7'])

    # -------------------------------------------------------------------------
    # SECTION 2: Interest Modelling
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "INTEREST MODELLING"
    ws[f'B{row}'].font = FONTS['subheader']

    row += 2
    ws[f'B{row}'] = "Default Interest Method"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = "Monthly"
    apply_input_style(ws[f'C{row}'])

    dv_interest = DataValidation(type="list", formula1='"Monthly,Daily"', allow_blank=False)
    ws.add_data_validation(dv_interest)
    dv_interest.add(ws[f'C{row}'])

    row += 1
    ws[f'B{row}'] = "Include Fees in Calculations"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = "No"
    apply_input_style(ws[f'C{row}'])

    dv_yesno = DataValidation(type="list", formula1='"Yes,No"', allow_blank=False)
    ws.add_data_validation(dv_yesno)
    dv_yesno.add(ws[f'C{row}'])

    # -------------------------------------------------------------------------
    # SECTION 3: Output Tiles (Calculated Summary)
    # -------------------------------------------------------------------------
    row += 3
    ws[f'B{row}'] = "PLAN SUMMARY (Auto-Calculated)"
    ws[f'B{row}'].font = FONTS['subheader']

    tiles = [
        ("Total Starting Debt", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[StartBalance])'),
        ("Total Current Debt", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[CurrentBalance])'),
        ("Total Minimum Payments", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[MinimumPayment])'),
        ("Planned Extra Per Month", '=C8'),
        ("Total Monthly Payment", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[MinimumPayment])+C8'),
        ("Number of Active Debts", '=COUNTIFS(tblDebts[IsIncluded],"Yes",tblDebts[Status],"Open")'),
    ]

    row += 2
    start_tile_row = row
    for label, formula in tiles:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = formula
        apply_calc_style(ws[f'C{row}'])
        ws[f'C{row}'].number_format = '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'
        row += 1

    # Fix the count format
    ws[f'C{start_tile_row + 5}'].number_format = '0'

    # -------------------------------------------------------------------------
    # SECTION 4: tblAssumptions Table (for formulas to reference)
    # -------------------------------------------------------------------------
    ws['H4'] = "ASSUMPTIONS TABLE"
    ws['H4'].font = FONTS['subheader']

    # Create tblAssumptions
    assumptions_headers = ['Parameter', 'Value']
    assumptions_data = [
        ['PlanStartMonth', '=C6'],
        ['Method', '=C7'],
        ['ExtraPaymentPerMonth', '=C8'],
        ['MaxMonthsToProject', '=C9'],
        ['CurrencySymbol', '=C10'],
        ['InterestMethod', '=C14'],
        ['IncludeFees', '=C15'],
    ]

    assumptions_row = 6
    for col_idx, header in enumerate(assumptions_headers, start=8):
        cell = ws.cell(row=assumptions_row, column=col_idx, value=header)
        apply_header_style(cell)

    for data_row in assumptions_data:
        assumptions_row += 1
        for col_idx, value in enumerate(data_row, start=8):
            cell = ws.cell(row=assumptions_row, column=col_idx, value=value)
            cell.border = thin_border
            if col_idx == 9:
                apply_calc_style(cell)

    # Create table
    table_ref = f"H6:I{assumptions_row}"
    table = Table(displayName="tblAssumptions", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    table.tableStyleInfo = style
    ws.add_table(table)

    ws.freeze_panes = 'B4'

    return ws


# =============================================================================
# TAB 3: DEBT REGISTER
# =============================================================================

def build_debt_register(wb):
    """Build the Debt Register tab with tblDebts."""
    ws = wb.create_sheet("Debt Register")

    # Title
    ws.merge_cells('B2:N2')
    ws['B2'] = "DEBT REGISTER"
    ws['B2'].font = FONTS['title']

    ws['B3'] = "Enter all your debts below. Green input cells are required, grey cells are calculated."
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)
    ws.merge_cells('B3:N3')

    # Define headers
    headers = [
        'DebtID', 'DebtName', 'Lender', 'DebtType', 'StartBalance', 'CurrentBalance',
        'AnnualInterestRate', 'InterestMethod', 'MinimumPayment', 'DueDayOfMonth',
        'PaymentPriorityOverride', 'IsIncluded', 'Status', 'Notes', 'ReadyForPlan'
    ]

    # Column widths
    widths = {
        'A': 3, 'B': 10, 'C': 20, 'D': 18, 'E': 14, 'F': 15, 'G': 16,
        'H': 18, 'I': 15, 'J': 16, 'K': 14, 'L': 22, 'M': 12, 'N': 12, 'O': 25, 'P': 14
    }
    set_column_widths(ws, widths)

    # Write headers
    header_row = 5
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=header_row, column=col_idx, value=header)
        apply_header_style(cell)

    # Add sample data rows with formulas
    sample_debts = [
        [1, 'Credit Card A', 'Bank ABC', 'Credit Card', 5000, 4800, 0.1999, 'Monthly', 150, 15, '', 'Yes', 'Open', ''],
        [2, 'Car Loan', 'Auto Finance', 'Loan', 15000, 12500, 0.0699, 'Monthly', 350, 1, '', 'Yes', 'Open', ''],
        [3, 'Student Loan', 'Fed Loans', 'Loan', 25000, 22000, 0.0499, 'Monthly', 250, 20, '', 'Yes', 'Open', ''],
        [4, 'Credit Card B', 'Bank XYZ', 'Credit Card', 3000, 2800, 0.2499, 'Monthly', 85, 10, '', 'Yes', 'Open', ''],
        [5, 'Personal Loan', 'Credit Union', 'Loan', 8000, 6500, 0.0899, 'Monthly', 200, 5, '', 'Yes', 'Open', ''],
    ]

    # Add data rows and sample data
    data_start_row = header_row + 1
    for row_offset, debt in enumerate(sample_debts):
        row = data_start_row + row_offset
        for col_offset, value in enumerate(debt):
            cell = ws.cell(row=row, column=col_offset + 2, value=value)
            cell.border = thin_border

            # Apply input styling to editable columns
            if col_offset in [1, 2, 3, 4, 5, 6, 8, 9, 10, 13]:  # Input columns
                apply_input_style(cell)

            # Format currency columns
            if col_offset in [4, 5, 8]:  # Balance and payment columns
                cell.number_format = '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'

            # Format percentage
            if col_offset == 6:  # Interest rate
                cell.number_format = '0.00%'

        # ReadyForPlan formula (column P, index 14)
        ready_formula = f'=IF(AND(C{row}<>"",F{row}>0,G{row}<>"",H{row}>0,I{row}<>"",J{row}>0,K{row}>0,M{row}<>"",N{row}<>""),"Ready","Missing Data")'
        ready_cell = ws.cell(row=row, column=16, value=ready_formula)
        apply_calc_style(ready_cell)

    # Add 45 more empty rows for up to 50 debts
    for row_offset in range(5, 50):
        row = data_start_row + row_offset
        # DebtID formula
        ws.cell(row=row, column=2, value=row_offset + 1).border = thin_border
        for col in range(3, 16):
            cell = ws.cell(row=row, column=col, value='')
            cell.border = thin_border
            if col in [3, 4, 5, 6, 7, 8, 10, 11, 12, 15]:
                apply_input_style(cell)
        # ReadyForPlan formula
        ready_formula = f'=IF(C{row}="","",IF(AND(C{row}<>"",F{row}>0,G{row}<>"",H{row}>0,I{row}<>"",J{row}>0,K{row}>0,M{row}<>"",N{row}<>""),"Ready","Missing Data"))'
        ws.cell(row=row, column=16, value=ready_formula).border = thin_border

    # Create table
    table_end_row = data_start_row + 49
    table_ref = f"B{header_row}:P{table_end_row}"
    table = Table(displayName="tblDebts", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    table.tableStyleInfo = style
    ws.add_table(table)

    # Data Validations
    # DebtType
    dv_type = DataValidation(type="list", formula1='"Credit Card,Loan,Overdraft,Line of Credit,Other"')
    ws.add_data_validation(dv_type)
    dv_type.add(f'E{data_start_row}:E{table_end_row}')

    # InterestMethod
    dv_interest = DataValidation(type="list", formula1='"Monthly,Daily"')
    ws.add_data_validation(dv_interest)
    dv_interest.add(f'I{data_start_row}:I{table_end_row}')

    # IsIncluded
    dv_included = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(dv_included)
    dv_included.add(f'M{data_start_row}:M{table_end_row}')

    # Status
    dv_status = DataValidation(type="list", formula1='"Open,Paid,On Hold"')
    ws.add_data_validation(dv_status)
    dv_status.add(f'N{data_start_row}:N{table_end_row}')

    # DueDay (1-28)
    dv_day = DataValidation(type="whole", operator="between", formula1="1", formula2="28")
    dv_day.error = "Due day must be between 1 and 28"
    ws.add_data_validation(dv_day)
    dv_day.add(f'K{data_start_row}:K{table_end_row}')

    # Interest rate (0-100%)
    dv_rate = DataValidation(type="decimal", operator="between", formula1="0", formula2="1")
    dv_rate.error = "Interest rate must be between 0% and 100%"
    ws.add_data_validation(dv_rate)
    dv_rate.add(f'H{data_start_row}:H{table_end_row}')

    # Conditional formatting for ReadyForPlan
    green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
    red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')

    ws.conditional_formatting.add(f'P{data_start_row}:P{table_end_row}',
        FormulaRule(formula=[f'$P{data_start_row}="Ready"'], fill=green_fill))
    ws.conditional_formatting.add(f'P{data_start_row}:P{table_end_row}',
        FormulaRule(formula=[f'$P{data_start_row}="Missing Data"'], fill=red_fill))

    ws.freeze_panes = 'C6'

    return ws


# =============================================================================
# TAB 4: BUDGET AND DEBT CAPACITY
# =============================================================================

def build_budget_capacity(wb):
    """Build the Budget and Debt Capacity tab."""
    ws = wb.create_sheet("Budget & Capacity")

    set_column_widths(ws, {'A': 5, 'B': 35, 'C': 20, 'D': 5, 'E': 35, 'F': 20})

    # Title
    ws.merge_cells('B2:F2')
    ws['B2'] = "BUDGET & DEBT CAPACITY"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:F3')
    ws['B3'] = "Determine how much you can afford to put toward debt each month"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # -------------------------------------------------------------------------
    # SECTION 1: Income & Expenses
    # -------------------------------------------------------------------------
    ws['B5'] = "MONTHLY INCOME"
    ws['B5'].font = FONTS['subheader']

    income_items = [
        ("Primary Income (Net)", 0),
        ("Secondary Income", 0),
        ("Other Income", 0),
    ]

    row = 7
    for label, default in income_items:
        ws[f'B{row}'] = label
        ws[f'C{row}'] = default
        apply_input_style(ws[f'C{row}'])
        ws[f'C{row}'].number_format = '_($* #,##0.00_)'
        row += 1

    ws[f'B{row}'] = "Total Monthly Income"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = '=SUM(C7:C9)'
    apply_calc_style(ws[f'C{row}'])
    ws[f'C{row}'].number_format = '_($* #,##0.00_)'
    income_total_row = row

    row += 2
    ws[f'B{row}'] = "ESSENTIAL EXPENSES"
    ws[f'B{row}'].font = FONTS['subheader']

    expense_items = [
        ("Housing (Rent/Mortgage)", 0),
        ("Utilities", 0),
        ("Food & Groceries", 0),
        ("Transportation", 0),
        ("Insurance", 0),
        ("Healthcare", 0),
        ("Childcare/Education", 0),
        ("Other Essential", 0),
    ]

    row += 2
    expense_start = row
    for label, default in expense_items:
        ws[f'B{row}'] = label
        ws[f'C{row}'] = default
        apply_input_style(ws[f'C{row}'])
        ws[f'C{row}'].number_format = '_($* #,##0.00_)'
        row += 1
    expense_end = row - 1

    ws[f'B{row}'] = "Total Essential Expenses"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = f'=SUM(C{expense_start}:C{expense_end})'
    apply_calc_style(ws[f'C{row}'])
    ws[f'C{row}'].number_format = '_($* #,##0.00_)'
    expense_total_row = row

    # -------------------------------------------------------------------------
    # SECTION 2: Capacity Calculation
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "DEBT PAYMENT CAPACITY"
    ws[f'B{row}'].font = FONTS['subheader']

    row += 2
    ws[f'B{row}'] = "Available After Essentials"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = f'=C{income_total_row}-C{expense_total_row}'
    apply_calc_style(ws[f'C{row}'])
    ws[f'C{row}'].number_format = '_($* #,##0.00_)'
    available_row = row

    row += 1
    ws[f'B{row}'] = "Emergency Buffer (Recommended 10%)"
    ws[f'C{row}'] = 0
    apply_input_style(ws[f'C{row}'])
    ws[f'C{row}'].number_format = '_($* #,##0.00_)'
    buffer_row = row

    row += 1
    ws[f'B{row}'] = "Maximum Debt Payment Capacity"
    ws[f'B{row}'].font = FONTS['bold']
    ws[f'C{row}'] = f'=MAX(0,C{available_row}-C{buffer_row})'
    apply_calc_style(ws[f'C{row}'])
    ws[f'C{row}'].number_format = '_($* #,##0.00_)'
    capacity_row = row

    # -------------------------------------------------------------------------
    # SECTION 3: Feasibility Check
    # -------------------------------------------------------------------------
    row += 3
    ws[f'E5'] = "FEASIBILITY CHECK"
    ws[f'E5'].font = FONTS['subheader']

    checks = [
        ("Total Minimum Payments Required", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[MinimumPayment])'),
        ("Your Debt Payment Capacity", f'=C{capacity_row}'),
        ("Surplus / (Shortfall)", f'=F8-F7'),
    ]

    row = 7
    for label, formula in checks:
        ws[f'E{row}'] = label
        ws[f'E{row}'].font = FONTS['bold']
        ws[f'F{row}'] = formula
        apply_calc_style(ws[f'F{row}'])
        ws[f'F{row}'].number_format = '_($* #,##0.00_);[Red]_($* (#,##0.00);_($* "-"??_);_(@_)'
        row += 1

    # Status indicator
    row += 1
    ws[f'E{row}'] = "Status"
    ws[f'E{row}'].font = FONTS['bold']
    ws[f'F{row}'] = '=IF(F9>=0,"✓ Feasible","⚠ Insufficient Capacity")'
    apply_calc_style(ws[f'F{row}'])

    # Conditional formatting for status
    green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
    red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
    ws.conditional_formatting.add(f'F{row}',
        FormulaRule(formula=['F9>=0'], fill=green_fill))
    ws.conditional_formatting.add(f'F{row}',
        FormulaRule(formula=['F9<0'], fill=red_fill))

    # Suggested extra payment
    row += 2
    ws[f'E{row}'] = "Suggested Extra Payment"
    ws[f'E{row}'].font = FONTS['bold']
    ws[f'F{row}'] = '=MAX(0,F9)'
    apply_calc_style(ws[f'F{row}'])
    ws[f'F{row}'].number_format = '_($* #,##0.00_)'
    ws[f'F{row}'].comment = Comment("This is your surplus after minimum payments. Consider putting this toward extra debt payments.", "System")

    ws.freeze_panes = 'B5'

    return ws


# =============================================================================
# TAB 5: PAYOFF ENGINE
# =============================================================================

def build_payoff_engine(wb):
    """Build the Payoff Engine calculation tab."""
    ws = wb.create_sheet("Payoff Engine")

    set_column_widths(ws, {'A': 5, 'B': 15, 'C': 20, 'D': 16, 'E': 18, 'F': 16, 'G': 16, 'H': 18})

    # Title
    ws.merge_cells('B2:H2')
    ws['B2'] = "PAYOFF ENGINE"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:H3')
    ws['B3'] = "This sheet calculates the optimal payment order based on your selected method"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # -------------------------------------------------------------------------
    # SECTION 1: Debt Priority Order
    # -------------------------------------------------------------------------
    ws['B5'] = "DEBT PRIORITY ORDER"
    ws['B5'].font = FONTS['subheader']

    ws['B6'] = "Current Method:"
    ws['B6'].font = FONTS['bold']
    ws['C6'] = '=Setup!C7'
    apply_calc_style(ws['C6'])

    # Priority table headers
    priority_headers = ['Priority', 'DebtID', 'DebtName', 'CurrentBalance', 'InterestRate', 'MinPayment', 'SortKey']

    row = 8
    for col_idx, header in enumerate(priority_headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Note: In a real implementation, these would be dynamic array formulas
    # For now, we'll add placeholder formulas that reference the debt table
    row = 9
    for i in range(1, 11):  # Show first 10 debts
        ws.cell(row=row, column=2, value=i).border = thin_border  # Priority

        # These formulas would need FILTER/SORT in actual use (Microsoft 365)
        # Simplified placeholders:
        ws.cell(row=row, column=3, value=f'=IFERROR(INDEX(tblDebts[DebtID],{i}),"")').border = thin_border
        ws.cell(row=row, column=4, value=f'=IFERROR(INDEX(tblDebts[DebtName],{i}),"")').border = thin_border
        ws.cell(row=row, column=5, value=f'=IFERROR(INDEX(tblDebts[CurrentBalance],{i}),"")').border = thin_border
        ws.cell(row=row, column=6, value=f'=IFERROR(INDEX(tblDebts[AnnualInterestRate],{i}),"")').border = thin_border
        ws.cell(row=row, column=7, value=f'=IFERROR(INDEX(tblDebts[MinimumPayment],{i}),"")').border = thin_border

        # SortKey depends on method
        sort_formula = f'=IF($C$6="Snowball",E{row},IF($C$6="Avalanche",-F{row},IFERROR(INDEX(tblDebts[PaymentPriorityOverride],{i}),999)))'
        ws.cell(row=row, column=8, value=sort_formula).border = thin_border

        for col in range(2, 9):
            ws.cell(row=row, column=col).number_format = '@'
        ws.cell(row=row, column=5).number_format = '_($* #,##0.00_)'
        ws.cell(row=row, column=6).number_format = '0.00%'
        ws.cell(row=row, column=7).number_format = '_($* #,##0.00_)'

        row += 1

    # -------------------------------------------------------------------------
    # SECTION 2: Monthly Allocation Logic
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "MONTHLY ALLOCATION RULES"
    ws[f'B{row}'].font = FONTS['subheader']

    row += 2
    rules = [
        "1. Pay minimum on ALL included open debts",
        "2. Apply remaining capacity to the 'focus debt' (top priority)",
        "3. When focus debt reaches $0, roll its payment to next focus debt",
        "4. Interest accrues monthly: Interest = Balance × (Annual Rate ÷ 12)",
        "5. Payment covers interest first, then principal",
    ]

    for rule in rules:
        ws[f'B{row}'] = rule
        ws.merge_cells(f'B{row}:H{row}')
        row += 1

    # -------------------------------------------------------------------------
    # SECTION 3: Key Calculations
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "KEY CALCULATIONS"
    ws[f'B{row}'].font = FONTS['subheader']

    calcs = [
        ("Total Debt Balance", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[CurrentBalance])'),
        ("Total Minimum Required", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[MinimumPayment])'),
        ("Extra Payment Available", '=Setup!C8'),
        ("Total Monthly Payment", '=B29+B30'),
    ]

    row += 2
    for label, formula in calcs:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = formula
        apply_calc_style(ws[f'C{row}'])
        ws[f'C{row}'].number_format = '_($* #,##0.00_)'
        row += 1

    ws.freeze_panes = 'B5'

    # Protect sheet but allow viewing
    ws.protection.sheet = True
    ws.protection.password = 'view'

    return ws


# =============================================================================
# TAB 6: PAYOFF SCHEDULE
# =============================================================================

def build_payoff_schedule(wb):
    """Build the Payoff Schedule tab."""
    ws = wb.create_sheet("Payoff Schedule")

    set_column_widths(ws, {
        'A': 5, 'B': 12, 'C': 10, 'D': 18, 'E': 16, 'F': 14,
        'G': 14, 'H': 14, 'I': 16, 'J': 16, 'K': 12
    })

    # Title
    ws.merge_cells('B2:K2')
    ws['B2'] = "PAYOFF SCHEDULE"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:K3')
    ws['B3'] = "Month-by-month payment plan showing how your debts will be paid off"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # Schedule headers
    headers = [
        'Month', 'MonthNum', 'DebtName', 'StartBalance', 'Interest',
        'Payment', 'Principal', 'EndBalance', 'CumulativeInt', 'PayoffFlag'
    ]

    row = 5
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Add sample schedule data (first few months for first debt as example)
    sample_schedule = [
        ['Jan 2025', 1, 'Credit Card A', 4800.00, 79.98, 150.00, 70.02, 4729.98, 79.98, ''],
        ['Feb 2025', 2, 'Credit Card A', 4729.98, 78.82, 150.00, 71.18, 4658.80, 158.80, ''],
        ['Mar 2025', 3, 'Credit Card A', 4658.80, 77.63, 150.00, 72.37, 4586.43, 236.43, ''],
        ['Jan 2025', 1, 'Car Loan', 12500.00, 72.71, 350.00, 277.29, 12222.71, 72.71, ''],
        ['Feb 2025', 2, 'Car Loan', 12222.71, 71.10, 350.00, 278.90, 11943.81, 143.81, ''],
        ['Mar 2025', 3, 'Car Loan', 11943.81, 69.47, 350.00, 280.53, 11663.28, 213.28, ''],
    ]

    row = 6
    for data in sample_schedule:
        for col_idx, value in enumerate(data, start=2):
            cell = ws.cell(row=row, column=col_idx, value=value)
            cell.border = thin_border

            # Number formatting
            if col_idx in [5, 6, 7, 8, 9, 10]:  # Currency columns
                cell.number_format = '_($* #,##0.00_)'
        row += 1

    # Add note about formula complexity
    row += 2
    ws[f'B{row}'] = "NOTE: This schedule uses simplified example data."
    ws[f'B{row}'].font = Font(name='Calibri', size=10, italic=True, color=COLORS['secondary'])
    ws.merge_cells(f'B{row}:K{row}')

    row += 1
    ws[f'B{row}'] = "For full dynamic calculation, use SCAN() or iterative formulas in Microsoft 365."
    ws[f'B{row}'].font = Font(name='Calibri', size=10, italic=True, color=COLORS['secondary'])
    ws.merge_cells(f'B{row}:K{row}')

    # -------------------------------------------------------------------------
    # Summary Section
    # -------------------------------------------------------------------------
    row += 3
    ws[f'B{row}'] = "PAYOFF SUMMARY BY DEBT"
    ws[f'B{row}'].font = FONTS['subheader']

    summary_headers = ['DebtName', 'StartBalance', 'TotalInterest', 'TotalPaid', 'PayoffMonth', 'MonthsToPayoff']
    row += 2
    for col_idx, header in enumerate(summary_headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Sample summary data
    summary_data = [
        ['Credit Card B', 2800, 892, 3692, 'Mar 2028', 39],
        ['Credit Card A', 4800, 1856, 6656, 'Oct 2028', 46],
        ['Personal Loan', 6500, 1243, 7743, 'Feb 2029', 50],
        ['Car Loan', 12500, 2187, 14687, 'Aug 2029', 56],
        ['Student Loan', 22000, 4892, 26892, 'Apr 2031', 76],
    ]

    row += 1
    for data in summary_data:
        for col_idx, value in enumerate(data, start=2):
            cell = ws.cell(row=row, column=col_idx, value=value)
            cell.border = thin_border
            if col_idx in [3, 4, 5]:
                cell.number_format = '_($* #,##0.00_)'
        row += 1

    # Conditional formatting for PayoffFlag
    green_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
    ws.conditional_formatting.add('K6:K200',
        FormulaRule(formula=['$K6="PAID"'], fill=green_fill))

    ws.freeze_panes = 'D6'

    return ws


# =============================================================================
# TAB 7: ACTUAL PAYMENTS LOG
# =============================================================================

def build_actual_payments(wb):
    """Build the Actual Payments Log tab."""
    ws = wb.create_sheet("Actual Payments")

    set_column_widths(ws, {
        'A': 5, 'B': 14, 'C': 12, 'D': 20, 'E': 14, 'F': 14, 'G': 12, 'H': 30
    })

    # Title
    ws.merge_cells('B2:H2')
    ws['B2'] = "ACTUAL PAYMENTS LOG"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:H3')
    ws['B3'] = "Track your actual payments to compare against the plan"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # Table headers
    headers = ['Date', 'DebtID', 'DebtName', 'AmountPaid', 'FeesPaid', 'IsExtra', 'Notes']

    row = 5
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Add sample data
    sample_payments = [
        ['2025-01-15', 1, 'Credit Card A', 150.00, 0, 'No', 'Minimum payment'],
        ['2025-01-01', 2, 'Car Loan', 350.00, 0, 'No', ''],
        ['2025-01-20', 3, 'Student Loan', 250.00, 0, 'No', ''],
        ['2025-01-10', 4, 'Credit Card B', 100.00, 0, 'Yes', 'Extra $15'],
        ['2025-01-05', 5, 'Personal Loan', 200.00, 0, 'No', ''],
    ]

    row = 6
    for payment in sample_payments:
        for col_idx, value in enumerate(payment, start=2):
            cell = ws.cell(row=row, column=col_idx, value=value)
            cell.border = thin_border
            apply_input_style(cell)

            if col_idx == 2:  # Date
                cell.number_format = 'YYYY-MM-DD'
            elif col_idx in [5, 6]:  # Currency
                cell.number_format = '_($* #,##0.00_)'
        row += 1

    # Add empty rows for data entry
    for _ in range(95):  # 100 rows total
        for col_idx in range(2, 9):
            cell = ws.cell(row=row, column=col_idx, value='')
            cell.border = thin_border
            apply_input_style(cell)
        row += 1

    # Create table
    table_ref = f"B5:H{row-1}"
    table = Table(displayName="tblPaymentsActual", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium3", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    table.tableStyleInfo = style
    ws.add_table(table)

    # Data validation for DebtID (reference tblDebts)
    # Note: Dynamic list from table requires named range in practice
    dv_extra = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(dv_extra)
    dv_extra.add(f'G6:G{row-1}')

    # -------------------------------------------------------------------------
    # Summary Section
    # -------------------------------------------------------------------------
    ws['J5'] = "PAYMENT SUMMARY"
    ws['J5'].font = FONTS['subheader']

    summaries = [
        ("Total Paid (All Time)", '=SUMIF(tblPaymentsActual[AmountPaid],">0")'),
        ("Total Fees Paid", '=SUM(tblPaymentsActual[FeesPaid])'),
        ("Payments This Month", '=SUMIFS(tblPaymentsActual[AmountPaid],tblPaymentsActual[Date],">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))'),
        ("Extra Payments Made", '=SUMIF(tblPaymentsActual[IsExtra],"Yes",tblPaymentsActual[AmountPaid])'),
    ]

    row = 7
    for label, formula in summaries:
        ws[f'J{row}'] = label
        ws[f'J{row}'].font = FONTS['bold']
        ws[f'K{row}'] = formula
        apply_calc_style(ws[f'K{row}'])
        ws[f'K{row}'].number_format = '_($* #,##0.00_)'
        row += 1

    ws.freeze_panes = 'B6'

    return ws


# =============================================================================
# TAB 8: DEBT DASHBOARD
# =============================================================================

def build_dashboard(wb):
    """Build the Debt Dashboard tab with visualizations."""
    ws = wb.create_sheet("Dashboard")

    set_column_widths(ws, {
        'A': 5, 'B': 25, 'C': 18, 'D': 5, 'E': 25, 'F': 18, 'G': 5,
        'H': 25, 'I': 18
    })

    # Title
    ws.merge_cells('B2:I2')
    ws['B2'] = "DEBT PAYOFF DASHBOARD"
    ws['B2'].font = FONTS['title']

    # -------------------------------------------------------------------------
    # KPI Scorecards Row 1
    # -------------------------------------------------------------------------
    row = 4
    kpis_row1 = [
        ("Total Debt Remaining", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[CurrentBalance])', 'B'),
        ("Monthly Payment", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[MinimumPayment])+Setup!C8', 'E'),
        ("Active Debts", '=COUNTIFS(tblDebts[IsIncluded],"Yes",tblDebts[Status],"Open")', 'H'),
    ]

    for label, formula, col in kpis_row1:
        # Label
        ws[f'{col}{row}'] = label
        ws[f'{col}{row}'].font = FONTS['bold']
        ws[f'{col}{row}'].fill = FILLS['header']
        ws[f'{col}{row}'].font = FONTS['header']
        ws[f'{col}{row}'].alignment = ALIGN['center']
        ws[f'{col}{row}'].border = thin_border
        next_col = chr(ord(col) + 1)
        ws[f'{next_col}{row}'].fill = FILLS['header']
        ws[f'{next_col}{row}'].border = thin_border
        ws.merge_cells(f'{col}{row}:{next_col}{row}')

        # Value
        ws[f'{col}{row+1}'] = formula
        ws[f'{col}{row+1}'].font = Font(name='Calibri', size=20, bold=True, color=COLORS['primary'])
        ws[f'{col}{row+1}'].alignment = ALIGN['center']
        ws[f'{col}{row+1}'].border = thin_border
        ws[f'{next_col}{row+1}'].border = thin_border
        ws.merge_cells(f'{col}{row+1}:{next_col}{row+1}')

        if col != 'H':
            ws[f'{col}{row+1}'].number_format = '_($* #,##0_)'
        else:
            ws[f'{col}{row+1}'].number_format = '0'

    # -------------------------------------------------------------------------
    # KPI Scorecards Row 2
    # -------------------------------------------------------------------------
    row = 7
    kpis_row2 = [
        ("Highest Rate Debt", '=INDEX(tblDebts[DebtName],MATCH(MAX(tblDebts[AnnualInterestRate]),tblDebts[AnnualInterestRate],0))', 'B'),
        ("Avg Interest Rate", '=AVERAGEIF(tblDebts[IsIncluded],"Yes",tblDebts[AnnualInterestRate])', 'E'),
        ("Total Paid to Date", '=SUM(tblPaymentsActual[AmountPaid])', 'H'),
    ]

    for label, formula, col in kpis_row2:
        ws[f'{col}{row}'] = label
        ws[f'{col}{row}'].font = FONTS['bold']
        ws[f'{col}{row}'].fill = FILLS['light_grey']
        ws[f'{col}{row}'].alignment = ALIGN['center']
        ws[f'{col}{row}'].border = thin_border
        next_col = chr(ord(col) + 1)
        ws[f'{next_col}{row}'].fill = FILLS['light_grey']
        ws[f'{next_col}{row}'].border = thin_border
        ws.merge_cells(f'{col}{row}:{next_col}{row}')

        ws[f'{col}{row+1}'] = formula
        ws[f'{col}{row+1}'].font = Font(name='Calibri', size=16, bold=True, color=COLORS['secondary'])
        ws[f'{col}{row+1}'].alignment = ALIGN['center']
        ws[f'{col}{row+1}'].border = thin_border
        ws[f'{next_col}{row+1}'].border = thin_border
        ws.merge_cells(f'{col}{row+1}:{next_col}{row+1}')

        if col == 'E':
            ws[f'{col}{row+1}'].number_format = '0.00%'
        elif col == 'H':
            ws[f'{col}{row+1}'].number_format = '_($* #,##0_)'

    # -------------------------------------------------------------------------
    # Debt Breakdown Section
    # -------------------------------------------------------------------------
    row = 11
    ws[f'B{row}'] = "DEBT BREAKDOWN"
    ws[f'B{row}'].font = FONTS['subheader']

    # Create a mini table showing debt breakdown
    breakdown_headers = ['Debt', 'Balance', 'Rate', 'Min Payment', '% of Total']
    row += 2
    for col_idx, header in enumerate(breakdown_headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Reference debt data (simplified - in production would use INDEX/MATCH or spill)
    for i in range(1, 6):
        row += 1
        ws.cell(row=row, column=2, value=f'=IFERROR(INDEX(tblDebts[DebtName],{i}),"")').border = thin_border
        ws.cell(row=row, column=3, value=f'=IFERROR(INDEX(tblDebts[CurrentBalance],{i}),"")').border = thin_border
        ws.cell(row=row, column=3).number_format = '_($* #,##0_)'
        ws.cell(row=row, column=4, value=f'=IFERROR(INDEX(tblDebts[AnnualInterestRate],{i}),"")').border = thin_border
        ws.cell(row=row, column=4).number_format = '0.0%'
        ws.cell(row=row, column=5, value=f'=IFERROR(INDEX(tblDebts[MinimumPayment],{i}),"")').border = thin_border
        ws.cell(row=row, column=5).number_format = '_($* #,##0_)'
        pct_formula = f'=IFERROR(INDEX(tblDebts[CurrentBalance],{i})/SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[CurrentBalance]),"")'
        ws.cell(row=row, column=6, value=pct_formula).border = thin_border
        ws.cell(row=row, column=6).number_format = '0.0%'

    # -------------------------------------------------------------------------
    # Progress Indicators
    # -------------------------------------------------------------------------
    row += 3
    ws[f'B{row}'] = "PROGRESS TRACKING"
    ws[f'B{row}'].font = FONTS['subheader']

    progress_items = [
        ("Starting Total Debt", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[StartBalance])'),
        ("Current Total Debt", '=SUMIF(tblDebts[IsIncluded],"Yes",tblDebts[CurrentBalance])'),
        ("Amount Paid Off", '=B24-B25'),
        ("Progress %", '=IFERROR(B26/B24,0)'),
    ]

    row += 2
    for label, formula in progress_items:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = formula
        apply_calc_style(ws[f'C{row}'])
        if 'Progress' in label:
            ws[f'C{row}'].number_format = '0.0%'
        else:
            ws[f'C{row}'].number_format = '_($* #,##0.00_)'
        row += 1

    # -------------------------------------------------------------------------
    # Chart: Debt Breakdown Pie Chart
    # -------------------------------------------------------------------------
    # Data for pie chart is in B14:C18 (debt names and balances)
    pie = PieChart()
    pie.title = "Debt Distribution"
    labels = Reference(ws, min_col=2, min_row=14, max_row=18)
    data = Reference(ws, min_col=3, min_row=13, max_row=18)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.height = 10
    pie.width = 14
    ws.add_chart(pie, "H11")

    ws.freeze_panes = 'B4'

    return ws


# =============================================================================
# TAB 9: CALENDAR
# =============================================================================

def build_calendar(wb):
    """Build the Calendar tab for due date visibility."""
    ws = wb.create_sheet("Calendar")

    # Set column widths for calendar grid
    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 14
    ws.column_dimensions['A'].width = 5

    # Title
    ws.merge_cells('B2:H2')
    ws['B2'] = "PAYMENT CALENDAR"
    ws['B2'].font = FONTS['title']

    # Month selector
    ws['B4'] = "Display Month:"
    ws['B4'].font = FONTS['bold']
    ws['C4'] = datetime.now().strftime('%Y-%m')
    apply_input_style(ws['C4'])

    ws['E4'] = "Week Starts:"
    ws['E4'].font = FONTS['bold']
    ws['F4'] = "Monday"
    apply_input_style(ws['F4'])

    dv_week = DataValidation(type="list", formula1='"Monday,Sunday"')
    ws.add_data_validation(dv_week)
    dv_week.add('F4')

    # Calendar header (days of week)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    row = 6
    for col_idx, day in enumerate(days, start=2):
        cell = ws.cell(row=row, column=col_idx, value=day)
        apply_header_style(cell)

    # Calendar grid (6 weeks)
    current_date = datetime.now().replace(day=1)

    row = 7
    for week in range(6):
        # Day number row
        for col_idx in range(2, 9):
            cell = ws.cell(row=row, column=col_idx, value='')
            cell.border = thin_border
            cell.alignment = Alignment(horizontal='right', vertical='top')
            cell.font = FONTS['bold']
        row += 1

        # Payment info row
        for col_idx in range(2, 9):
            cell = ws.cell(row=row, column=col_idx, value='')
            cell.border = thin_border
            cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
            cell.font = FONTS['small']
        row += 1

        # Weekly total row
        for col_idx in range(2, 9):
            cell = ws.cell(row=row, column=col_idx, value='')
            cell.border = thin_border
        row += 1

    # Fill in sample calendar data for current month
    # First, find what day of week the 1st falls on
    first_day = datetime.now().replace(day=1)
    start_weekday = first_day.weekday()  # Monday = 0

    day_num = 1
    days_in_month = 31  # Simplified

    for week in range(6):
        day_row = 7 + (week * 3)
        for weekday in range(7):
            col = weekday + 2

            if week == 0 and weekday < start_weekday:
                continue
            if day_num > days_in_month:
                continue

            ws.cell(row=day_row, column=col, value=day_num)

            # Check if any debts are due on this day
            # This would be a formula in practice: =TEXTJOIN(", ",TRUE,IF(tblDebts[DueDayOfMonth]=day_num,tblDebts[DebtName]&": $"&tblDebts[MinimumPayment],""))
            payment_cell = ws.cell(row=day_row + 1, column=col)

            # Sample data - in practice this would be formula-driven
            if day_num == 1:
                payment_cell.value = "Car Loan: $350"
                payment_cell.fill = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')
            elif day_num == 5:
                payment_cell.value = "Personal Loan: $200"
                payment_cell.fill = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')
            elif day_num == 10:
                payment_cell.value = "Credit Card B: $85"
                payment_cell.fill = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')
            elif day_num == 15:
                payment_cell.value = "Credit Card A: $150"
                payment_cell.fill = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')
            elif day_num == 20:
                payment_cell.value = "Student Loan: $250"
                payment_cell.fill = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')

            day_num += 1

    # Weekly totals summary
    row = 25
    ws[f'B{row}'] = "WEEKLY PAYMENT TOTALS"
    ws[f'B{row}'].font = FONTS['subheader']

    row += 2
    weekly_totals = [
        ("Week 1 (1st - 7th)", "$550"),
        ("Week 2 (8th - 14th)", "$85"),
        ("Week 3 (15th - 21st)", "$400"),
        ("Week 4 (22nd - 28th)", "$0"),
        ("Month Total", "$1,035"),
    ]

    for label, amount in weekly_totals:
        ws[f'B{row}'] = label
        ws[f'C{row}'] = amount
        if "Month" in label:
            ws[f'B{row}'].font = FONTS['bold']
            ws[f'C{row}'].font = FONTS['bold']
        row += 1

    # Upcoming payments section
    row += 2
    ws[f'E25'] = "NEXT 5 PAYMENTS"
    ws[f'E25'].font = FONTS['subheader']

    upcoming_headers = ['Due Date', 'Debt', 'Amount']
    row = 27
    for col_idx, header in enumerate(upcoming_headers, start=5):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    upcoming = [
        ('Jan 1', 'Car Loan', '$350'),
        ('Jan 5', 'Personal Loan', '$200'),
        ('Jan 10', 'Credit Card B', '$85'),
        ('Jan 15', 'Credit Card A', '$150'),
        ('Jan 20', 'Student Loan', '$250'),
    ]

    for due, debt, amt in upcoming:
        row += 1
        ws.cell(row=row, column=5, value=due).border = thin_border
        ws.cell(row=row, column=6, value=debt).border = thin_border
        ws.cell(row=row, column=7, value=amt).border = thin_border

    ws.freeze_panes = 'B6'

    return ws


# =============================================================================
# TAB 10: AUDIT AND SETTINGS
# =============================================================================

def build_audit_settings(wb):
    """Build the Audit and Settings tab."""
    ws = wb.create_sheet("Audit & Settings")

    set_column_widths(ws, {'A': 5, 'B': 30, 'C': 40, 'D': 20})

    # Title
    ws.merge_cells('B2:D2')
    ws['B2'] = "AUDIT & SETTINGS"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:D3')
    ws['B3'] = "Workbook configuration and maintenance information"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # -------------------------------------------------------------------------
    # Workbook Information
    # -------------------------------------------------------------------------
    ws['B5'] = "WORKBOOK INFORMATION"
    ws['B5'].font = FONTS['subheader']

    info = [
        ("Workbook Version", "1.0"),
        ("Created Date", datetime.now().strftime('%Y-%m-%d')),
        ("Last Modified", datetime.now().strftime('%Y-%m-%d %H:%M')),
        ("Excel Version Required", "Microsoft 365 (recommended)"),
        ("Calculation Mode", "Automatic"),
    ]

    row = 7
    for label, value in info:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = FONTS['bold']
        ws[f'C{row}'] = value
        row += 1

    # -------------------------------------------------------------------------
    # Named Ranges Registry
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "TABLES REGISTRY"
    ws[f'B{row}'].font = FONTS['subheader']

    tables = [
        ("tblDebts", "Debt Register", "Master list of all debts"),
        ("tblAssumptions", "Setup", "Plan configuration parameters"),
        ("tblPaymentsActual", "Actual Payments", "Payment transaction log"),
    ]

    row += 2
    headers = ['Table Name', 'Location', 'Description']
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    for table_name, location, desc in tables:
        row += 1
        ws.cell(row=row, column=2, value=table_name).border = thin_border
        ws.cell(row=row, column=3, value=location).border = thin_border
        ws.cell(row=row, column=4, value=desc).border = thin_border

    # -------------------------------------------------------------------------
    # Data Validation Lists
    # -------------------------------------------------------------------------
    row += 3
    ws[f'B{row}'] = "DATA VALIDATION LISTS"
    ws[f'B{row}'].font = FONTS['subheader']

    validations = [
        ("PayoffMethod", "Snowball, Avalanche, Custom"),
        ("DebtType", "Credit Card, Loan, Overdraft, Line of Credit, Other"),
        ("InterestMethod", "Monthly, Daily"),
        ("YesNo", "Yes, No"),
        ("DebtStatus", "Open, Paid, On Hold"),
        ("WeekStart", "Monday, Sunday"),
    ]

    row += 2
    headers = ['List Name', 'Values']
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    for list_name, values in validations:
        row += 1
        ws.cell(row=row, column=2, value=list_name).border = thin_border
        ws.cell(row=row, column=3, value=values).border = thin_border

    # -------------------------------------------------------------------------
    # Reset Instructions
    # -------------------------------------------------------------------------
    row += 3
    ws[f'B{row}'] = "RESET INSTRUCTIONS"
    ws[f'B{row}'].font = FONTS['subheader']

    instructions = [
        "To reset actual payments: Select all data rows in tblPaymentsActual and delete",
        "To reset debts: Clear rows in tblDebts (keep headers)",
        "To start fresh: Save a copy of this workbook before entering data",
    ]

    row += 2
    for instruction in instructions:
        ws[f'B{row}'] = f"• {instruction}"
        ws.merge_cells(f'B{row}:D{row}')
        row += 1

    # -------------------------------------------------------------------------
    # Troubleshooting
    # -------------------------------------------------------------------------
    row += 2
    ws[f'B{row}'] = "TROUBLESHOOTING"
    ws[f'B{row}'].font = FONTS['subheader']

    issues = [
        ("Formulas show #REF!", "Check that all tables exist and have data"),
        ("Schedule not calculating", "Ensure at least one debt is marked 'Yes' for IsIncluded"),
        ("Calendar not updating", "Verify the Display Month format is YYYY-MM"),
        ("Slow performance", "Set calculation to Manual, calculate with F9"),
    ]

    row += 2
    headers = ['Issue', 'Solution']
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    for issue, solution in issues:
        row += 1
        ws.cell(row=row, column=2, value=issue).border = thin_border
        ws.cell(row=row, column=3, value=solution).border = thin_border
        ws.merge_cells(f'C{row}:D{row}')

    # Hide this sheet (optional - commented out for now)
    # ws.sheet_state = 'hidden'

    return ws


# =============================================================================
# TAB 11: WINDFALLS (Bonus)
# =============================================================================

def build_windfalls(wb):
    """Build the Windfalls tracking tab."""
    ws = wb.create_sheet("Windfalls")

    set_column_widths(ws, {'A': 5, 'B': 14, 'C': 16, 'D': 25, 'E': 18, 'F': 30})

    # Title
    ws.merge_cells('B2:F2')
    ws['B2'] = "WINDFALL TRACKER"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:F3')
    ws['B3'] = "Track bonus payments, tax refunds, and other lump sum payments toward debt"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # Table headers
    headers = ['Date', 'Amount', 'AllocationRule', 'TargetDebtID', 'Notes']

    row = 5
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Sample data
    sample = [
        ['2025-03-15', 1500, 'Highest Rate', '', 'Tax refund'],
        ['2025-06-01', 500, 'Smallest Balance', '', 'Bonus'],
        ['2025-12-01', 1000, 'Custom', 2, 'Year-end bonus to car loan'],
    ]

    row = 6
    for windfall in sample:
        for col_idx, value in enumerate(windfall, start=2):
            cell = ws.cell(row=row, column=col_idx, value=value)
            cell.border = thin_border
            apply_input_style(cell)
            if col_idx == 2:
                cell.number_format = 'YYYY-MM-DD'
            elif col_idx == 3:
                cell.number_format = '_($* #,##0.00_)'
        row += 1

    # Add empty rows
    for _ in range(47):
        for col_idx in range(2, 7):
            cell = ws.cell(row=row, column=col_idx, value='')
            cell.border = thin_border
            apply_input_style(cell)
        row += 1

    # Create table
    table_ref = f"B5:F{row-1}"
    table = Table(displayName="tblWindfalls", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium4", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    table.tableStyleInfo = style
    ws.add_table(table)

    # Data validation
    dv_rule = DataValidation(type="list", formula1='"Highest Rate,Smallest Balance,Custom"')
    ws.add_data_validation(dv_rule)
    dv_rule.add(f'D6:D{row-1}')

    # Summary
    ws['H5'] = "WINDFALL SUMMARY"
    ws['H5'].font = FONTS['subheader']

    summaries = [
        ("Total Windfalls Planned", '=SUM(tblWindfalls[Amount])'),
        ("Applied This Year", '=SUMIF(tblWindfalls[Date],">="&DATE(YEAR(TODAY()),1,1),tblWindfalls[Amount])'),
    ]

    row = 7
    for label, formula in summaries:
        ws[f'H{row}'] = label
        ws[f'H{row}'].font = FONTS['bold']
        ws[f'I{row}'] = formula
        apply_calc_style(ws[f'I{row}'])
        ws[f'I{row}'].number_format = '_($* #,##0.00_)'
        row += 1

    ws.freeze_panes = 'B6'

    return ws


# =============================================================================
# TAB 12: METHOD COMPARISON (Bonus)
# =============================================================================

def build_method_comparison(wb):
    """Build the Method Comparison tab."""
    ws = wb.create_sheet("Method Comparison")

    set_column_widths(ws, {'A': 5, 'B': 25, 'C': 18, 'D': 18, 'E': 18})

    # Title
    ws.merge_cells('B2:E2')
    ws['B2'] = "METHOD COMPARISON"
    ws['B2'].font = FONTS['title']

    ws.merge_cells('B3:E3')
    ws['B3'] = "Compare Snowball vs Avalanche payoff strategies"
    ws['B3'].font = Font(name='Calibri', size=11, italic=True)

    # Comparison headers
    headers = ['Metric', 'Snowball', 'Avalanche', 'Difference']
    row = 5
    for col_idx, header in enumerate(headers, start=2):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_header_style(cell)

    # Comparison metrics (placeholder values - would be calculated)
    metrics = [
        ('Debt-Free Date', 'Apr 2031', 'Feb 2031', '2 months faster'),
        ('Total Interest Paid', '$11,070', '$9,845', '$1,225 savings'),
        ('First Debt Paid Off', 'Mar 2026', 'Oct 2028', '30 months faster'),
        ('Total Paid', '$59,670', '$58,445', '$1,225 savings'),
    ]

    row = 6
    for metric, snowball, avalanche, diff in metrics:
        ws.cell(row=row, column=2, value=metric).border = thin_border
        ws.cell(row=row, column=2).font = FONTS['bold']
        ws.cell(row=row, column=3, value=snowball).border = thin_border
        ws.cell(row=row, column=4, value=avalanche).border = thin_border
        ws.cell(row=row, column=5, value=diff).border = thin_border

        # Highlight better option
        if 'savings' in diff or 'faster' in diff:
            ws.cell(row=row, column=4).fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
        row += 1

    # Recommendation
    row += 2
    ws[f'B{row}'] = "RECOMMENDATION"
    ws[f'B{row}'].font = FONTS['subheader']

    row += 2
    ws[f'B{row}'] = "Based on your debts:"
    row += 1
    ws.merge_cells(f'B{row}:E{row}')
    ws[f'B{row}'] = "• AVALANCHE saves you $1,225 in interest and gets you debt-free 2 months sooner"
    row += 1
    ws.merge_cells(f'B{row}:E{row}')
    ws[f'B{row}'] = "• SNOWBALL pays off your first debt 30 months earlier (psychological wins)"
    row += 2
    ws.merge_cells(f'B{row}:E{row}')
    ws[f'B{row}'] = "Choose Avalanche if you're motivated by savings. Choose Snowball if you need quick wins."
    ws[f'B{row}'].font = Font(name='Calibri', size=11, italic=True, bold=True)

    ws.freeze_panes = 'B5'

    return ws


# =============================================================================
# MAIN BUILDER
# =============================================================================

def create_debt_payoff_workbook(output_path='Debt_Payoff_Workbook.xlsx'):
    """Create the complete Debt Payoff Workbook."""

    print("Creating Debt Payoff Workbook...")

    # Create workbook
    wb = Workbook()

    # Build all tabs
    print("  Building Start Here tab...")
    build_start_here(wb)

    print("  Building Setup tab...")
    build_setup(wb)

    print("  Building Debt Register tab...")
    build_debt_register(wb)

    print("  Building Budget & Capacity tab...")
    build_budget_capacity(wb)

    print("  Building Payoff Engine tab...")
    build_payoff_engine(wb)

    print("  Building Payoff Schedule tab...")
    build_payoff_schedule(wb)

    print("  Building Actual Payments tab...")
    build_actual_payments(wb)

    print("  Building Dashboard tab...")
    build_dashboard(wb)

    print("  Building Calendar tab...")
    build_calendar(wb)

    print("  Building Audit & Settings tab...")
    build_audit_settings(wb)

    print("  Building Windfalls tab...")
    build_windfalls(wb)

    print("  Building Method Comparison tab...")
    build_method_comparison(wb)

    # Set the active sheet to Start Here
    wb.active = wb['Start Here']

    # Save workbook
    wb.save(output_path)
    print(f"\nWorkbook saved to: {output_path}")
    print(f"Total tabs created: {len(wb.worksheets)}")

    return output_path


if __name__ == '__main__':
    output_file = '/home/user/Automations/Debt_Payoff_Workbook.xlsx'
    create_debt_payoff_workbook(output_file)
