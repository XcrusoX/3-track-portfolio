import pandas as pd

# 1. Load raw data
df = pd.read_csv('../data/cashflow.csv',
                 parse_dates=['InvoiceDate','PaymentDate'])

# 2. Calculate metrics
df['DaysOutstanding'] = (df.PaymentDate - df.InvoiceDate).dt.days
df['NetCash']        = df.AmountPaid - df.AmountInvoiced

# 3. Save the cleaned file
out_path = '../data/cashflow_cleaned.csv'
df.to_csv(out_path, index=False)
print(f"Cleaned data saved to {out_path}")
