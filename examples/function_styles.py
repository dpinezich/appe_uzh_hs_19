# Case: function without a positional argument
def calc(number1, number2):
    sum = number1 + number2
    print(sum)

calc(1, 4) # the 1 will be number1 and 4 will be number2
print('***************')



# Case 2: function with a positional argument in the caller
def special_function(number1, number2):
    print(number1 + number2)

# function call with a positional argument
special_function(number2=2000, number1=10000)
print('***************')


# Case 3: function with a default name
def country_function(country = "Norway"):
  print("I am from " + country)

country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")
print('***************')







