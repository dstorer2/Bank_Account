num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # variable declaration, Data-type - primative - boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, this is a list which is a composite data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # this is a Dictionary Data type
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # adding a value to a list
print(person['name']) # log statement
person['name'] = 'George' # change value of a dictionary item
person['eye_color'] = 'blue' # change value of a dictionary item
print(fruit[2]) # log statement

if num1 > 45: # if condition
    print("It's greater") # log statement
else: # else condition
    print("It's lower") # log statement

if len(string) < 5: # if condition
    print("It's a short word!") # log statement
elif len(string) > 15: # else if condition
    print("It's a long word!") # log statement
else:# else condition
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): #for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # while loop iterator

pizza_toppings.pop() # remove the last item from list
pizza_toppings.pop(1) # remove the second item from the list

print(person) # log statement
person.pop('eye_color') # remove type from dictionary
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # if condition
        continue # continue for loop
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if condition
        break # stop for loop

def print_hello_ten_times(): # function declaration
    for num in range(10): # for conditon
        print('Hello') # log statement

print_hello_ten_times() # call funtion

def print_hello_x_times(x): # function declaration with variable parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # call function with parameter 4

def print_hello_x_or_ten_times(x = 10): #  function declaration with variable declaration parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # call function with default parameter
print_hello_x_or_ten_times(4)# call function with parameter 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)