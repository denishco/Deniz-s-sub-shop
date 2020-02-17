#Deniz Erdem COMP 1405 Assignment 2
#student number: 101161756

#NOTE TO MARKER: in this program all values for the sub sandwich are saved in an array
#By using this method it is very easy to create more than one sub and save all the values seperately
#Different funcitons were created for each step so that the customer can go back in any point in time and keep some informatoin and change other
#An example of this would be if the customer picked the wrong sub but the right toppings, to save time you do not have to re run the entire program and can rather just run the function that picks the type of sandwich
#Another reason why code that is devided into funcitons is optimal in this case is because it makes it all very organized and avoids larger quantities of code in one huge block


#import this library
import random


#functions to create an array that stores all the names of toppings
def namesOfToppings():
	toppings = ["tomatoes", "onions","peppers","jalepenos","pickles","cucumbers","olives","guacamole","lettuce"]
	return toppings

#Function that checks if input from is acceptable depending on the perameters given
def inputCheck(given, parameters):
	x=0
	while x < len(parameters):
		if given == parameters[x]:
			return
		else:
			x += 1
	print("The value you input is invalid")
	

#function that returns a different kind of responsive phrase each time
def responses():
	#recieving a random number
	num = random.randint(0,2)
	#an array with the different phrases
	responses = ["great choice", "sounds great", "that sounds so good"]
	#returning the phrase chosen
	return responses[num]

#function that returns a different kind of greeting each time
def greetings():
	#recieving a random number
	num = random.randint(0,5)
	#an array with the different greetings
	greetings = ["Hello", "Hi", "Greetings", "Salutations", "Good day", "Hey"]
	#returning the greetings
	return greetings[num]


#Function to print the different subs
def printSubs():
	#printed like so to keep code organized
	print(greetings(),"how are you?")
	print("Please select your sub:")
	print("1. ""Meat""-ball sub ($7.99)")
	print("2. Cold-cut Club sub ($8.25)")
	print("3. Philly's Cheese Mis-Steak sub ($9.55)")
	print("4. Veggie Pile sub ($6.75)")


#Function to print the different toppings
def printToppings ():
	#printed like so to keep code organized
	print("sounds good")
	print("Select your toppings.")
	print("Type any of the following toppings and press enter:")
	print("lettuce, tomatoes, onions, peppers, jalepenos, pickles, cucumbers, olives, or guacamole.")
	print("Please note: all toppings are free except guacamole costs an extra $1.50")
	print("Type ""done"" to stop.")


#Function that creates an array that will store different values in each place
def createSub ():
	#array that will store values
	sub = [0,0,0,0,0,0,0,0,0,0,0]
	#returning array
	return sub
	
#Recieving input from the user on what they would like as toppings in their sub
def askSub(sub):
	#defining the bool variable we will use to make sure the input is valid
	done = 0
	#while we are not done do the following
	while done == 0:
		print("which sub would you like?")
		sub[0] = input(">")
		#whole lotta if statements so that when the selection is picked 
		#that sub array will have that value storred in it
		if sub[0] == '1':
			sub[0] = "Meat-ball sub"
			sub[10] += 7.99
			#make done = 1 so that the program can continue
			done = 1
		elif sub[0] == '2':
			sub[0] = "Cold-cut Club sub"
			sub[10] += 8.25
			done = 1
		elif sub[0] == '3':
			sub[0] = "Philly's Cheese Mis-Steak sub"
			sub[10] += 9.55
			done = 1
		elif sub[0] == '4':
			sub[0] = "Veggie Pile sub"
			sub[10] += 6.75
			done = 1
		#if the input is invalid go through again
		else:
			print("sorry but that sub is not on our list")

#function that asks the user for toppings
def askToppings (sub):
	#inputs is our bool, we are waiting for it to be done to continue through the program
	inputs = "not done"
	#while the input is not done the go through this
	while inputs != "done":
		#whole lotta if statements so that when the selection is picked 
		#that sub array will have that value storred in it
		inputs = input(">")
		if inputs == "tomatoes":
			sub[1] += 1
		elif inputs == "onions":
			sub[2] += 1
		elif inputs == "peppers":
			sub[3] += 1
		elif inputs == "jalepenos":
			sub[4] += 1
		elif inputs == "pickles":
			sub[5] += 1
		elif inputs == "cucumbers":
			sub[6] += 1
		elif inputs == "olives":
			sub[7] += 1
		elif inputs == "guacamole":
			sub[8] += 1
			sub[10] += 1.50
		elif inputs == "lettuce":
			sub[9] += 1
		#if done print a response and leave the funciton while returning sub array
		elif inputs == "done":
			print(responses())
			return sub
		#if inputs is anything other than what we have in the if statements then print 
		#something and go through aagin
		else:
			print("sorry but",inputs,"is not on our list")

			#funciton to print the toppings on the sub; requires the array with the 
			#toppings selected and the array that stores the names of the toppings

#printing all the toppings
def printSubToppings (sub, toppingNames):
	#counter variable
	x = 1
	#while loop
	while x < 10:
		if sub[x] > 0:
			#print the amout of that topping that is requested and the name of the topping
			print(sub[x],"x",toppingNames[x-1])
		#counter go up by one
		x+=1

#at the end of the program check is thats the sub the user wanted
def checkCorrectSub():
	#validity boolean value 
	valid = 0
	#while false do this
	while valid == 0:
		#asking if its right
		correctSub = input("Is this correct? (y/n): ")
		#if not right then end program
		if correctSub =="n":
			print("Oh sorry for the confusion, hav a good day")
			exit()
		#if right, go back to main code
		elif correctSub =="y":
			return
		#if input is invalud then go though again
		else:
			print("please enter a valid input")
			


#Welcoming message
print("================================")
print("| Welcome to Deniz's Sub Shoppe! |")
print("================================")

#Running the functions required
toppingNames = namesOfToppings()
sub = createSub()
printSubs()
askSub(sub)
printToppings()
askToppings(sub)

#Printing Final message
print("Your order:")
print("Sub: " ,sub[0])
print("Toppings: ")
#Running the function that prints all the toppings in the order(order = sub array)
printSubToppings(sub, toppingNames)
#running the function that checks if the sub the user picked is what they want 
checkCorrectSub()


#math to calculate tax and the total
tax = round(sub[10] * 0.13, 2)
total = round(sub[10] + tax,2)

#printing final costs and a goodbye message
print("================================")
print("Subtotal:               $",sub[10])
print("Tax:                    $",tax)
print("================================")
print("Total:                  $",total)
print("Thanks for shopping and stuff! have a good one")
