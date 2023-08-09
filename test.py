print("Welcome to the rollercoaster")
height = int(input("what is your height in cm?"))
bill = 0 
if height > 120 :
    print("You can ride ")
    age = int(input("what is your age "))
    if age <12: 
     bill = 5
     print ("Child ticket are 5$ ")
    elif  age <= 18 :
       bill = 7
       print("Youth tickets are 7$ ")
    else:
      bill = 12
      print(" Adult tickets are  12$  ")

    wantsPhoto =  input ("Do you want a photo taken? Y or N. ")

    if wantsPhoto == "Y" or wantsPhoto == "y" :
       bill += 3
       print(f"Your price ticke is price {bill}$ ")
       if wantsPhoto == "N" or wantsPhoto == "n":
        print(f"Your price ticke is price {bill}$ ") 


else :
   print("You can't ride")
