"""
Author: [Natanya Anderson]
Assignment / Part: HW4 - Q5 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask user for integer value, representing number of players who played.
# Miniumum of players is @ and maximum is 8. If user enters invalid input, keep asking user input until correct.
# Once input is valid, each player will enter values of their properties/assets.
# Once players have entered values, game will print out sum.
# Program repeats steps until all players are accounted for.
# Output will be which player has the most money.
sum = 0
i = 0
player_asset_max = 0
player_asset_max_number = 0
num_of_players = int(input("Enter a valid number of players: "))
while num_of_players < 2 or num_of_players > 8:
    print("Minimum amount of players is 2 and maximum is 8")
    num_of_players = int(input("Enter a valid number of players: "))


for i in range(1, num_of_players+1):
    player_asset = ""
    while player_asset != "DONE":
        player_asset = input("Enter the value of a property/asset, or DONE to finish: ")
        if player_asset != "DONE":
            sum += int(player_asset)
        else:
            print("Player " + str(i) + " has " + str(float(sum)) + " dollars.")
            if sum > player_asset_max:
                player_asset_max_number = i
                player_asset_max = float(sum)
            sum = 0
print(str(player_asset_max_number) + " wins with " + str(player_asset_max) + " dollars!")

  #  print("Player " + str(player_asset_max_number) + " is the winner!")




#print("Player " + str(i) + " is the winner!")
           # else:
               # print("Player " + str(i) + " is the winner!")
#if winner == results:
    #print(str(i) + " wins with " + str(float(winner)) + " dollars!")


    #sum_one = player_asset_one + player_asset_two
   # print("Player one has " + round(sum_one, 1) + "dollars.")
    #if player_asset_two == "DONE":


