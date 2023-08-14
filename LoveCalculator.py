# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 
insideCount3 = 0
insideCount1 = 0
name1 = name1.lower()

name2 = name2.lower()

programming_language = name1

programming_language_list = list(programming_language)



programming_language2 = name2

programming_language2_list = list(programming_language2)


 
joinedlist = programming_language2_list  + programming_language_list


  
True1 = ["t","r" ,"u" ,"e"]
for count1 in True1:
 insideCount2 = joinedlist.count(count1)
 insideCount1 += insideCount2



Love = ["l","o" ,"v" ,"e"]
for count2 in Love:
 insideCount = joinedlist.count(count2)
 insideCount3  += insideCount 



finalScore = (insideCount1 *10) + insideCount3

if finalScore <10 or finalScore > 90 :
 print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore >=40 and finalScore <= 50 :
 print(f"Your score is {finalScore} , you are alright together.")
else :
 print(f"Your score is {finalScore}.") 