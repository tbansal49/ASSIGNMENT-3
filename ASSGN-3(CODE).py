#Assignment 3
#Name-->TANISH BANSAL
#SID-->21104079
#Deptt-->EE


#Question.1--------------------------------------------------------------

string=input("Enter the string: ")
checking_list = string.split(" ")  # we make a list to check whether user enter a singlr word or more than one word in string

if len(checking_list) == 1 :

#Now we make a list of letters of word entered by user

    letter_list = list(string.lower())        # We use lower() function here so that for example both "P" in Purple are considered as same
    d = {}                                    # empty dictionary

    for letter in letter_list:
        if letter in d:
            d[letter] = d[letter] + 1
        else:
            d[letter] = 1
    for key in d:
        print(f'The occurance of letter "{key}" is {d[key]} time')

else:

# here WE MAKE A NEW STRING SO THAT ALL WORDS OF STRING ARE OF SAME CASE LETTER (LOWER/UPPER)
# OTHERWISE FOR EXAMPLE :Ankit and ankit are considered as differnt by our program

    new_string=string.lower()
    word_list=new_string.split(" ")   # here we make a list of words of new string
    d1={}                              # empty dictionary

    for word in word_list:
        if word in d1:
            d1[word] +=1
        else:
            d1[word]=1
    for key in d1:
        print(f'The occurance of "{key}" is {d1[key]} times')





#Question>> 2 -----------------------------------------------------------------------

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# below we use a for loop of single iteration so that we can use "break" command ,otherwise our output given by code work as input and  code executed one more time


for i in range(1):
    if month in (1, 3, 5, 7, 8, 10):                     # because days in there month are equal
        if day > 31 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 30:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = month + 1
            print(f'The next date is {day}/{month}/{year}')
            break
    if month in (4, 6, 9, 11):                                 # because days in these month are equal
        if day > 30 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 29:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = month + 1
            print(f'The next date is {day}/{month}/{year}')
            break

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # HERE we check the condition of leap year
            if day == 28:
                day = day + 1
                print(f'The next date is {day}/{month}/{year}')

            elif day == 29:
                day = 1
                month = month + 1
                print(f'The next date is {day}/{month}/{year}')
                break
            else:
                print("Your entered date is invalid")

        else:
            if day > 28 or day < 0:
                print("This day cannot exist")
            elif 0 < day <= 27:
                day = day + 1
                print(f'The next date is {day}/{month}/{year}')
            else:
                day = 1
                month = month + 1
                print(f'The next date is {day}/{month}/{year}')
                break

    if month == 12:
        if day > 31 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 30:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = 1
            year = year + 1
            print(f'The next date is {day}/{month}/{year}')
            break

    if month > 12 or month < 0:
        print("Your entered month is invalid,Please enter a valid month")

#Question >> 3 --------------------------------------------------------------------------------------------------------------

number_of_element=int(input("how many number you want to enter>> "))

list1=[]                                           # empty list to store numbers entered by user


for i in range(number_of_element):
    n=float(input("enter the number >> "))         #Here we take input as float because it is not mentioned in question that we have to take only interger as input
    list1.append(n)

list2=[]                                           # Empty list to store square of number entered by user
for number in list1:
    new_number=number*number
    list2.append(new_number)

# now we use a inbuilt funtion zip(a,b) to extract  corresponding element of list "a" and list "b" in a tuple

required_output=list(zip(list1,list2))
print("output is",required_output)



#Question >> 4 -------------------------------------------------------------------------------------------------

grade_points = int(input("Please enter your grade point>> "))     # Taking input from user

if grade_points == 10:
    print("Your Grade is 'A+' and Excellent Performance")

elif grade_points == 9:
    print("Your Grade is 'A' and Excellent Performance")

elif grade_points == 8:
    print("Your Grade is 'B+' and Excellent Performance")

elif grade_points == 7:
    print("Your Grade is 'B' and Excellent Performance")

elif grade_points == 6:
    print("Your Grade is 'C+' and Excellent Performance")

elif grade_points == 5:
    print("Your Grade is 'C' and Excellent Performance")

elif grade_points == 4:
    print("Your Grade is 'D' and Excellent Performance")

else:
    print("Error")



#Question >> 5 ------------------------------------------------------------------------------------------------------


letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for i in range(11):
    output =""                # empty string

    for letter in range(11 - 2 * i):
        output += letters[letter]
    k=" "                      # we make this 'k' so that we give a Tab(white space) after each iteration of outer loop to get required output
    print(k * i + output)

# Question >> 6 -----------------------------------------------------------------------------------------------------

dictionary ={}   # empty dictionary to store data entered by user

while True:
    user_choice = input("Enter 'Y' if you want to enter more data ,else enter 'N' >>> ")


    if user_choice.upper() == 'N':
        break
    if user_choice.upper() == 'Y':
        name = input("Enter your name :")
        sid = int(input("Enter your sid : "))
        dictionary[sid] = name
    else:
        print("Your enter  invalid choice,Please enter valid choice")   # case when user enter his choice other than 'Y'  and 'N'

# part (a)--------
print("part (a)")
print(dictionary)

#part (b)---------

print("part (b)")
print({i:j for i,j in sorted(dictionary.items(), key = lambda a:a[1])})   # here we sort the dictionary by name using inbuilt lambda function

#part (c)---------

print("Part (c)")
print({i:j for i,j in sorted(dictionary.items())})   # here we sort the dictionary sid-wise

#part (D) ---------
print("part(d)")
sid=int(input("Please enter a sid which you want to search>>"))
print("your searched student name is >>",dictionary[sid])




#question >> 7 ------------------------------------------------------------------------------------------------------

n=int(input("How many terms you want to print>>"))
if n<0:
    print("invalid input,please enter a positive number")
sum1=0                                                         # make to store sum of fibonnaci series of required terms
def fib(n):  # defined a function to print fibonacci series
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

for i in range(n):

    print(fib(i))
    sum1 += fib(i)

if n==0:                       # when your enter n=0 ,average is 0
    print(" average is 0")
else:
    print("the average of above series is ", sum1 / n)




#Question >> 8 -----------------------------------------------------------------------------------------------------------


set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

# part (a)####################
# in this part we have to make a set whose element are same as element in symmetric difference of set1 and set2
# to find this me use '^' operater to fulfil required condition

new_set= set1^set2
print("part (a)>>")
print(new_set)

# Part (b)#########################
# actually we have to  find symmetric of set1 ,set2 and set3 .so, we use  again '^' operator

set4=set3^set2^set1
print("Part (b)>>")
print(set4)

# part (c)#####################
# here we use '&' operator for intersection of two set at a time and use '|' operator for union of the whole  case

set5= set1&set2 | set2&set3 | set3&set1
print("Part (C)>>")
print(set5)

#Part (d)########################
# here we remove all element of set1 from our set formed in range 1 to 10

our_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set6 = our_set - set1
print("Part (D)>>")
print(set6)

# part (e)##########################
# here we remove all element which present in set1 and set2 and set3 from the our_set to get answer

set7 = our_set - set1 -set2 - set3
print("Part (E)>>")
print(set7)
