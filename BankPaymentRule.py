# Create Bank Loan Repayment Schedule
# Calculate Required Monthly Repayment Amount 


def Calculate_Monthly_Payment(P,T,R):
    RY=float(R/100)             #Calculating Yearly Rate of Interest
    RM=float(RY/12)             #Calculating Monthly Rate of Interest
    N=float(T*12)               #Calculating Number of Period
    x=(RM*P)/(1-(1+RM)**(-N))   #Calculating Required Monthly Payment Amount
    return x

def Repayment_Schedule(P,T,R,MP):
    Total_Interest=float(0)
    Total_Payment=float(0)
    RY=float(R/100)             #Calculating Yearly Rate of Interest
    RM=float(RY/12)             #Calculating Monthly Rate of Interest
    N=float(T*12)  
    for i in range(int(N)):
        I=float(RM*P)
        Deducted_P=MP-I
        P-=Deducted_P
        Total_Interest+=I
        Total_Payment+=MP
        i=i+1
        print(i)
        print("Payment is :",MP)
        print("Interest is :",I)
        print("Deducted amount in Principal is :",Deducted_P)
        print("New Principal is :",P)
        print("Total Interest Till Now is :",Total_Interest)
        print("Total Payment Till Now is :",Total_Payment)
        print("\n")
P=float(input("Enter The Principal :"))
T=float(input("Enter The Years :"))
R=float(input("Enter The Rate :"))
MP=Calculate_Monthly_Payment(P,T,R)
Repayment_Schedule(P,T,R,MP)