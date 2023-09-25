# Ask input for day, time, and duration
# Any call between 500 and 2100, mon and thurs, = 0.55/min
# Any call before 500 or after 2100, mon and thurs, = 0.35/min
# Fri Sat Sun = 0.10
# Input for days must be Mon-Tue_Wed_Thurs etc

day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))
billing_rate = 0.0
do_calculation = True

if not (day == "Mon" or "Tue" or "Wed" or "Thr" or "Fri" or "Sat" or "Sun"):
    print("Enter the correct three letter abbreviation (Mon, Tue, Wed, Thr, Fri, Sat, Sun)")
    do_calculation = False
elif day == "Fri" or "Sat" or "Sun":
    billing_rate = 0.10
elif day == "Mon" or "Tue" or "Wed" or "Thr":
    if day >= 500 and day <= 2100:
        billing_rate = 0.55
    elif day < 500 and day > 2100:
        billing_rate = 0.35

if duration < 0:
    print("Enter a number above 0")
    do_calculation == False
if do_calculation == True:
    calculation_1 = billing_rate*duration
    calculation_one_rounded = round(calculation_1, 2)
    print("The total would be " + str(calculation_one_rounded))