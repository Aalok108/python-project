cost_price=int(input("enter the cost price"))
if(cost_price>100000):
    a=15/100*cost_price
    print(a)
elif(cost_price>50000 and cost_price<=100000):
    b=10/100*cost_price
    print(b)
elif(cost_price<=50000):
    c=5/100*cost_price
    print(c)
else:
    print("no tax")  
       