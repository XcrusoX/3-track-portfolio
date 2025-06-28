# Gap Analysis: Invoice Reminder Automation

| As-Is Process Step                                   | Pain Point                                                | To-Be Automated Step                                    | Proposed Fix                                  |
|-------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------|
| AR Clerk checks due date manually                     | Inconsistent timing, forgot reminders                     | System evaluates due date automatically                  | Schedule a Power Automate flow to run nightly |
| AR Clerk sends reminders at 5/15/30 days              | Manual emails → error-prone, high workload                | Trigger reminder email via Power Automate                | Build email template + timed flows           |
| Customer pays; AR Clerk updates ledger manually       | Delays in data entry → reporting lags                     | Auto-update ledger via webhook/ETL to ERP                | Write Python/webhook script to post payments |
| Escalation triggered by AR Clerk if >30 days overdue  | Reactive, inconsistent follow-up                          | Automated escalation alert to AR Manager                 | Add “Wait X days” timer + escalation flow    |
