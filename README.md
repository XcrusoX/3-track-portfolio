# 3-Track-Portfolio

This repository hosts three independent Business Analysis projects.  
Below you’ll find Projects 1 and 2 fully scoped, documented and delivered.  
Project 3 folder structure will go here when you start.

---

## Project 1: Invoice Automation

├── **docs/**  
│   ├── cost-benefits-gap-analysis.md  
│   ├── implementation-roadmap.md  
│   ├── interview-deck.md  
│   ├── kpi-scorecard.md  
│   ├── requirements.md  
│   ├── stakeholder-plan.md  
│   ├── stakeholder-raci.md  
│   ├── roi-analysis.md  
│   └── uat-summary.md  

├── **data/**  
│   ├── cashflow.csv  
│   ├── cashflow_cleaned.csv  
│   └── cashflow_cleaned.xlsx  

├── **diagrams/**  
│   ├── as-is_flowchart.png  
│   ├── invoice_pipeline_flowchart.png  
│   └── to-be_flowchart.png  

├── **report/**  
│   └── cashflow_report.pbix  

└── **script/**  
    ├── ap.py  
    ├── clean_cashflow.py  
    └── gen_dummy.py  

---

## Project 2: Customer Success

├── **docs/**  
│   ├── cs_deck_outline.md  
│   ├── cs_stakeholder_plan.md  
│   └── cs_success_metrics.md  

├── **diagrams/**  
│   └── service_journey.png  

└── **slides/**  
    └── customer_success.pptx  

---

## How to run

### Project 1  
1. `cd script`  
2. `pip install -r requirements.txt`  
3. `python gen_dummy.py` (seed sample data)  
4. `python ap.py` (start Flask webhook)  
5. Open `report/cashflow_report.pbix` in Power BI Desktop  

### Project 2  
1. Open `slides/customer_success.pptx` to review deck  
2. Refer to `.md` in `docs/` for journey, stakeholders & metrics  

---

## Next Steps

- Push Project 3 folder when you’re ready to start your third case study.  
- For any updates, simply add or edit files, then commit & push.

