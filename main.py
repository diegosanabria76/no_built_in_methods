#c:\users\sanabrid\github\no_built_in_methods

from t import *

print("Welcome to my stats program!")
print("="*60)

stat = my_stats()
list = stat.user_input()
lista = list


print("="*60)

keep = 1

while keep != 0:

    keep = int(input("PLease enter:\n 1 for average, 2 for variance, 3 for standard deviation or 0 to quit."))

    if keep==1:
        mean = stat.mean(list)

        print("data entered : ", list)
        print("the mean of that data is : ", mean)
    elif keep == 2:
        variance = stat.variance(list)
        print("The Variance of your data is : ", variance)
    elif keep == 3:
        sd = stat.s_d(variance)
        print("The standard deviation is: \n",sd)

print("Thanks for using this program")
