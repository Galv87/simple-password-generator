

#for randomization
import random
#Call lettters from the keyboard
import string

#selceting what characters can be called no spaces
characters = string.ascii_letters + string.digits + "-"

#ask for user input and put result as integer
length = int(input("enter password length: "))

#empty string funtion for result
password = ""

#take password length and put the result into password += means add it all to one line
for i in range(length):
    password += random.choice(characters)
#join function i:i+4 seperates into chunks of 4 
#i in range then has a start at 0 for the length of the password and 4 at a time
    grouped_password = "-".join(password[i:i+4] for i in range(0, len(password), 4))
#display result
print("your strong password is: ", grouped_password)
