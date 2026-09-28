b= float(input("Enter basic salary"))
hra= b*20/100
ta= b*5/100
da= b*10/100
g_salary= b+hra+ta+da
print(g_salary)
if g_salary<=300000:
    tax=0
elif g_salary<=1000000:
    tax= g_salary*10/100
elif g_salary<=2500000:
    tax= g_salary*20/100
else:
    tax= g_salary*30/100
print("Income Tax",tax)
