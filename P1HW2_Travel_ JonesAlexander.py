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
#Display:"How much will you spend on gas? "
#set gas = input gas
#Display:"How much will you spend on your accomadations? "
#set accomodations = input accomodations
#Display:"How much will you spend on food? "
#set food = input food
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
gas = int(input("How much will you spend on gas? "))
accomodations = int(input("How much will you spend on your accomadations? "))
food = int(input("How much will you spend on food? "))
expenses = gas + accomodations + food
remBalence = budget - expenses
print("----------Travel expenses----------")
print("location: ", destination)
print("Initial Budget: ", budget)
print("Gas: ", gas)
print("Accomodations: ", accomodations)
print("Food: ", food)
print("Remaining balence: ", remBalence)

