# CTI-110
# P3HW2 - Salary
# Alexander Jones 
# 12/01/22


# Program is designed to take the name. hours worked, and payrate of the employee than
# it will calculate how much money they emplyoee is owned for not only their regular
# pay but alos gross pay, gross pay is overtime pay + regular pay

base_hours = 40
xtra_hours = 60
over_time = 1.5
xover_time = 2.0

name = input("Enter the name of employee: ")
hours = float(input('Enter the amount of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

if (hours > base_hours) and (hours < 60):
    overtime_hours = hours - base_hours
    overtime_pay = overtime_hours * pay_rate * over_time
    gross_pay = base_hours * pay_rate + overtime_pay

elif hours > 60:
    overtime_hours = hours - base_hours 
    overtime_pay = overtime_hours * pay_rate * xover_time
    gross_pay = base_hours * pay_rate * overtime_pay

else:
    gross_pay = hours * pay_rate

print("------------------------------------")
print(f'{"Employee name: ":20s}' + name)
print("")
print(f'{"Hours Worked ":15s}{"Pay Rate ":12s}{"OverTime ":12s}{"OverTime Pay ":20s}{"RegHour Pay ":20s}' "Gross Pay")
print("----------------------------------------------------------------------------------------------")
print(hours , '         '  , pay_rate , '      ' , overtime_hours , '       ' , overtime_pay , '            ' , "${:,.2f}".format(base_hours*pay_rate) , '           ' , "${:,.2f}".format(gross_pay))
