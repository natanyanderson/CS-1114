"""
Author: [Natanya Anderson]
Assignment / Part: HW1 - Q3 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
print("Please enter number of coins:")
quarters = int(input("Number of quarters: "))
dimes = int(input("Number of dimes: "))
nickels = int(input("Number of nickels: "))
pennies = int(input("Number of pennies: "))
quarters_sum = (quarters*.25)
dimes_sum = (dimes*.10)
nickels_sum = (nickels*.05)
pennies_sum = (pennies*.01)
#dollar = quarters_sum + dimes_sum + pennies_sum
#print (dollar + nickels_sum)
Total = quarters_sum + dimes_sum + nickels_sum + pennies_sum
Dollar_equal = int(Total//1)
Cents_equal = int((Total%Dollar_equal)*100)
answer = "The total is " + str(Dollar_equal) + " dollar(s) and " + str(Cents_equal) + " cent(s)"
print(answer)

#quarters_in_dollar = 4*.25
#dimes_in_dollar = 10*.10
#nickels_in_dollar = 20*.05
#pennies_in_dollar = 100*0.01


