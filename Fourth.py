name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height * height)
print(f"Hello, {name}! Based on your age of {age} years, height of {height}, and weight of {weight}, your BMI is: {bmi:.2f}")

exit()
