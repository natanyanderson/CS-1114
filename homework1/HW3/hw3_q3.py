"""
Author: [Natanya Anderson]
Assignment / Part: HW3 - Q3 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
#5am-9pm mon-thurs is $0.55/min
#before 5am or after 9pm mon-thurs is $0.35/min
#Fri-Sat_Sun is $0.10/min


day = input("Enter the day the call started at: ")
times = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))
billing_rate = 0.0
do_calculation = True

if not (day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr" or day == "Fri" or day == "Sat" or day == "Sun"):
    print("Enter the proper three letter abbreviation (Mon,Tue,Wed)")
    do_calculation = False
elif day == "Fri" or day == "Sat" or day == "Sun":
    billing_rate = 0.10
elif day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr":
    if times >= 500 and times <= 2100:
        billing_rate = 0.55
    elif times < 500 or times > 2100:
        billing_rate = 0.35
if duration < 0:
    print("Duration can only be positive")
    do_calculation = False
if do_calculation == True:
    calulation_one = billing_rate*duration
    calulation_one_rounded = round(calulation_one, 2)
    answer = "This call will cost $" + str(calulation_one_rounded)
    print(answer)