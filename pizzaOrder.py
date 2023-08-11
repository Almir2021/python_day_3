# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzaPrice = 0

if size == "S" or size == "s":
   pizzaPrice +=15
if add_pepperoni == "Y" and size == "S":
    pizzaPrice +=2 
elif extra_cheese == "Y" and size == "S":
          pizzaPrice +=1


if size == "M" or size ==  "m":
   pizzaPrice +=20
if add_pepperoni == "Y" and size == "M":
     pizzaPrice +=3
elif   extra_cheese == "Y"  and size == "M":
      pizzaPrice +=1 

if size == "L"  or size == "l":
 pizzaPrice +=25
if add_pepperoni == "Y" and size == "L" :
     pizzaPrice +=3
elif   extra_cheese == "Y" and size == "L":
      pizzaPrice +=1 


print(f"Your final bill is: ${pizzaPrice}")




