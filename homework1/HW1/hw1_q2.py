"""
Author: [Natanya Anderson]
Assignment / Part: HW1 - Q2 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
year_str = input("Please enter a year greater than 2022:")
year = int(year_str)
current_population = 330109174
seconds_in_hour = 60*60
hours_in_day = 24
seconds_in_year = 365*hours_in_day*seconds_in_hour
number_of_years = year-2022
#print(number_of_years)
total_seconds = number_of_years*seconds_in_year
new_born = total_seconds//9
#print(new_born)
death = total_seconds//18
#print(death)
immigrant = total_seconds//40
#print(immigrant)
emigration = total_seconds//60
population_change = new_born-death+immigrant-emigration
final_population = population_change+current_population
answer = "The population in year " + str(year) + " will be " + str(final_population)
print(answer)