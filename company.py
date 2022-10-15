#company will give bonus base on following criteria

#time spent in company     bonus
#   greater than 10 years      10%

#more than 6 and less 
#       than 10                        8%

#less than 6                           5%

#ask the salary and time spent from user
#print the net bonus amount accordingly

salary =int (input("what is yor salary"))
time =int (input("how much time have you spend on this company"))

if time<10:
    print("you are eligible for 10%of the bonus and your net amount will be" ,salary+(10/100)*salary)
elif time>6 and time <10:
    print( you have spent )