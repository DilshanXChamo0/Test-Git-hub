bill_total=int(input("Enter your totla bill: "))
if bill_total >= 5000:
    print("Your Discount is: 10%")
    Discount = 10/100
    netpay = (bill_total*Discount)
    total_payment=(bill_total-netpay)
    print("your bill is: ",total_payment)
else:
     print("Your Discount is: 5%")
     Discount = 5/100
     netpay = (bill_total*Discount)
     total_payment=(bill_total-netpay)
     print("your bill is: ",total_payment)
     
    
    
