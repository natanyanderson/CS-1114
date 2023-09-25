"""
Author: [Natanya Anderson]
Assignment / Part: HW1 - Q4 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount of dollars and cents, in two separate lines")
dollar = int(input())
cents = int(input())
Money = (dollar*100) + cents
quarter = int(Money//25)
change_left_one = (Money-(25*quarter))
dimes = int(change_left_one//10)
change_left_two = (change_left_one-(dimes*10))
nickels = int(change_left_two//5)
change_left_three = (change_left_two-(nickels*5))
pennies = int(change_left_three//1)
print(dollar, 'dollars and',cents,'cents are:',quarter, "quarters, ",dimes,"dimes, " ,nickels,"nickels and ",pennies,"pennies")

#temp = change_left_two-0.05
#print(temp)
#nickels = (dimes//0.05)
#print(quarter)
#print(dimes)
#print(nickels)

#print(Money)
#print(quarter)
#print(change_left_one)
#print(dimes)
#print(change_left_two)
#print(nickels)
#print(change_left_three)
#print(pennies)



#quarters = 17*.25
#print (quarters)
