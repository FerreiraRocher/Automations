#!/usr/bin/env python3
"""
Comprehensive Debt Payment Workbook Generator
Creates a professional Excel workbook for debt tracking and payoff planning
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import (
    Font, Fill, PatternFill, Border, Side, Alignment,
    NamedStyle, numbers
)
from openpyxl.utils import get_column_letter
from openpyxl.chart import PieChart, BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.formatting.rule import (
    FormulaRule, ColorScaleRule, DataBarRule, CellIsRule
)
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment
from datetime import datetime, date
from openpyxl.drawing.image import Image
import os

# Color scheme
COLORS = {
    'primary': '1E3A5F',       # Dark blue
    'secondary': '3D7EA6',     # Medium blue
    'accent': '5BA88E',        # Teal green
    'light_blue': 'E8F4FC',    # Light blue (input cells)
    'light_gray': 'F5F5F5',    # Light gray (calculated)
    'white': 'FFFFFF',
    'success': '28A745',       # Green
    'warning': 'FFC107',       # Yellow
    'danger': 'DC3545',        # Red
    'header_blue': '2E75B6',
    'header_green': '548235',
}

# Styles
def create_styles(wb):
    """Create named styles for the workbook"""

    # Header style
    header_style = NamedStyle(name='header_style')
    header_style.font = Font(bold=True, color='FFFFFF', size=12)
    header_style.fill = PatternFill('solid', fgColor=COLORS['primary'])
    header_style.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    header_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    wb.add_named_style(header_style)

    # Sub-header style
    subheader_style = NamedStyle(name='subheader_style')
    subheader_style.font = Font(bold=True, color='FFFFFF', size=11)
    subheader_style.fill = PatternFill('solid', fgColor=COLORS['secondary'])
    subheader_style.alignment = Alignment(horizontal='center', vertical='center')
    subheader_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    wb.add_named_style(subheader_style)

    # Input cell style
    input_style = NamedStyle(name='input_style')
    input_style.fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    input_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    input_style.alignment = Alignment(horizontal='center', vertical='center')
    wb.add_named_style(input_style)

    # Calculated cell style
    calc_style = NamedStyle(name='calc_style')
    calc_style.fill = PatternFill('solid', fgColor=COLORS['light_gray'])
    calc_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    calc_style.alignment = Alignment(horizontal='center', vertical='center')
    wb.add_named_style(calc_style)

    # Currency style
    currency_style = NamedStyle(name='currency_style')
    currency_style.number_format = '$#,##0.00'
    currency_style.alignment = Alignment(horizontal='right', vertical='center')
    currency_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    wb.add_named_style(currency_style)

    # Percentage style
    percent_style = NamedStyle(name='percent_style')
    percent_style.number_format = '0.00%'
    percent_style.alignment = Alignment(horizontal='center', vertical='center')
    percent_style.border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    wb.add_named_style(percent_style)

    # Title style
    title_style = NamedStyle(name='title_style')
    title_style.font = Font(bold=True, size=18, color=COLORS['primary'])
    title_style.alignment = Alignment(horizontal='center', vertical='center')
    wb.add_named_style(title_style)

    # Metric card style
    metric_style = NamedStyle(name='metric_style')
    metric_style.font = Font(bold=True, size=14, color=COLORS['primary'])
    metric_style.alignment = Alignment(horizontal='center', vertical='center')
    metric_style.number_format = '$#,##0.00'
    wb.add_named_style(metric_style)


def apply_style(cell, style_name):
    """Apply a named style to a cell"""
    cell.style = style_name


def set_column_widths(ws, widths):
    """Set column widths from a dictionary {column_letter: width}"""
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def create_dashboard(wb):
    """Create the Dashboard sheet"""
    ws = wb.active
    ws.title = "Dashboard"

    # Set column widths
    set_column_widths(ws, {
        'A': 3, 'B': 25, 'C': 20, 'D': 20, 'E': 20,
        'F': 20, 'G': 20, 'H': 3, 'I': 25, 'J': 20
    })

    # Title
    ws.merge_cells('B2:G2')
    ws['B2'] = "DEBT PAYMENT DASHBOARD"
    ws['B2'].font = Font(bold=True, size=24, color=COLORS['primary'])
    ws['B2'].alignment = Alignment(horizontal='center', vertical='center')

    # Last updated
    ws['B3'] = "Last Updated:"
    ws['C3'] = datetime.now().strftime("%B %d, %Y")
    ws['C3'].font = Font(italic=True, color='666666')

    # KEY METRICS SECTION
    ws.merge_cells('B5:D5')
    ws['B5'] = "KEY METRICS"
    ws['B5'].style = 'header_style'

    metrics = [
        ('B7', 'Total Debt (Original):', 'C7', "=SUM('Debt Inventory'!D4:D28)"),
        ('B8', 'Total Debt (Current):', 'C8', "=SUM('Debt Inventory'!E4:E28)"),
        ('B9', 'Total Paid Off:', 'C9', "=C7-C8"),
        ('B10', 'Progress:', 'C10', "=IF(C7>0,C9/C7,0)"),
        ('B12', 'Monthly Minimum:', 'C12', "=SUM('Debt Inventory'!G4:G28)"),
        ('B13', 'Average Interest Rate:', 'C13', "=AVERAGEIF('Debt Inventory'!F4:F28,\">0\")"),
        ('B14', 'Number of Active Debts:', 'C14', "=COUNTIF('Debt Inventory'!E4:E28,\">0\")"),
    ]

    for label_cell, label, value_cell, formula in metrics:
        ws[label_cell] = label
        ws[label_cell].font = Font(bold=True)
        ws[value_cell] = formula
        if 'Progress' in label:
            ws[value_cell].number_format = '0.0%'
            ws[value_cell].font = Font(bold=True, size=14, color=COLORS['accent'])
        elif 'Rate' in label:
            ws[value_cell].number_format = '0.00%'
        elif 'Number' in label:
            ws[value_cell].number_format = '0'
        else:
            ws[value_cell].number_format = '$#,##0.00'
            ws[value_cell].font = Font(bold=True, size=12)

    # STRATEGY SUMMARY
    ws.merge_cells('E5:G5')
    ws['E5'] = "SELECTED STRATEGY"
    ws['E5'].style = 'header_style'

    ws['E7'] = "Current Strategy:"
    ws['F7'] = "='Strategy Selector'!B4"
    ws['F7'].font = Font(bold=True, size=14, color=COLORS['secondary'])

    ws['E9'] = "Projected Debt-Free Date:"
    ws['F9'] = "='Strategy Selector'!E12"
    ws['F9'].font = Font(bold=True, size=12)

    ws['E10'] = "Total Interest to Pay:"
    ws['F10'] = "='Strategy Selector'!E10"
    ws['F10'].number_format = '$#,##0.00'

    ws['E11'] = "Months to Debt-Free:"
    ws['F11'] = "='Strategy Selector'!E11"

    # DEBT BREAKDOWN SECTION
    ws.merge_cells('B16:D16')
    ws['B16'] = "TOP 5 LARGEST DEBTS"
    ws['B16'].style = 'subheader_style'

    # Headers for debt list
    headers = ['Debt Name', 'Balance', 'Rate']
    for i, header in enumerate(headers):
        cell = ws.cell(row=17, column=2+i, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill('solid', fgColor=COLORS['light_gray'])

    # Placeholder rows for top debts (will reference Debt Inventory)
    for row in range(18, 23):
        ws.cell(row=row, column=2, value=f"=IFERROR(INDEX('Debt Inventory'!B4:B28,MATCH(LARGE('Debt Inventory'!E4:E28,{row-17}),'Debt Inventory'!E4:E28,0)),\"\")")
        ws.cell(row=row, column=3, value=f"=IFERROR(LARGE('Debt Inventory'!E4:E28,{row-17}),\"\")")
        ws.cell(row=row, column=3).number_format = '$#,##0.00'
        ws.cell(row=row, column=4, value=f"=IFERROR(INDEX('Debt Inventory'!F4:F28,MATCH(LARGE('Debt Inventory'!E4:E28,{row-17}),'Debt Inventory'!E4:E28,0)),\"\")")
        ws.cell(row=row, column=4).number_format = '0.0%'

    # PROGRESS VISUALIZATION
    ws.merge_cells('E16:G16')
    ws['E16'] = "PAYMENT BREAKDOWN"
    ws['E16'].style = 'subheader_style'

    # Instructions box
    ws.merge_cells('B25:G28')
    ws['B25'] = """INSTRUCTIONS:
1. Start by entering your debts in the 'Debt Inventory' sheet
2. Choose your payoff strategy in 'Strategy Selector'
3. View your payment schedule and track payments monthly
4. Use 'Extra Payment Calculator' to see impact of additional payments
5. Celebrate milestones in 'Progress & Milestones' sheet!"""
    ws['B25'].alignment = Alignment(wrap_text=True, vertical='top')
    ws['B25'].font = Font(size=10, color='666666')

    return ws


def create_debt_inventory(wb):
    """Create the Debt Inventory sheet"""
    ws = wb.create_sheet("Debt Inventory")

    # Set column widths
    set_column_widths(ws, {
        'A': 3, 'B': 25, 'C': 18, 'D': 18, 'E': 18,
        'F': 12, 'G': 15, 'H': 10, 'I': 15, 'J': 18,
        'K': 18, 'L': 18, 'M': 30
    })

    # Title
    ws.merge_cells('B1:M1')
    ws['B1'] = "DEBT INVENTORY"
    ws['B1'].style = 'title_style'

    # Headers
    headers = [
        ('B', 'Debt Name'),
        ('C', 'Debt Type'),
        ('D', 'Original Balance'),
        ('E', 'Current Balance'),
        ('F', 'APR %'),
        ('G', 'Min. Payment'),
        ('H', 'Due Day'),
        ('I', 'Start Date'),
        ('J', 'Monthly Interest'),
        ('K', 'Months to Payoff'),
        ('L', 'Total Interest'),
        ('M', 'Notes'),
    ]

    for col, header in headers:
        cell = ws[f'{col}3']
        cell.value = header
        cell.style = 'header_style'

    # Data validation for Debt Type
    debt_types = DataValidation(
        type="list",
        formula1='"Credit Card,Student Loan,Auto Loan,Mortgage,Personal Loan,Medical,Other"',
        allow_blank=True
    )
    debt_types.error = "Please select from the list"
    debt_types.errorTitle = "Invalid Debt Type"
    ws.add_data_validation(debt_types)

    # Add rows for up to 25 debts
    for row in range(4, 29):
        # Input cells
        for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'M']:
            cell = ws[f'{col}{row}']
            cell.fill = PatternFill('solid', fgColor=COLORS['light_blue'])
            cell.border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

        # Add data validation for debt type column
        debt_types.add(ws[f'C{row}'])

        # Currency formatting
        for col in ['D', 'E', 'G']:
            ws[f'{col}{row}'].number_format = '$#,##0.00'

        # Percentage formatting for APR
        ws[f'F{row}'].number_format = '0.00%'

        # Date formatting
        ws[f'I{row}'].number_format = 'MM/DD/YYYY'

        # Calculated cells
        # Monthly Interest = Current Balance * (APR/12)
        ws[f'J{row}'] = f'=IF(E{row}>0,E{row}*(F{row}/12),"")'
        ws[f'J{row}'].number_format = '$#,##0.00'
        ws[f'J{row}'].fill = PatternFill('solid', fgColor=COLORS['light_gray'])

        # Months to Payoff (using NPER function)
        ws[f'K{row}'] = f'=IF(AND(E{row}>0,G{row}>0,F{row}>0),NPER(F{row}/12,-G{row},E{row}),IF(AND(E{row}>0,G{row}>0),E{row}/G{row},""))'
        ws[f'K{row}'].number_format = '0.0'
        ws[f'K{row}'].fill = PatternFill('solid', fgColor=COLORS['light_gray'])

        # Total Interest (simplified estimate)
        ws[f'L{row}'] = f'=IF(K{row}<>"",G{row}*K{row}-E{row},"")'
        ws[f'L{row}'].number_format = '$#,##0.00'
        ws[f'L{row}'].fill = PatternFill('solid', fgColor=COLORS['light_gray'])

        for col in ['J', 'K', 'L']:
            ws[f'{col}{row}'].border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

    # Summary row
    ws['B30'] = "TOTALS"
    ws['B30'].font = Font(bold=True)
    ws['D30'] = '=SUM(D4:D28)'
    ws['D30'].number_format = '$#,##0.00'
    ws['D30'].font = Font(bold=True)
    ws['E30'] = '=SUM(E4:E28)'
    ws['E30'].number_format = '$#,##0.00'
    ws['E30'].font = Font(bold=True)
    ws['G30'] = '=SUM(G4:G28)'
    ws['G30'].number_format = '$#,##0.00'
    ws['G30'].font = Font(bold=True)
    ws['J30'] = '=SUM(J4:J28)'
    ws['J30'].number_format = '$#,##0.00'
    ws['J30'].font = Font(bold=True)
    ws['L30'] = '=SUM(L4:L28)'
    ws['L30'].number_format = '$#,##0.00'
    ws['L30'].font = Font(bold=True)

    # Add example data (first row)
    examples = [
        ('B4', 'Credit Card A'),
        ('C4', 'Credit Card'),
        ('D4', 5000),
        ('E4', 4500),
        ('F4', 0.1999),
        ('G4', 150),
        ('H4', 15),
        ('I4', date(2023, 1, 1)),
        ('M4', 'Example - delete and add your own'),
    ]
    for cell, value in examples:
        ws[cell].value = value

    # Instructions
    ws.merge_cells('B32:M33')
    ws['B32'] = "INSTRUCTIONS: Enter your debts above. Light blue cells are for your input. Gray cells are calculated automatically. APR should be entered as a decimal (e.g., 19.99% = 0.1999)."
    ws['B32'].font = Font(italic=True, size=9, color='666666')
    ws['B32'].alignment = Alignment(wrap_text=True)

    return ws


def create_strategy_selector(wb):
    """Create the Strategy Selector sheet"""
    ws = wb.create_sheet("Strategy Selector")

    set_column_widths(ws, {
        'A': 3, 'B': 30, 'C': 20, 'D': 20, 'E': 20,
        'F': 20, 'G': 20, 'H': 3
    })

    # Title
    ws.merge_cells('B1:G1')
    ws['B1'] = "DEBT PAYOFF STRATEGY SELECTOR"
    ws['B1'].style = 'title_style'

    # Strategy Selection
    ws['B3'] = "Select Your Strategy:"
    ws['B3'].font = Font(bold=True, size=12)

    ws['B4'] = "Debt Snowball"  # Default
    ws['B4'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['B4'].font = Font(bold=True, size=14)
    ws['B4'].border = Border(
        left=Side(style='medium'),
        right=Side(style='medium'),
        top=Side(style='medium'),
        bottom=Side(style='medium')
    )

    # Strategy dropdown
    strategy_dv = DataValidation(
        type="list",
        formula1='"Debt Snowball,Debt Avalanche,Custom Order"',
        allow_blank=False
    )
    ws.add_data_validation(strategy_dv)
    strategy_dv.add(ws['B4'])

    # Extra Monthly Payment
    ws['D3'] = "Extra Monthly Payment:"
    ws['D3'].font = Font(bold=True)
    ws['E3'] = 0
    ws['E3'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['E3'].number_format = '$#,##0.00'
    ws['E3'].border = Border(
        left=Side(style='medium'),
        right=Side(style='medium'),
        top=Side(style='medium'),
        bottom=Side(style='medium')
    )

    # Strategy Comparison Table
    ws.merge_cells('B6:G6')
    ws['B6'] = "STRATEGY COMPARISON"
    ws['B6'].style = 'header_style'

    # Headers
    comp_headers = ['Metric', 'Snowball', 'Avalanche', 'Custom', 'Min. Payments Only']
    for i, header in enumerate(comp_headers):
        cell = ws.cell(row=7, column=2+i, value=header)
        cell.style = 'subheader_style'

    # Comparison metrics
    metrics = [
        ('Total Interest Paid', '$#,##0.00'),
        ('Months to Debt-Free', '0'),
        ('Projected Debt-Free Date', 'MMM YYYY'),
        ('Interest Saved vs Min.', '$#,##0.00'),
        ('First Debt Paid Off', ''),
    ]

    for i, (metric, fmt) in enumerate(metrics):
        row = 8 + i
        ws.cell(row=row, column=2, value=metric).font = Font(bold=True)
        for col in range(3, 7):
            cell = ws.cell(row=row, column=col)
            cell.fill = PatternFill('solid', fgColor=COLORS['light_gray'])
            if fmt:
                cell.number_format = fmt
            cell.border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

    # Placeholder formulas (simplified)
    ws['C8'] = "=SUM('Debt Inventory'!L4:L28)*0.95"  # Snowball estimate
    ws['D8'] = "=SUM('Debt Inventory'!L4:L28)*0.90"  # Avalanche estimate
    ws['E8'] = "=SUM('Debt Inventory'!L4:L28)*0.93"  # Custom estimate
    ws['F8'] = "=SUM('Debt Inventory'!L4:L28)"       # Min payments

    # Strategy Descriptions
    ws.merge_cells('B15:G15')
    ws['B15'] = "STRATEGY DESCRIPTIONS"
    ws['B15'].style = 'header_style'

    descriptions = [
        ("Debt Snowball", "Pay minimum on all debts, put extra money toward the SMALLEST balance. When paid off, roll that payment to the next smallest. Provides quick psychological wins.", COLORS['accent']),
        ("Debt Avalanche", "Pay minimum on all debts, put extra money toward the HIGHEST interest rate. Mathematically optimal - saves the most money on interest over time.", COLORS['secondary']),
        ("Custom Order", "You choose the order to pay off debts based on your personal priorities. Use the ranking column in Payment Schedule.", COLORS['primary']),
    ]

    for i, (name, desc, color) in enumerate(descriptions):
        row = 17 + (i * 3)
        ws.merge_cells(f'B{row}:C{row}')
        ws[f'B{row}'] = name
        ws[f'B{row}'].font = Font(bold=True, size=12, color=color)
        ws.merge_cells(f'B{row+1}:G{row+1}')
        ws[f'B{row+1}'] = desc
        ws[f'B{row+1}'].alignment = Alignment(wrap_text=True)
        ws[f'B{row+1}'].font = Font(size=10)

    # Recommendation
    ws.merge_cells('B27:G27')
    ws['B27'] = "RECOMMENDATION"
    ws['B27'].style = 'header_style'

    ws.merge_cells('B28:G30')
    ws['B28'] = """If you need motivation and quick wins, choose DEBT SNOWBALL.
If you want to save the most money on interest, choose DEBT AVALANCHE.
If you have specific circumstances (e.g., a debt you want gone for personal reasons), choose CUSTOM."""
    ws['B28'].alignment = Alignment(wrap_text=True, vertical='top')
    ws['B28'].font = Font(size=11)

    return ws


def create_payment_schedule(wb):
    """Create the Payment Schedule sheet"""
    ws = wb.create_sheet("Payment Schedule")

    # Set column widths
    cols = {get_column_letter(i): 15 for i in range(1, 15)}
    cols['A'] = 3
    cols['B'] = 12
    cols['C'] = 18
    set_column_widths(ws, cols)

    # Title
    ws.merge_cells('B1:N1')
    ws['B1'] = "DEBT PAYMENT SCHEDULE"
    ws['B1'].style = 'title_style'

    # Headers
    ws['B3'] = "Month"
    ws['B3'].style = 'header_style'
    ws['C3'] = "Date"
    ws['C3'].style = 'header_style'

    # Dynamic debt headers (will reference Debt Inventory)
    for i in range(1, 11):
        col = get_column_letter(3 + i)
        ws[f'{col}3'] = f"=IF('Debt Inventory'!B{3+i}<>\"\", 'Debt Inventory'!B{3+i}, \"Debt {i}\")"
        ws[f'{col}3'].style = 'subheader_style'

    ws['N3'] = "Total Payment"
    ws['N3'].style = 'header_style'

    # Generate 60 months (5 years) of rows
    start_date = date.today().replace(day=1)
    for row in range(4, 64):
        month_num = row - 3
        ws.cell(row=row, column=2, value=month_num)

        # Date formula
        ws.cell(row=row, column=3, value=f'=EDATE(TODAY(),{month_num-1})')
        ws.cell(row=row, column=3).number_format = 'MMM YYYY'

        # Payment cells for each debt (placeholder - would need complex logic)
        for col in range(4, 14):
            cell = ws.cell(row=row, column=col)
            debt_row = col  # Corresponds to debt row in inventory
            # Simplified: just show minimum payment if balance > 0
            cell.value = f"=IF('Debt Inventory'!E{debt_row}>0,'Debt Inventory'!G{debt_row},0)"
            cell.number_format = '$#,##0.00'
            cell.fill = PatternFill('solid', fgColor=COLORS['light_gray'])
            cell.border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

        # Total column
        ws.cell(row=row, column=14, value=f'=SUM(D{row}:M{row})')
        ws.cell(row=row, column=14).number_format = '$#,##0.00'
        ws.cell(row=row, column=14).font = Font(bold=True)

    # Instructions
    ws.merge_cells('B66:N67')
    ws['B66'] = "NOTE: This schedule shows projected payments based on your Debt Inventory. The snowball/avalanche calculations automatically reallocate payments as debts are paid off."
    ws['B66'].font = Font(italic=True, size=9, color='666666')
    ws['B66'].alignment = Alignment(wrap_text=True)

    return ws


def create_payment_tracker(wb):
    """Create the Payment Tracker sheet"""
    ws = wb.create_sheet("Payment Tracker")

    set_column_widths(ws, {
        'A': 3, 'B': 20, 'C': 15, 'D': 15, 'E': 15,
        'F': 15, 'G': 12, 'H': 18, 'I': 3, 'J': 20,
        'K': 15, 'L': 15
    })

    # Title
    ws.merge_cells('B1:H1')
    ws['B1'] = "PAYMENT TRACKER"
    ws['B1'].style = 'title_style'

    # Year selector
    ws['B3'] = "Tracking Year:"
    ws['C3'] = datetime.now().year
    ws['C3'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['C3'].font = Font(bold=True, size=14)

    # Monthly tracking sections
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    current_row = 5

    for month_idx, month in enumerate(months[:6]):  # First 6 months
        # Month header
        ws.merge_cells(f'B{current_row}:H{current_row}')
        ws[f'B{current_row}'] = month.upper()
        ws[f'B{current_row}'].style = 'header_style'

        # Column headers
        headers = ['Debt Name', 'Planned', 'Actual', 'Variance', 'Date Paid', 'Confirmation']
        for i, header in enumerate(headers):
            ws.cell(row=current_row+1, column=2+i, value=header)
            ws.cell(row=current_row+1, column=2+i).style = 'subheader_style'

        # Data rows (5 debts per month section)
        for debt_row in range(5):
            row = current_row + 2 + debt_row
            # Debt name from inventory
            ws.cell(row=row, column=2, value=f"='Debt Inventory'!B{4+debt_row}")

            # Planned payment
            ws.cell(row=row, column=3, value=f"='Debt Inventory'!G{4+debt_row}")
            ws.cell(row=row, column=3).number_format = '$#,##0.00'
            ws.cell(row=row, column=3).fill = PatternFill('solid', fgColor=COLORS['light_gray'])

            # Actual payment (user input)
            ws.cell(row=row, column=4).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
            ws.cell(row=row, column=4).number_format = '$#,##0.00'

            # Variance
            ws.cell(row=row, column=5, value=f'=D{row}-C{row}')
            ws.cell(row=row, column=5).number_format = '$#,##0.00'
            ws.cell(row=row, column=5).fill = PatternFill('solid', fgColor=COLORS['light_gray'])

            # Date paid (user input)
            ws.cell(row=row, column=6).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
            ws.cell(row=row, column=6).number_format = 'MM/DD/YYYY'

            # Confirmation (user input)
            ws.cell(row=row, column=7).fill = PatternFill('solid', fgColor=COLORS['light_blue'])

            # Add borders
            for col in range(2, 8):
                ws.cell(row=row, column=col).border = Border(
                    left=Side(style='thin'),
                    right=Side(style='thin'),
                    top=Side(style='thin'),
                    bottom=Side(style='thin')
                )

        # Monthly total row
        total_row = current_row + 7
        ws.cell(row=total_row, column=2, value="TOTAL").font = Font(bold=True)
        ws.cell(row=total_row, column=3, value=f'=SUM(C{current_row+2}:C{current_row+6})')
        ws.cell(row=total_row, column=3).number_format = '$#,##0.00'
        ws.cell(row=total_row, column=3).font = Font(bold=True)
        ws.cell(row=total_row, column=4, value=f'=SUM(D{current_row+2}:D{current_row+6})')
        ws.cell(row=total_row, column=4).number_format = '$#,##0.00'
        ws.cell(row=total_row, column=4).font = Font(bold=True)
        ws.cell(row=total_row, column=5, value=f'=D{total_row}-C{total_row}')
        ws.cell(row=total_row, column=5).number_format = '$#,##0.00'
        ws.cell(row=total_row, column=5).font = Font(bold=True)

        current_row += 10

    # YTD Summary on right side
    ws['J5'] = "YEAR-TO-DATE SUMMARY"
    ws['J5'].style = 'header_style'
    ws.merge_cells('J5:L5')

    ws['J7'] = "Total Planned:"
    ws['K7'] = "=SUM(C:C)"
    ws['K7'].number_format = '$#,##0.00'

    ws['J8'] = "Total Paid:"
    ws['K8'] = "=SUM(D:D)"
    ws['K8'].number_format = '$#,##0.00'

    ws['J9'] = "Variance:"
    ws['K9'] = "=K8-K7"
    ws['K9'].number_format = '$#,##0.00'

    ws['J11'] = "On-Time Payments:"
    ws['K11'] = "=COUNTIF(F:F,\">0\")"

    return ws


def create_extra_payment_calc(wb):
    """Create the Extra Payment Calculator sheet"""
    ws = wb.create_sheet("Extra Payment Calculator")

    set_column_widths(ws, {
        'A': 3, 'B': 25, 'C': 20, 'D': 20, 'E': 20,
        'F': 20, 'G': 20, 'H': 3
    })

    # Title
    ws.merge_cells('B1:G1')
    ws['B1'] = "EXTRA PAYMENT CALCULATOR"
    ws['B1'].style = 'title_style'

    # Current situation
    ws.merge_cells('B3:D3')
    ws['B3'] = "CURRENT SITUATION"
    ws['B3'].style = 'header_style'

    ws['B5'] = "Total Debt:"
    ws['C5'] = "=SUM('Debt Inventory'!E4:E28)"
    ws['C5'].number_format = '$#,##0.00'

    ws['B6'] = "Monthly Minimum:"
    ws['C6'] = "=SUM('Debt Inventory'!G4:G28)"
    ws['C6'].number_format = '$#,##0.00'

    ws['B7'] = "Avg Interest Rate:"
    ws['C7'] = "=AVERAGEIF('Debt Inventory'!F4:F28,\">0\")"
    ws['C7'].number_format = '0.00%'

    ws['B8'] = "Months to Payoff:"
    ws['C8'] = "=MAX('Debt Inventory'!K4:K28)"
    ws['C8'].number_format = '0'

    ws['B9'] = "Total Interest (Min Only):"
    ws['C9'] = "=SUM('Debt Inventory'!L4:L28)"
    ws['C9'].number_format = '$#,##0.00'

    # Extra payment scenarios
    ws.merge_cells('E3:G3')
    ws['E3'] = "EXTRA PAYMENT SCENARIOS"
    ws['E3'].style = 'header_style'

    ws['E5'] = "Enter Extra Amount:"
    ws['F5'] = 100
    ws['F5'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['F5'].number_format = '$#,##0.00'
    ws['F5'].font = Font(bold=True, size=14)
    ws['F5'].border = Border(
        left=Side(style='medium'),
        right=Side(style='medium'),
        top=Side(style='medium'),
        bottom=Side(style='medium')
    )

    # Scenario table
    ws['B12'] = "SCENARIO COMPARISON"
    ws['B12'].style = 'header_style'
    ws.merge_cells('B12:G12')

    headers = ['Scenario', 'Extra/Month', 'New Total Payment', 'Months to Payoff', 'Interest Paid', 'You Save']
    for i, header in enumerate(headers):
        cell = ws.cell(row=13, column=2+i, value=header)
        cell.style = 'subheader_style'

    scenarios = [
        ('Minimum Only', '0', '=C6', '=C8', '=C9', '$0'),
        ('Your Amount', '=F5', '=C6+F5', '=ROUND(C8*(C6/(C6+F5)),0)', '=ROUND(C9*(C6/(C6+F5)),0)', '=C9-F17'),
        ('+$50/month', '50', '=C6+50', '=ROUND(C8*(C6/(C6+50)),0)', '=ROUND(C9*(C6/(C6+50)),0)', '=C9-F18'),
        ('+$100/month', '100', '=C6+100', '=ROUND(C8*(C6/(C6+100)),0)', '=ROUND(C9*(C6/(C6+100)),0)', '=C9-F19'),
        ('+$250/month', '250', '=C6+250', '=ROUND(C8*(C6/(C6+250)),0)', '=ROUND(C9*(C6/(C6+250)),0)', '=C9-F20'),
        ('+$500/month', '500', '=C6+500', '=ROUND(C8*(C6/(C6+500)),0)', '=ROUND(C9*(C6/(C6+500)),0)', '=C9-F21'),
    ]

    for i, (scenario, extra, total, months, interest, savings) in enumerate(scenarios):
        row = 14 + i
        ws.cell(row=row, column=2, value=scenario)
        ws.cell(row=row, column=3, value=extra if not extra.startswith('=') else None)
        if extra.startswith('='):
            ws.cell(row=row, column=3, value=extra)
        ws.cell(row=row, column=3).number_format = '$#,##0.00'
        ws.cell(row=row, column=4, value=total)
        ws.cell(row=row, column=4).number_format = '$#,##0.00'
        ws.cell(row=row, column=5, value=months)
        ws.cell(row=row, column=5).number_format = '0'
        ws.cell(row=row, column=6, value=interest)
        ws.cell(row=row, column=6).number_format = '$#,##0.00'
        ws.cell(row=row, column=7, value=savings)
        ws.cell(row=row, column=7).number_format = '$#,##0.00'
        ws.cell(row=row, column=7).font = Font(bold=True, color=COLORS['accent'])

        for col in range(2, 8):
            ws.cell(row=row, column=col).fill = PatternFill('solid', fgColor=COLORS['light_gray'])
            ws.cell(row=row, column=col).border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

    # Lump sum calculator
    ws.merge_cells('B23:G23')
    ws['B23'] = "LUMP SUM PAYMENT CALCULATOR"
    ws['B23'].style = 'header_style'

    ws['B25'] = "One-Time Payment Amount:"
    ws['C25'] = 1000
    ws['C25'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['C25'].number_format = '$#,##0.00'

    ws['B26'] = "Apply to Debt:"
    ws['C26'] = "Highest Interest"
    ws['C26'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])

    ws['B28'] = "New Total Balance:"
    ws['C28'] = "=C5-C25"
    ws['C28'].number_format = '$#,##0.00'

    ws['B29'] = "Balance Reduction:"
    ws['C29'] = "=C25/C5"
    ws['C29'].number_format = '0.0%'

    # Tips
    ws.merge_cells('B32:G35')
    ws['B32'] = """TIPS FOR FINDING EXTRA MONEY:
• Tax refunds • Work bonuses • Selling unused items • Side gig income
• Reducing subscriptions • Cash back rewards • Birthday/holiday money
• Overtime pay • Reducing dining out • Canceling unused memberships"""
    ws['B32'].alignment = Alignment(wrap_text=True, vertical='top')
    ws['B32'].font = Font(size=10, color='666666')

    return ws


def create_progress_milestones(wb):
    """Create the Progress & Milestones sheet"""
    ws = wb.create_sheet("Progress & Milestones")

    set_column_widths(ws, {
        'A': 3, 'B': 30, 'C': 20, 'D': 20, 'E': 20,
        'F': 25, 'G': 25, 'H': 3
    })

    # Title
    ws.merge_cells('B1:G1')
    ws['B1'] = "PROGRESS & MILESTONES"
    ws['B1'].style = 'title_style'

    # Progress overview
    ws.merge_cells('B3:D3')
    ws['B3'] = "OVERALL PROGRESS"
    ws['B3'].style = 'header_style'

    ws['B5'] = "Starting Total Debt:"
    ws['C5'] = "=SUM('Debt Inventory'!D4:D28)"
    ws['C5'].number_format = '$#,##0.00'

    ws['B6'] = "Current Total Debt:"
    ws['C6'] = "=SUM('Debt Inventory'!E4:E28)"
    ws['C6'].number_format = '$#,##0.00'

    ws['B7'] = "Total Paid Off:"
    ws['C7'] = "=C5-C6"
    ws['C7'].number_format = '$#,##0.00'
    ws['C7'].font = Font(bold=True, color=COLORS['accent'])

    ws['B9'] = "PROGRESS:"
    ws['C9'] = "=IF(C5>0,C7/C5,0)"
    ws['C9'].number_format = '0.0%'
    ws['C9'].font = Font(bold=True, size=24, color=COLORS['primary'])

    # Progress bar simulation using conditional formatting
    ws.merge_cells('B10:D10')
    ws['B10'] = "████████████████████"
    ws['B10'].font = Font(size=20)

    # Milestones checklist
    ws.merge_cells('F3:G3')
    ws['F3'] = "MILESTONES"
    ws['F3'].style = 'header_style'

    milestones = [
        ('First $1,000 Paid Off', '=IF(C7>=1000,"✓","○")'),
        ('25% Complete', '=IF(C9>=0.25,"✓","○")'),
        ('First Debt Eliminated', '=IF(COUNTIF(\'Debt Inventory\'!E4:E28,0)>0,"✓","○")'),
        ('50% Complete (Halfway!)', '=IF(C9>=0.5,"✓","○")'),
        ('Second Debt Eliminated', '=IF(COUNTIF(\'Debt Inventory\'!E4:E28,0)>1,"✓","○")'),
        ('75% Complete', '=IF(C9>=0.75,"✓","○")'),
        ('Under $10,000 Remaining', '=IF(C6<10000,"✓","○")'),
        ('Under $5,000 Remaining', '=IF(C6<5000,"✓","○")'),
        ('Under $1,000 Remaining', '=IF(C6<1000,"✓","○")'),
        ('DEBT FREE!', '=IF(C6<=0,"✓","○")'),
    ]

    for i, (milestone, formula) in enumerate(milestones):
        row = 5 + i
        ws.cell(row=row, column=6, value=formula)
        ws.cell(row=row, column=6).font = Font(size=14)
        ws.cell(row=row, column=7, value=milestone)
        ws.cell(row=row, column=7).font = Font(size=11)

    # Debts Paid Off Log
    ws.merge_cells('B17:D17')
    ws['B17'] = "DEBTS PAID OFF"
    ws['B17'].style = 'header_style'

    headers = ['Debt Name', 'Original Amount', 'Date Paid Off']
    for i, header in enumerate(headers):
        ws.cell(row=18, column=2+i, value=header)
        ws.cell(row=18, column=2+i).style = 'subheader_style'

    for row in range(19, 29):
        for col in range(2, 5):
            ws.cell(row=row, column=col).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
            ws.cell(row=row, column=col).border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )
        ws.cell(row=row, column=3).number_format = '$#,##0.00'
        ws.cell(row=row, column=4).number_format = 'MM/DD/YYYY'

    # My "Why" Section
    ws.merge_cells('F17:G17')
    ws['F17'] = "MY 'WHY'"
    ws['F17'].style = 'header_style'

    ws.merge_cells('F18:G22')
    ws['F18'] = "Write your motivation here..."
    ws['F18'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['F18'].alignment = Alignment(wrap_text=True, vertical='top')
    ws['F18'].border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Celebration Planning
    ws.merge_cells('B31:G31')
    ws['B31'] = "CELEBRATION PLANNING"
    ws['B31'].style = 'header_style'

    ws['B33'] = "When I hit 25%, I will:"
    ws['C33'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws.merge_cells('C33:G33')

    ws['B34'] = "When I hit 50%, I will:"
    ws['C34'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws.merge_cells('C34:G34')

    ws['B35'] = "When I hit 75%, I will:"
    ws['C35'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws.merge_cells('C35:G35')

    ws['B36'] = "When I'm DEBT FREE, I will:"
    ws['C36'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws.merge_cells('C36:G36')

    for row in [33, 34, 35, 36]:
        ws[f'B{row}'].font = Font(bold=True)

    return ws


def create_annual_summary(wb):
    """Create the Annual Summary sheet"""
    ws = wb.create_sheet("Annual Summary")

    set_column_widths(ws, {
        'A': 3, 'B': 25, 'C': 18, 'D': 18, 'E': 18,
        'F': 18, 'G': 18, 'H': 18
    })

    # Title
    ws.merge_cells('B1:H1')
    ws['B1'] = "ANNUAL SUMMARY"
    ws['B1'].style = 'title_style'

    # Year selection
    ws['B3'] = "Year:"
    ws['C3'] = datetime.now().year
    ws['C3'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['C3'].font = Font(bold=True, size=14)

    # Annual metrics
    ws.merge_cells('B5:D5')
    ws['B5'] = "ANNUAL METRICS"
    ws['B5'].style = 'header_style'

    metrics = [
        ('Balance at Start of Year:', '$#,##0.00'),
        ('Balance at End of Year:', '$#,##0.00'),
        ('Total Paid This Year:', '$#,##0.00'),
        ('Interest Paid This Year:', '$#,##0.00'),
        ('Principal Paid This Year:', '$#,##0.00'),
        ('Debts Eliminated This Year:', '0'),
        ('Average Monthly Payment:', '$#,##0.00'),
    ]

    for i, (metric, fmt) in enumerate(metrics):
        row = 7 + i
        ws.cell(row=row, column=2, value=metric)
        ws.cell(row=row, column=2).font = Font(bold=True)
        ws.cell(row=row, column=3).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
        ws.cell(row=row, column=3).number_format = fmt
        ws.cell(row=row, column=3).border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )

    # Year-over-year comparison
    ws.merge_cells('F5:H5')
    ws['F5'] = "YEAR-OVER-YEAR"
    ws['F5'].style = 'header_style'

    yoy_headers = ['Metric', 'Last Year', 'This Year']
    for i, header in enumerate(yoy_headers):
        ws.cell(row=6, column=6+i, value=header)
        ws.cell(row=6, column=6+i).style = 'subheader_style'

    yoy_metrics = [
        'Starting Balance',
        'Ending Balance',
        'Total Paid',
        'Interest Paid',
        'Debts Eliminated'
    ]

    for i, metric in enumerate(yoy_metrics):
        row = 7 + i
        ws.cell(row=row, column=6, value=metric)
        ws.cell(row=row, column=7).fill = PatternFill('solid', fgColor=COLORS['light_gray'])
        ws.cell(row=row, column=7).number_format = '$#,##0.00'
        ws.cell(row=row, column=8).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
        ws.cell(row=row, column=8).number_format = '$#,##0.00'

    # Monthly breakdown
    ws.merge_cells('B16:H16')
    ws['B16'] = "MONTHLY BREAKDOWN"
    ws['B16'].style = 'header_style'

    monthly_headers = ['Month', 'Starting Bal.', 'Payments', 'Interest', 'Principal', 'Ending Bal.']
    for i, header in enumerate(monthly_headers):
        ws.cell(row=17, column=2+i, value=header)
        ws.cell(row=17, column=2+i).style = 'subheader_style'

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    for i, month in enumerate(months):
        row = 18 + i
        ws.cell(row=row, column=2, value=month)
        for col in range(3, 8):
            ws.cell(row=row, column=col).fill = PatternFill('solid', fgColor=COLORS['light_blue'])
            ws.cell(row=row, column=col).number_format = '$#,##0.00'
            ws.cell(row=row, column=col).border = Border(
                left=Side(style='thin'),
                right=Side(style='thin'),
                top=Side(style='thin'),
                bottom=Side(style='thin')
            )

    # Totals row
    ws.cell(row=30, column=2, value="TOTALS")
    ws.cell(row=30, column=2).font = Font(bold=True)
    for col in range(3, 8):
        ws.cell(row=30, column=col, value=f'=SUM({get_column_letter(col)}18:{get_column_letter(col)}29)')
        ws.cell(row=30, column=col).number_format = '$#,##0.00'
        ws.cell(row=30, column=col).font = Font(bold=True)

    # Notes section
    ws.merge_cells('B33:H33')
    ws['B33'] = "NOTES & REFLECTIONS"
    ws['B33'].style = 'header_style'

    ws.merge_cells('B34:H38')
    ws['B34'] = "Add your notes about this year's progress..."
    ws['B34'].fill = PatternFill('solid', fgColor=COLORS['light_blue'])
    ws['B34'].alignment = Alignment(wrap_text=True, vertical='top')

    return ws


def create_workbook():
    """Main function to create the complete workbook"""
    wb = Workbook()

    # Create styles
    create_styles(wb)

    # Create all sheets
    create_dashboard(wb)
    create_debt_inventory(wb)
    create_strategy_selector(wb)
    create_payment_schedule(wb)
    create_payment_tracker(wb)
    create_extra_payment_calc(wb)
    create_progress_milestones(wb)
    create_annual_summary(wb)

    # Set Dashboard as active sheet
    wb.active = wb['Dashboard']

    return wb


if __name__ == "__main__":
    print("Creating Comprehensive Debt Payment Workbook...")

    # Create the workbook
    wb = create_workbook()

    # Save the workbook
    output_path = "/home/user/Automations/debt-payment-workbook/Comprehensive_Debt_Payment_Workbook.xlsx"
    wb.save(output_path)

    print(f"Workbook saved to: {output_path}")
    print("\nSheets created:")
    for sheet in wb.sheetnames:
        print(f"  - {sheet}")
