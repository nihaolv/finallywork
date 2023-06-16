import math
import csv
#COMMENTS
#this is a one line comment

"""
this is
a multi
line comment
"""

#GETTING INPUT FROM THE USER
print("Enter a number:")
num =input() #num is variable
#what type is num?
print(type(num))
print("the number double is:",2 * num)

#we need to convert num from a string
#to a integer
num_int =int(num)
print("the number double is:",2 * num_int)

#CONDITIONALS (IF STATEMENTS)
#if some condition is truecode
#then execute some

x=10
if x ==5:
    print("x is 5")
elif x ==7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

#LOOPS
#use a loop when you want to repeat code
#we have for loops and while loops in python
#for item in sequence:
#      body of for loop (code you wantwrepeated)
for character in "python":
    print(character)

#we can also make our own sequences
#with range(start, stop, step)
for i in range(0,5,1):
    print(i)
for i in range(5):
    print(i)
for i in range(0,5):
    print(i)
for i in range(2,42,2):
    print(i,end=" ")
print()

##while loops
##while condition is true:
##body of loop (code to be repeated)
##progress towards the condition
##being false
##let's re-write our for loop
##with a while loop
i = 2
while i <= 40:
    print(i, end=" ")
    i += 2

def say_hello():
    print("hello")
for i in range(10):
    say_hello()
def say(message):
    print(message)
say("hi!!")
say("how are you??")
say("goodbye...")



def compute_cirle_area(radius):
    area = 3.14 * radius ** 2
    return area
result = compute_cirle_area(5)
print("result:",result)



list_ints = [10,4, -2,9,6]
print(list_ints)
print(list_ints[1],list_ints[-2])

list_ints[0] = 4000
print(list_ints)

list_ints[-1] = "nihao"
print(list_ints)

list_ints[-2] = "look"
print(list_ints)

print(len(list_ints))

list_ints.append(42)
print(len(list_ints))
##加数组

empty_list = [6,8,9]
print(len(empty_list))
##看数组有多少个内容

nested_list = [[0,1],[2,3],[],[8]]
print(nested_list)
print(nested_list[0])
print(nested_list[1][1])

foods = ["rice","noodle","beef"]
for food in foods:
    print(food)

i = 0
while i < len(foods):
    print("i:",i,"foods[i]:",foods[i])
    i += 1

print(foods)
foods += ["chicken","corn"]
print(foods)

repeated_list = 2 * ["fish","pig"]
print(repeated_list)

print(foods[1:3])

print(foods[:2])
print(foods[2:])

foods_copy = foods[:]
print("copy:",foods_copy)
foods_copy[0] = "nihao"
print("copy:",foods_copy)
print("original:",foods)

foods.append("new your food")
print(foods)
foods.remove("beef")
print(foods)

foods.pop(-1)
print(foods)

string_list = ["new","your","food"]
one_string = "***".join(string_list)
print(one_string)

comma_separated_value_string = "new-your-food"
sl2 = comma_separated_value_string.split("-")
print(sl2)

star_separated_value_string = "new***york***city"
sl3 = star_separated_value_string.split("***")
print(sl3)

filename = "data.csv"
infile = open(filename,"r")

reader = csv.reader(infile)
table = []
for row in reader:
    print(row)
    print(foods)
    table.append(row)
infile.close()

print("after closing file,table:")
print(table)



    














