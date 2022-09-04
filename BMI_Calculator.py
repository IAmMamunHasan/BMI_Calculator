w = float(input("weight in kg "))
h = float(input("height in meters "))
BMI = w / h ** 2
print("Your BMI is " + str(BMI))
if BMI < 18.5:
    print("you are underweight")
elif BMI < 24.9:
    print("your BMI is normal")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
