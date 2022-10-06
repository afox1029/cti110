# Program to calculate travel expenses
# 9/22/2022
# CTI-110 P1HW2 - Travel Expense
# Alexander Jones
#
#*********************Pseudocode*********************
#Display:"This program calculates and displays travel expenses "
#Display:"Enter Budget: "
#set budget = input budget
#Display:"Enter your travel destination: "
#set destination = input destination
#Display:"How far away are you to your destination in miles? "
#set distance = input distance
#Display:"How many miles to a gallon does your vehicle get? "
#set mph = input mph
#Display:"How much is gas to a gallon? "
#set gasPrice = input gasprice
#Display:"How much will you spend on your accomadations? "
#set accomodations = input accomodations
#Display:"How long will you be gone for? "
#set time = input time
#set food = time * 5
#set gas = 2(distance/mph) * gasPrice
#set expenses = gas + accomodations + food
#set remaining balence = calc budget - expenses
#Display:"----------Travel expenses----------"
#Display:"Location: location
#Display:"Initial Budget: budget
#Display:"Gas: gas
#Display:"Accomodation: accomodatons
#display:"Food: food
#display:"Remaining balence: remaining balence"
print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
distance = float(input("How far away are you to your destination in miles? "))
mph = float(input("How many miles to a gallon does your vehicle get? "))
gasPrice = float(input("How much is gas to a gallon? "))
accomodations = int(input("How much will you spend on your accomadations? "))
time = int(input("How long will you be gone for? "))
food = time * 5
gas = 2 * (distance / mph) * gasPrice
expenses = gas + accomodations + food
remBalence = budget - expenses
print("----------Travel expenses----------")
print("location: ", destination)
print("Initial Budget: $", budget)
print("Gas: $ ", round(gas, 2))
print("Accomodations: $", accomodations)
print("Food: $", food)
print("Remaining balence: $", round(remBalence, 2))
