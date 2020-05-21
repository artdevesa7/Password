#keep going.py
#demonstrate loop with multiple exits

correct = "IndyPy"
tries = 0

keepGoing = True
while(keepGoing):

	tries = tries + 1
	print("try #",tries)

	guess = input("What is the password? ")
	if guess == correct:
		print("That's correct! here's the treasure!")
		keepGoing = False

	elif tries >= 3:
		print("Too many wrong tries. Launching the missiles")
		keepGoing = False

#we shouldn't use break statements