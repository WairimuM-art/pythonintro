# Create a program that calculates your bmi

height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/height**2
print("Your BMI is:",bmi)
if bmi<18.5:
    print("Your BMI is normal")
elif 18.5 <= bmi < 25:
    print("Your BMI is obese")
else:
    print("Your BMI is overweight")
