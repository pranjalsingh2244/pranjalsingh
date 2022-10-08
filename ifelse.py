from re import X


x = 2
y = 3
""""""""""""""
if x>y:
    print("yayy")

else x>y:
    print("navy")

#take values off length nad breadth from user 
#print if it is square or not

length = (int(input("enter length")))
breadth = (int(input("enter breadth")))

if length==breadth:
    print("it is a square")
else:
    print("it is a square")












""""""""""""""""""""""""""""""""""""""




# A company decided to give bonus of rs 1000 to
#employee if his/her service is more than 5 years
#Ask user their salary and year of srvice and print 
#the net bonus amount

service = int(input("enter your year of service in this company"))
salary = int (input("enter your salary"))
if service > 5:
    print("your net worth in this company",salary+1000)
