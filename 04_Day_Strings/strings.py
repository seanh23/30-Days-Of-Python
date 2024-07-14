# Day 4 of 30-Day-Of-Python

print('Thirty','Days', 'Of', 'Python')
print('Thirty' + ' Days' + ' Of' + ' Python') # Can do either way to get same results

company = "Coding For All"
print(company)
print(len(company)) # Checks how many characters in a string

print(company.upper()) # Makes all letters uppercase
print(company.lower()) # Makes all letters lowercase
print(company.capitalize()) # Capitalizes first letter in string
print(company.title()) # Capitalizes all like it's a title
print(company.swapcase()) # Converts lower case letters to upper, and uppercase letters to lower

first_word_slice = company[0:6]
print(first_word_slice) # This will print out only the first word 'Coding'

first_space_index = company.find(' ') # Finds the position of the first space in string
sliced_company = company[first_space_index + 1:] # Slices the string from the character after the first space
print(sliced_company) # Prints 'For All' and takes out 'Coding'

print(company.index('Coding')) # 0 - because Coding is first one and C is in 0 location
print(company.index('For')) # 7 - because For is second word and F is in 7 location index wise
print(company.index('All')) # 11 - because All is third word and A is in 11 location index wise

new_company = company.replace("Coding", "Python")
print(new_company)

newer_company = new_company.replace("All", "Everyone")
print(newer_company)

company_split = company.split(" ")
company2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_split2 = company2.split(', ')
print(company2) # Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon

print(company[0]) # C (First character)
print(company[-1]) # l (Last character)
print(company[10]) # space

print(company.rfind("i")) # 3

sentence = "You cannot end a sentence with because because because is a conjuction"
print(sentence.find('because', 1)) # 31 is where b in because starts, 1 is for the first because
print(sentence.rindex('because')) # 47

because = 'because because because' # Going to remove
start_index = sentence.find(because) # Starting index
end_index = start_index + len(because) # Calculates the ending index of because
new_sentence = sentence[:start_index] + sentence[end_index:] # Creates a new sentence excluding the phrase because because because
print(new_sentence)

variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"

# isIdentifier() method checks if a string is valid according to rules (must start with a letter or underscore)
print(variable1.isidentifier())  # False
print(variable2.isidentifier())  # True

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries) # joins the elements of the list into a single string, with each element separated by a hashtag
print(joined_libraries)

print("I am enjoying this challenge.\nI just wonder what is next.") # \n drops the second sentence to the line below

print("Name\tAge\tCountry\tCity\nSean\t29\tUSA\tPulaski") # \t tabs 8 spaces 

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with a radius {} is {}".format(radius, area)) # Formats and states the sentence with the given variables

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))     










