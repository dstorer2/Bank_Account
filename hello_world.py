# 1. TASK: print "Hello World"
# print("Hello World")

# 2. print "Hello David!" with the name in a variable
# name = "David"
# print( "Hello " + name )	# with a +
# print( "Hello", name )	# with a comma

# # 3. print "Hello 42!" with the number in a variable
# name = 42
# print("Hello", name)	# with a comma
# print( "Hello" + str(name))	# with a +	-- this one should give us an error!

# # 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
# print( "I love to eat", fave_food1.format(str), "and", fave_food2.format(str) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

