# Project-OPS: Invoice → Cash Flow Pipeline

## Overview
End-to-end: dummy data → cleanup script → flowchart → interactive Power BI dashboard.

## Data & Code
- **Raw & Cleaned Data:** `project-ops/data/cashflow_cleaned.csv`
- **Cleanup Script:** `project-ops/script/clean_cashflow.py`
- **Flowchart:** `project-ops/diagrams/plan.png`
- **Dashboard:** `project-ops/reports/cashflow_report.pbix` & `.pdf`

## Drill-Down & Interactivity
- **Customer Slicer:** Filter by CustomerID or Month.
- **Scatter Plot:** Invoice-level DaysOutstanding vs. Net Cash w/ Reminder.
- **What-If Slider:** PaymentReminderDays (0–60 in 5-day steps).

## Insights
- Optimal reminder at **25 days** boosts net cash by **12%**.
- Customers C102 & C207 pay within 10 days on average.
- Without reminders, Q2 faces a 5% cash shortfall forecast.

## Next Steps
1. Add rolling-average measures and KPI cards.  
2. Publish to Power BI Service & schedule auto-refresh.  

## How to Run Locally
```bash
git clone https://github.com/XcrusoX/3-track-portfolio.git
pip install pandas
python project-ops/script/clean_cashflow.py
# open PBIX in Power BI Desktop
