# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzaPrice = 0 

if size == "S" or size ==  "s":
  pizzaPrice +=15
elif add_pepperoni == "Y" or add_pepperoni == "y":
  pizzaPrice +=2
elif   extra_cheese == "Y" or extra_cheese =="Y":
  pizzaPrice +=1 


if size == "M" or size ==  "m":
   pizzaPrice +=20

elif add_pepperoni == "Y" or add_pepperoni == "y":
  pizzaPrice +=3

elif   extra_cheese == "Y" or extra_cheese =="Y":
  pizzaPrice +=1 



if size == "L" or size == "l" :
 pizzaPrice +=25

elif add_pepperoni == "Y" or add_pepperoni == "y":
  pizzaPrice +=3

elif   extra_cheese == "Y" or extra_cheese =="Y":
  pizzaPrice +=1 


print(f"Your final bill is: ${pizzaPrice}")
