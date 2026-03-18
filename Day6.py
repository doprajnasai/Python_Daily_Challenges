n = int(input("Enter number of transactions:"))
transactions = []
for i in range(n):
    t = int(input("Enter transaction amount:"))
    transactions.append(t)
categories = {
    "normal":[],
    "large":[],
    "high_risk":[],
    "invalid":[]
}
for t in transactions:
    if(t <= 0):
        categories["invalid"].append(t)
    elif(t <= 500):

        categories["normal"].append(t)
    elif(t <= 2000):
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)
valid_transactions = [t for t in transactions if t>0]
sum_transactions = 0
for t in valid_transactions:
    sum_transactions += t
h_risk_count = len(categories["high_risk"])
frequent = len(valid_transactions) > 5
large_spend = sum_transactions > 5000
suspicious = h_risk_count >= 3
if suspicious and frequent:
    risk = "High risk"
elif frequent and large_spend:
    risk = "Medium risk"
else:
    risk = "Low risk"

transaction_summary = (
    sum_transactions,
    h_risk_count,
    len(valid_transactions)
)

print(("categorized Transactions"))
print("Invalid Transactions:",categories["invalid"])
print("Normal Transactions:",categories["normal"])
print("Large Transactions:",categories["large"])
print("High Risk Transactions:",categories["high_risk"])

print("Summary")
print("Total transactional value:",transaction_summary[0])
print("Number of Transactions:",transaction_summary[2])
print("Number of High risk Transactions:",transaction_summary[1])

print("Risk Classification:",risk)
