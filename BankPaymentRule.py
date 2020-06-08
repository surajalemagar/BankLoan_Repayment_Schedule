time=120
principal=float(2000000)
payment=float(31150)
rate=14
rate_month=float(14/1200)
total=float(0)
total_interest=float(0)
total_interest=float(0)
for i in range(120):
    interest=float(rate_month*principal)
    deducted_principal=payment-interest
    principal-=deducted_principal
    total_interest+=interest
    i=i+1
    print(i)
    print("Payment is :",payment)
    print("Interest is :",interest)
    print("Deducted amount in Principal is :",deducted_principal)
    print("New Principal is :",principal)
    print("Total Interest Till Now is :",total_interest)
    print("\n")


