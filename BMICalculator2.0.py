# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi= weight/ (height**2)

bmi = round( (bmi),1)

if bmi<18.5:
    print(f"Your BMI is {bmi} , you are underweight.")
elif bmi < 22 :
        print(f"Your BMI is {bmi} , you have a normal weight.")
elif bmi < 28 :
        print(f"Your BMI is {bmi} , you are a  slightly overweight.")
elif bmi < 33 :
        print(f"Your BMI is {bmi} , you are obese.")
elif bmi < 40 :
        print(f"Your BMI is {bmi} , you are clinically obese.")
