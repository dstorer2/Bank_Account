#1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#1, 1
# x[1][0] = 15
# print(x)

#1, 2
# students[0]['last_name'] = 'Bryant'
# print(students)

#1, 3
# print(sports_directory)
# sports_directory['soccer'][0] = 'Andres'

#1, 4
# z[0]['y'] = 30
# print(z)

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lst):
    for i in range(0, len(lst), 1):
        print(f"first_name - {lst[i]['first_name']}, last_name - {lst[i]['last_name']}")

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3
def iterateDictionary2(key_name, some_lst):
    for i in range(0, len(some_lst), 1):
        print(some_lst[i][key_name])

# iterateDictionary2('last_name', students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for i in range(0, len(dojo['locations'])):
        print(dojo['locations'][i])
    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for i in range(0, len(dojo['instructors'])):
        print(dojo['instructors'][i])

printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon