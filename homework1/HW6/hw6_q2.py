"""
Author: [Natanya Anderson]
Assignment / Part: HW6 - Q2 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Function called get_decimal_time(hour,minute,second)
# print function in format "HOUR:MIN:SEC"
# French revolutionary days each have 10 hours, 100 minutes, 100 seconds
# Function called get_decimal_date(month,date_of_month,common_era_year)
# print function in format "[Day] [month] [year], Décade [décade]"
# Months in system only have 10 days weeks, figure out décade by checking which of the weeks the current date is in
# Function called get_french_datetime(gregorian_date_and_time)
# Isolate each piece of information and pass relevant information to get_decimal_time() and get_decimal_date()

def get_decimal_time(hour,minute,second):
    minute_to_seconds = minute * 60
    hours_to_seconds = (hour * 60) * 60
    all = minute_to_seconds + hours_to_seconds + second
    hours = all // 10000
    remainder = all % 10000
    minutes = remainder // 100
    seconds = remainder % 100
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

def get_decimal_date(month,date_of_month,common_era_year):
    if month == 1:
        months = "Nivôse"
    elif month == 2:
        months = "Pluviôse"
    elif month == 3:
        months = "Ventôse"
    elif month == 4:
        months = "Germinal"
    elif month == 5:
        months = "Floréal"
    elif month == 6:
        months = "Prairial"
    elif month == 7:
        months = "Messidor"
    elif month == 8:
        months = "Thermidor"
    elif month == 9:
        months = "Fructidor"
    elif month == 10:
        months = "Vendémiaire"
    elif month == 11:
        months = "Brumaire"
    else:
        months = "Frimaire"
    revolutionary_year = common_era_year - 1792
    decade = 0
    if date_of_month >= 1 and date_of_month <= 10:
        decade = 1
    elif date_of_month >= 10 and date_of_month <= 20:
        decade = 2
    else:
        decade = 3
    return str(date_of_month) + " " + months + " Year " + str(revolutionary_year) + ", Décade " + str(decade)

def get_french_datetime(gregorian_date):
    find_hours = gregorian_date.find(":")
    find_minutes = gregorian_date.find(":", find_hours + 1)
    find_seconds = gregorian_date.find(" ", find_minutes + 1)
    found_hours = int(gregorian_date[0:find_hours])
    found_minutes = int(gregorian_date[find_hours + 1: find_minutes])
    found_seconds = int(gregorian_date[find_minutes + 1: find_seconds])
    find_month = gregorian_date.find("/")
    find_day = gregorian_date.find("/", find_month + 1)
    found_month = int(gregorian_date[8: find_month])
    found_day = int(gregorian_date[find_month + 1: find_day])
    found_year = int(gregorian_date[find_day + 1::])

    french_time = get_decimal_time(found_hours, found_minutes, found_seconds)
    french_date = get_decimal_date(found_month, found_day, found_year)
    return french_time + "\n" + french_date

def main():
    print(get_french_datetime("16:07:46 03/22/2022"))
    print(get_french_datetime("02:50:20 2/12/2022"))

main()



