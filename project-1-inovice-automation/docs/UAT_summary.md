# UAT Summary

## Test Case HP-001: Happy Path
Precondition:
- Invoice #123 exists in DB, status = “Pending”, due_date = today
Steps:
1. Trigger the reminder flow or run `send_reminders()` script  
2. Verify reminder email is sent to customer’s email  
3. POST to `/payment` webhook with JSON `{"invoice_id":123, "status":"Paid"}`  
4. Confirm DB record for invoice #123 updates to status = “Paid”  
Expected Result:
- Email delivered, webhook returns 204, DB status = “Paid”  
Actual Result:  
Status (Pass/Fail):  

## Test Case EC-001: Duplicate Callback
Precondition:
- Invoice #123 already marked “Paid”
Steps:
1. POST to `/payment` webhook with JSON `{"invoice_id":123, "status":"Paid"}` again  
2. Observe system behavior  
Expected Result:
- No status change, logs “Already Paid” warning, returns 200 or 204  
Actual Result:  
Status (Pass/Fail):  

## Test Case EC-002: Invalid Invoice ID
Precondition: none
Steps:
1. POST to `/payment` webhook with JSON `{"invoice_id":999, "status":"Paid"}`  
Expected Result:
- Returns 404 or 400 with error “Invoice Not Found”  
Actual Result:  
Status (Pass/Fail):  

## Test Case EC-003: Missing Fields
Precondition: none
Steps:
1. POST to `/payment` webhook with JSON `{"invoice_id":123}` (no status)  
Expected Result:
- Returns 400 with error “invoice_id and status required”  
Actual Result:  
Status (Pass/Fail):  

## Test Case EC-004: Invalid JSON
Precondition: none
Steps:
1. POST to `/payment` webhook with a non-JSON payload (e.g., plain text)  
Expected Result:
- Returns 400 with error “Invalid payload format”  
Actual Result:  
Status (Pass/Fail):  

## Test Case EC-005: Network Failure Retry
Precondition:
- Simulate network drop on email send
Steps:
1. Trigger reminder flow during network outage  
2. Observe retry logic  
Expected Result:
- Flow retries configured times, logs failure after last retry  
Actual Result:  
Status (Pass/Fail):  

---

**Lessons Learned / Fixes Needed**  
- 
