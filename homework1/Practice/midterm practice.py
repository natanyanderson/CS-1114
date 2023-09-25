hours_worked = int(input("Enter the hours worked: "))
pay_rate = 10.275
save_hours_worked = 0
bonus = 0.0
overtime_pay = 0.0
while hours_worked > 0:
    if hours_worked > 10:
        bonus += 13.0
    save_hours_worked += hours_worked
    hours_worked = int(input("Enter the hours worked: "))
print("Bonus: $" + str(bonus))
if save_hours_worked > 40:
    overtime_extra_hours = save_hours_worked - 40
    overtime_pay = pay_rate * 1.5 * overtime_extra_hours
    print("Overtime pay: $" + str(round(overtime_pay, 2)))
else:
    print("Overtime pay: $" + str(overtime_pay))
total_pay = (pay_rate * save_hours_worked) + bonus + overtime_pay
print("Total pay: $" + str(round(total_pay, 2)))

