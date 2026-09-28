i= int(input("Enter taxable income"))
if i<=20000:
    tax=0.2*i
elif i<=50000:
    tax=400+0.025*(i-20000)
else:
    tax=1150+0.035*(i-50000)
print(tax)