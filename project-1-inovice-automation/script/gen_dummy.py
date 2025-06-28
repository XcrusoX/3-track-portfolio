import pandas as pd, numpy as np

n = 20
start = pd.to_datetime('2025-01-01')
df = pd.DataFrame({
    'InvoiceID': [f'INV{1000+i}' for i in range(n)],
    'InvoiceDate': pd.date_range(start, periods=n, freq='5D')
})
# simulate payment delays
df['PaymentDate'] = df.InvoiceDate + pd.to_timedelta(
    np.random.randint(10, 50, size=n), unit='D')
# simulate amounts
df['AmountInvoiced'] = np.random.randint(10000, 30000, size=n)
df['AmountPaid'] = df.AmountInvoiced - np.random.randint(-500, 500, size=n)

df.to_csv('../data/cashflow.csv', index=False)
print(f"Dummy data created: {n} rows in data/cashflow.csv")
