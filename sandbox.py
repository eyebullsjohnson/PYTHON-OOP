# print("class types")
# list=[1,2,3,4,5,6,6]
# print("this [] is a " + str(type(list)))
# Normal_Tuple=(1,2,3,4,5,6,6)
# print("this () is a " + str(type(Normal_Tuple)))
# set={1,2,3,4,5,6,6}
# print("this {} is a " + str(type(set)))
# tuple=1,2,3,4,5,6,6
# print("without any brackets it is a " + str(type(tuple)))

# ##the Str() converts to string, we are printing strings without this it is a 'type'. items in print have to be the same. 
# print(type(type(list)))


# print(list.count(6)) #how many sixes?
# print(len(set)) #len gives the number of unique elements if a set, because it s a set like math
# print(len(list)) #here it gives the numer of items because it is a list
# print(len(tuple)) #here is also just the total items


# print("----------IF STATEMENTS----------")
# ##if statements need == instead of =, and need to be punctuated with : to end it.
# Comprehension_check= input("entiendiste? ") 
# if Comprehension_check == "si":        ##SEEEEEEE it has a : and a ==
#     print("congrats!")
# elif Comprehension_check == (("no hablo") or ("no hablo espanol") or ("yes")):     ##you can use boolean operators, but this line has issues.  perserved as an example. see the fix in the while loop.
#     print("por que no usas si o no? no es dificil. entiendiste es DO YOU UNDERSTAND.")

# elif Comprehension_check == ("no"):
#     print("THEN READ IT AGAIN pls ^_^")
# else:        ##notice it is else:, not else.this is becuase it is an inequality, so broadly saying if anything else then..
#     print("AY that is a yes or no question")

# print("")
# print("---once more, this time its a while loop, fancy!)----")
# print("")
# ##if we want it to loop we can use a while loop

# #######
# while True: #while it is true a = b, do c. also True is case sensitive.
#     Comprehension_check = input("entiendiste ahora? ")  #why is this = and not ==, who knows. 

#     if Comprehension_check == "si":   
#         print("Good job")
#         break #breaks the loop, handy. without this it will loop forever. 
#     elif Comprehension_check in ["no hablo", "no hablo espanol", "yes"]: # see the fix? if comprehension_check input is in the list then... COOL. credit to CHATGPT
#         print("por que no usas si o no? no es dificil. entiendiste es DO YOU UNDERSTAND. USE SPANISH")
#     elif Comprehension_check == ("no"):
#         print("Imma loop until you do bud")
#     else:       
#         print("this is a yes or no question you got it right the first time dude come on")
# #########


##LETS DO FUNCTIONS BABYYYYYYYYYYYYYYYYY
###collatz fun
# print("first we will print the sequence of a given number to an chosen number of iterations")
# def collatzFX(chosen_number, iterations): #inputs defined in parens, notice the :
#     '''
#     A comment like this is good practice, these are called docstrings. describe functions here
#     '''
#     sequence = [chosen_number]
#     for something in range(iterations) : # 'something' could be anything, it gets declared here. it is literally something in the range. it is a temporary variable.  It's just a placeholder variable used because Python requires a variable to iterate over when using a for loop. 
#         if chosen_number % 2 == 0:
#             chosen_number = chosen_number//2 ## // is floor division, / will return a float
#         else:
#             chosen_number = 3*chosen_number+1
#         sequence.append(chosen_number)
#     return sequence

# number = int(input("Enter the number to compute: "))
# num_iterations = int(input("Enter the number of iterations: "))

# result = collatzFX(number, num_iterations) 
# #Notice that 'num_iterations' is pointing to 'iterations' in the function, so when we input 'num_iterations' it becomes th value for "iterations". and that becomes a range
# # the range in the for loop now is the value we put in for num iterations. COOOLL
# print("Collatz sequence:", result)

# #now iterate until 1
# print("now we iterate until one and print the sequence")
# '''
# loops the number and updates it, each lop appends a new number to the sequence
# '''
# def collatz_While_loop(chosen_number):
#     sequence = [chosen_number] # creates a list, only contains (and starts at), [chosen number]. we append to this list everytime the loop runs
#     while chosen_number != 1: # != does not equal, this says "while this is the case do this, and when it is not- stop" -in this case it is while it is not. like while is (is not true) is true. 
#         if chosen_number % 2 == 0:
#             chosen_number = chosen_number // 2
#         else:
#             chosen_number = 3 * chosen_number + 1
#         sequence.append(chosen_number) # this is an action, it appends the reult to our sequence. our sequence, declared above, already starts at [chosen number] 
#     return sequence #says im done with this and will us

# number = int(input("Enter the number to compute: "))

# result = collatz_While_loop(number)
# print("Collatz sequence:", result)

#now for loop again, but only return the end value
# print("(test) now lets return only the value of some number after n iterations, no list!")

# def collatz_single_output(chosen_number,iterations):
#     for n in range(iterations): #pointed to from below
#         if chosen_number % 2 == 0:
#             chosen_number = chosen_number// 2
#         else:
#             chosen_number = 3* chosen_number + 1
#     return chosen_number


# starting_num=int(input("start with which number?"))
# num_iterations = int(input("For how many times?")) #referenced in the function below, points to iterations. 
# print(collatz_single_output(starting_num , num_iterations) ) # the result and print result felt cumbersome, i can read this fine.

##if i were to just type into the program itelf to calculate, change num and range. python as a calcualtor. 
# num = 5
# for n in range(60):
#     if num % 2 == 0:
#             num = num// 2
#     else:
#             num = 3* num + 1
# print(num)


##Dictionaries using characters


# #####
# #imagine one person
# Max_Data = {"name":"Max","age":30,"gender": "male"} #makes the dictionary, keys and values. note the curly brackets, note the : #
# print(type(Max_Data))
# print(Max_Data) #print the whole thing
# print(Max_Data["age"]) #pick a piece

# #modify it
# Max_Data["age"] = 31 
# print(Max_Data["age"])

# #add stuff
# Max_Data["new thing"] = "taught Archery"
# print(Max_Data)

# #remove stuff
# del Max_Data["new thing"]
# print(Max_Data)

# #also they have methods!
# print(Max_Data.values())
# #####

#you can use nested dictionaries for say, multiple people. a dictionary of dictionaries

# people_data_DD = {
#     "John": {"age": 30, "city": "New York"},
#     "Alice": {"age": 25, "city": "Los Angeles"},
#     "Bob": {"age": 35, "city": "Chicago"}
# }

# print(people_data_DD["John"]["age"])

# #Same, but as a list of dictionaries. 

# people_data_LD = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Alice", "age": 25, "city": "Los Angeles"},
#     {"name": "Bob", "age": 35, "city": "Chicago"}
# ]

# print(people_data_LD[1]["age"]) #will not work with a name, notice the index starting at 0. 

#one is a list and the other a dictionary, which you use depends on which functionality you want. lists are indexed, 




## COPY:   python3 sandbox.py