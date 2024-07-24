# Day 6 of 30-Days-Of-Python

empty_tuple = ()
siblings = ('Brad', 'Sherri')
print(len(siblings))

parents = ('Jeff', 'Gail')
family_members = parents + siblings
print(family_members) # Combining parents and siblings to create one tuple

fruits = ('banana', 'apple', 'grape')
vegetables = ('potato', 'onion', 'lettuce')
animal_products = ('milk', 'eggs', 'butter')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

length = len(food_stuff_lt)
middle = len(food_stuff_lt) // 2
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]

print(middle)
print(first_three)
print(last_three)

del food_stuff_tp