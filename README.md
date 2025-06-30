# 3-Track-Portfolio

This repository contains three independent BA projects.

---

## Project 1: Invoice Automation

├── docs/  
│   ├── cost-benefits-gap-analysis.md  
│   ├── implementation-roadmap.md  
│   ├── interview-deck.md  
│   ├── kpi-scorecard.md  
│   ├── requirements.md  
│   ├── stakeholder-plan.md  
│   ├── stakeholder-raci.md  
│   ├── roi-analysis.md  
│   └── uat-summary.md  

├── data/  
│   ├── cashflow.csv  
│   ├── cashflow_cleaned.csv  
│   └── cashflow_cleaned.xlsx  

├── diagrams/  
│   ├── as-is_flowchart.png  
│   ├── invoice_pipeline_flowchart.png  
│   └── to-be_flowchart.png  

├── report/  
│   └── cashflow_report.pbix  

└── script/  
    ├── ap.py  
    ├── clean_cashflow.py  
    └── gen_dummy.py  

### How to run Project 1

1. `cd script`  
2. `pip install -r requirements.txt` (if you have one)  
3. `python gen_dummy.py` (optional data seeding)  
4. `python ap.py` to start the Flask webhook  
5. Open `report/cashflow_report.pbix` in Power BI  

---

## Project 2 & 3

Coming soon—service journeys, stakeholder plans, success matrices, etc.
