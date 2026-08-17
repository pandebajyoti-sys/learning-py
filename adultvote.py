age= int(input("Enter your age:"))
print("Your age is:"+ str(age))
if  age>=18:
   print("You are an adult")
   print("You are eligible to vote")
   
elif age<18 and age>6:
   print("You are in school")
   print("You are not eligible to vote")   
   
else:
   print("You are a kid")
   
   
print("Thank you")   