# Business Requirements Document  

**Project:** Invoice → Cash-Flow Pipeline  
**Goal:** Reduce Days Outstanding and automate reminders to improve cash flow by 10%.

## Business Requirements  
1. The system shall flag invoices X days before due date.  
2. The system shall send automated reminder emails at configurable intervals (e.g., 5, 15, 30 days past due).  
3. The AR Manager shall receive a weekly summary of invoices >30 days outstanding.  
4. The dashboard shall display real-time cash-flow impact for reminder scenarios.
### User Story 1
**As an** AR Clerk  
**I want** the system to send a reminder email 5 days before an invoice’s due date  
**So that** I can prompt customers early and reduce late payments  

**Acceptance Criteria:**  
- Email includes invoice number, due date, and payment link  
- Automatically sends when `ReminderDays = 5`  
- Dashboard shows count of “5-day reminders sent”

### User Story 2
**As an** AR Manager  
**I want** to receive a weekly summary report of invoices >30 days overdue  
**So that** I can prioritize escalations and allocate resources effectively  

**Acceptance Criteria:**  
- Report auto-generates every Monday at 9 AM  
- Contains customer name, invoice date, days outstanding, and amount due  
- Accessible via Power BI dashboard and emailed as a PDF  

### User Story 3
**As a** Finance Lead  
**I want** to adjust reminder intervals (e.g., 5, 15, 30 days) via a slider  
**So that** I can model how different strategies impact cash flow in real time  

**Acceptance Criteria:**  
- “What-If” slider controls `ReminderDays` values  
- Net Cash w/ Reminder card and charts update instantly  
- Valid values: 0–60 days in 5-day increments
