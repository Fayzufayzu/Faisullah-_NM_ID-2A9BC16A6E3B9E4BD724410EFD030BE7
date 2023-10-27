year = 2823

#To get year (integer input) from the user

#year int(input("Enter a year: "))

# divided by 18e beans century year fending with (8)

# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
  print("{0} is a leap year".format(year))

#not divided by 100 means ma century year

#year divided by 4 is lead year

elif (year % 4== 0) and (year % 100 != 0): 
  print("{0} is a leap year".format(year))

# if at divided by both 409 (century year) and 4 [not century year)

#year is not leap year

else:

  print("{0} is not a leap year".format(year))