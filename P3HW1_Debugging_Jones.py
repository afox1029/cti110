# CTI-110
# P3HW1 - Debugging
# Alexander Jones
# 12/01/22

# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# determine lowest, highest , sum and average for grades

grades_low = min(grades)
grades_high = max(grades)
grades_sum = sum(grades)
grades_avg = sum(grades)/len(grades) 

print("------------Results------------")
print(f'{"Lowest Grade: ":20s}{grades_low:.1f}')
print(f'{"Highest Grade: ":20s}{grades_high:.1f}')
print(f'{"Sum of Grades: ":20s}{grades_sum:.1f}')
print(f'{"Average: ":20s}{grades_avg:.2f}')
print("-------------------------------")

# determine letter grade for average

if grades_avg >= 90:
    print('Your grade is: A')
elif grades_avg >= 80:
    print('Your grade is: B')
elif grades_avg >= 70:
    print('Your grade is: c')
elif grades_avg >= 80:
    print('Your grade is: D')
else:
    print('Your grade is: F')
