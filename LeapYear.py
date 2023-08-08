# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

century4 = year % 400 
century  = year % 100
year4    = year % 4

if century4 == 0:
    print ("Leap year")
elif century == 0:
    print("Not leap")
elif year4 ==0: 
    print("Leap year ")
else :
    print("Not leap")   



