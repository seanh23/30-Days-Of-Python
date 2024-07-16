# Day 5 of 30-Days-Of-Python
# A list is a collection of different data types which is ordered and modifiable
# Can use list() or []

fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits: ', fruits)
print('Number of Fruits: ', len(fruits))
first_fruit = fruits[0]
print(first_fruit) # Prints banana

list = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# .append() to add an item to a list
# .sort() to sort alphabetical or numerical, .sort(reverse=True) if want to sort opposite way

empty_list = [] # Empty list
sports_list = ['baseball', 'football', 'basketball', 'soccer', 'hockey', 'golf']
print(len(sports_list)) # 6

length_of_list = len(sports_list)
first_item = sports_list[0]
middle_item = sports_list[length_of_list // 2]
last_item = sports_list[-1]

print(first_item) # baseball
print(middle_item) # soccer
print(last_item) # golf

mixed_data_types = ['Sean', 29]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
length_of_companies = len(it_companies)
print(length_of_companies)
first_company = it_companies[0]
middle_company = it_companies[length_of_companies // 2]
last_company = it_companies[-1]
print(first_company) # Facebook
print(middle_company) # Apple
print(last_company) # Amazon

it_companies[0] = 'Meta' # Modified first company in list from Facebook to Meta
print(it_companies)
it_companies.append('Anthropic') # Adding company to end of the list
print(it_companies)
it_companies.insert(3, 'Nvidia') # Adding Nvidia into index 3 in list
print(it_companies)
convertied_list = it_companies[3].lower() # Nvidia is now nvidia
print(convertied_list) 

joined_companies = '#; '.join(it_companies)
print(joined_companies)

if 'Apple' in it_companies:        # Checks if company, Apple, is in list
    print("Exists")
else:
    print('Does not Exist')

it_companies.sort() # Sorting in alphabetical order
print(it_companies)

it_companies.reverse()
print(it_companies)

first_three = it_companies[0:3]
last_three = it_companies[-3:]
middle_company2 = it_companies[length_of_companies // 2]

print(first_three)
print(last_three)
print(middle_company2)

del it_companies[0] # Removes the first item Oracle off of list
print(it_companies)

del it_companies[length_of_companies // 2] # Removes IBM
del it_companies[-1] # Removes Amazon
print(it_companies)

del it_companies[0:] # Removes all companies
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_stacks = front_end + back_end # Joining front end and back end
print(joined_stacks)

full_stack = joined_stacks.copy() # Copying joined_stacks variable and making it into full_stack variable then adding two
full_stack.insert(5, 'Python') # Placing Python after Redux
full_stack.insert(6, 'SQL') # Placing SQL after Python
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)
ages.append(19) # adding min again
ages.append(26) # adding max again
ages.sort() # have to re-sort
print(ages)
length_of_age = len(ages)
median_age = ages[length_of_age // 2]
print(median_age)

average_age = sum(ages) / len(ages)
print(average_age) # 22.75

range_of_ages = max(ages) - min(ages)
print(range_of_ages) 

min_avg_diff = min_age - average_age
max_avg_diff = max_age - average_age

abs_min_avg_diff = abs(min_avg_diff)
abs_max_avg_diff = abs(max_avg_diff)

print(abs_min_avg_diff)
print(abs_max_avg_diff)
