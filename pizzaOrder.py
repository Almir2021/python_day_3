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
elif size == "M" or size ==  "m":
   pizzaPrice +=20
else:
 pizzaPrice +=25


if pizzaPrice == 15:
  if add_pepperoni == "Y" or add_pepperoni == "y": 
    pizzaPrice +=2 
elif extra_cheese == "Y" or extra_cheese =="y":
          pizzaPrice +=1


if pizzaPrice == 25:
   if add_pepperoni == "Y" or add_pepperoni == "y":
     pizzaPrice +=3
elif   extra_cheese == "Y" or extra_cheese =="y":
      pizzaPrice +=1 



if pizzaPrice == 25:
 if add_pepperoni == "Y" or add_pepperoni == "y":
  pizzaPrice +=3
elif   extra_cheese == "Y" or extra_cheese =="y":
   pizzaPrice +=1 



print(f"Your final bill is: ${pizzaPrice}")




