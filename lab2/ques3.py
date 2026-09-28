h=float(input("Enter Heigth"))
wt=float(input("Enter Weight"))
bmi=wt/(h**2)
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal Weight")
elif bmi<30:
    print("Slighty Overweight")
elif bmi<35:
    print("Obese")
else:
    print("Clinically Obese")