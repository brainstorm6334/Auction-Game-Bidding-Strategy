from __future__ import print_function
# Echo client program
import socket
import random
import time
import os
import platform


HOST = '10.225.26.226'    # Change this to your own IP if you want to try running it

# to act as a client
PORT = 50018              # The server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# APPLICATION

partnerid = -1 # no partner
numberbidders = 0 # will be given by server
artists = ['Picasso', 'Rembrandt', 'Van_Gogh', 'Da_Vinci']

# DO SOMETHING HERE
# you need to change this to do something much more clever
def determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, artists, standings, rd):

# A:search list of paintings, find the one that comes up 4 times first. Bid 34, 36, everything, everything for it. If u dont get 1st, continue.
# B:Meanwhile, bid 2 for eveything else, if u get 1 of them, bid 6 for the same kind

# C:If you dont get the first two from A, bid 11 for everything, then if u get somethng, bid 21 for it, if 2 obtained, bid everything 3rd time. 
# D:Meanwhile, continue bidding 11 for eveything if u only have 1, if u get two, stop bidding for evetything. 

	global moneyleft, mybidderid
	our_name = str(mybidderid)

#_______________________________________________________________________
	if numberbidders >=5:

		pc = 0
		rb = 0
		vg = 0
		dv = 0
		targetPaintings = " "
		bid = 0
		counter = 0
		for item in itemsinauction:

			if item == "Rembrandt":
				rb +=1
				if rb == 4:
					targetPaintings = "Rembrandt"
					break
			elif item == "Picasso":
				pc +=1
				if pc == 4:
					targetPaintings = "Picasso"
					break
			elif item == "Van_Gogh":
				vg +=1
				if vg == 4:
					targetPaintings = "Van_Gogh"
					break
			elif item == "Da_Vinci":
				dv +=1
				if dv == 4:
					targetPaintings = "Da_Vinci"
					break

		# print(itemsinauction)
		# print()
		# print(targetPaintings)

		if itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==0 and counter<2:
			bid = 34
			if moneyleft < 35:
				bid = moneyleft//2
			counter +=1
		elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==1 and counter<3:
			bid = 36
			counter +=1
			if moneyleft < 37:
				bid = moneyleft//2
		elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==2:
			bid = moneyleft
			counter +=1
		else:
			bid = 4

		if standings[our_name][targetPaintings]<2 and counter>3:
			bid = 11	
			if moneyleft < bid:
				bid = moneyleft//2	
		elif standings[our_name][itemsinauction[rd]]== 1 and counter>2:
			bid = 28
			if moneyleft < bid:
				bid = moneyleft//2
		elif standings[our_name][itemsinauction[rd]]==2:
			bid = moneyleft


		if moneyleft <= 5:
			bid = 1
#_____________________________________________________________________

#_______________________________________________________________________
	elif numberbidders == 4:

		bid = 0
		for name in players:
			flag = False	
			if standings[name][itemsinauction[rd]]==2:
				for n in players:
					if standings[n]['money'] > standings[name]['money']:
						flag = True
						break
				if flag == False and bid < standings[name]['money']+1:
					bid = standings[name]['money']+1

				if bid > moneyleft:
					bid = 0


					
		if bid==0:

			pc = 0
			rb = 0
			vg = 0
			dv = 0
			targetPaintings = " "
			bid = 0
			counter = 0
			for item in itemsinauction:

				if item == "Rembrandt":
					rb +=1
					if rb == 4:
						targetPaintings = "Rembrandt"
						break
				elif item == "Picasso":
					pc +=1
					if pc == 4:
						targetPaintings = "Picasso"
						break
				elif item == "Van_Gogh":
					vg +=1
					if vg == 4:
						targetPaintings = "Van_Gogh"
						break
				elif item == "Da_Vinci":
					dv +=1
					if dv == 4:
						targetPaintings = "Da_Vinci"
						break

			# print(itemsinauction)
			# print()
			# print(targetPaintings)

			if itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==0 and counter<2:
				bid = 34
				if moneyleft < 35:
					bid = moneyleft//2
				counter +=1
			elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==1 and counter<3:
				bid = 36
				counter +=1
				if moneyleft < 37:
					bid = moneyleft//2
			elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==2:
				bid = moneyleft
				counter +=1
			else:
				bid = 4

			if standings[our_name][targetPaintings]<2 and counter>3:
				bid = 11	
				if moneyleft < bid:
					bid = moneyleft//2	
			elif standings[our_name][itemsinauction[rd]]== 1 and counter>2:
				bid = 28
				if moneyleft < bid:
					bid = moneyleft//2
			elif standings[our_name][itemsinauction[rd]]==2:
				bid = moneyleft


			if moneyleft <= 5:
				bid = 1
#_____________________________________________________________________

	elif numberbidders <= 3:

		bid = 0
		for name in players:
			if standings[name][itemsinauction[rd]]==2 and name != mybidderid and bid < standings[name]['money']+1:
				bid = standings[name]['money']+1
			if bid > moneyleft:
				bid = 0



		if bid==0:

			pc = 0
			rb = 0
			vg = 0
			dv = 0
			targetPaintings = " "
			bid = 0
			counter = 0
			for item in itemsinauction:

				if item == "Rembrandt":
					rb +=1
					if rb == 4:
						targetPaintings = "Rembrandt"
						break
				elif item == "Picasso":
					pc +=1
					if pc == 4:
						targetPaintings = "Picasso"
						break
				elif item == "Van_Gogh":
					vg +=1
					if vg == 4:
						targetPaintings = "Van_Gogh"
						break
				elif item == "Da_Vinci":
					dv +=1
					if dv == 4:
						targetPaintings = "Da_Vinci"
						break

			# print(itemsinauction)
			# print()
			# print(targetPaintings)

			if itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==0 and counter<2:
				bid = 34
				if moneyleft < 35:
					bid = moneyleft//2
				counter +=1
			elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==1 and counter<3:
				bid = 36
				counter +=1
				if moneyleft < 37:
					bid = moneyleft//2
			elif itemsinauction[rd] == targetPaintings and standings[our_name][targetPaintings]==2:
				bid = moneyleft
				counter +=1
			else:
				bid = 4

			if standings[our_name][targetPaintings]<2 and counter>3:
				bid = 11	
				if moneyleft < bid:
					bid = moneyleft//2	
			elif standings[our_name][itemsinauction[rd]]== 1 and counter>2:
				bid = 28
				if moneyleft < bid:
					bid = moneyleft//2
			elif standings[our_name][itemsinauction[rd]]==2:
				bid = moneyleft


			if moneyleft <= 5:
				bid = 1

	# print(bid)
#_____________________________________________________________________



	# '''

	# itemsinauction is a list where at index "rd" the item in that round is being sold is displayed.

	# winnerarray is a list where at index "rd" the winner of the item sold in that round is displayed.

	# winneramount is a list where at index "rd" the amount of money paid for the item sold in that round is displayed.

	# example: I will now construct a sentence that would be correct if you substituted the outputs of the lists:
	# In round 5 winnerarray[4] bought itemsinauction[4] for winneramount[4] dirhams/dollars/money unit.

	# numberbidders is an integer displaying the amount of people playing the auction game.

	# players is a list containing all the names of the current players.

	# artists is a list containing all the names of the artists (paintings) that are for sale in our auction.

	# standings is a set of nested dictionaries (standings is a dictionary that for each person has another dictionary
	# associated with them). standings[name][artist] will return how many paintings "artist" the player "name" currently has
	# standings[name]['money'] (remember quotes for string, important!) returns how much money the player "name" has left.

	# rd is the current round in 0 based indexing.

	# Good luck!
	# '''
	return int(bid)


# DATA

mybidderid = raw_input("Input team / player name : ").strip()  # this is the only thing that distinguishes the clients 
while len(mybidderid) == 0 or ' ' in mybidderid:
	mybidderid = raw_input("You input an empty string or included a space in your name which is not allowed (_ or / are all allowed)\n for example Emil_And_Nischal is okay\nInput team / player name: ").strip()

moneyleft = 100 # should change over time
winnerarray = [] # who won each round
winneramount = [] # how much they paid

itemsinauction = []
myTypes = {'Picasso': 0, 'Rembrandt': 0, 'Van_Gogh': 0, 'Da_Vinci': 0, 'money': moneyleft}

# EXECUTION

# get list of items and types
getlistflag = 1
s.send(str(mybidderid))
while(getlistflag == 1):
	# print "Have sent data from ", str(mybidderid)
	data = s.recv(5024)
	x = data.split(" ")
	# print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
	if(x[0] != "Not" and len(data) != 0):
		getlistflag = 0
		numberbidders = int(x[0])
		itemsinauction = x[1:]
	else:
		time.sleep(2)

while True:
	s.send(str(mybidderid) + ' ')
	data = s.recv(5024)
	x = data.split(" ")
	if (x[0] == 'wait'):
		continue
	players = []
	for player in range(1, numberbidders + 1):
		players.append(x[player])
	break
standings = {name: {'Picasso': 0, 'Van_Gogh': 0, 'Rembrandt': 0, 'Da_Vinci': 0, 'money': 100} for name in players}
# now do bids
continueflag = 1
j = 0
while(continueflag == 1):
	#roundStart = time.time()
	print(random.choice(["I'm doing my best, okay?", "Why aren't you cheering louder?", "Aren't you proud of me?", "Damn I'm good, and I don't even have a brain!", "And do you think you could do any better?", "I feel like it's me doing all the work, you're just chilling in your chair", "If I lose this it's your fault not mine... I'm doing EXACTLY what you told me to do!"]))
	print()
	bidflag = 1
	bid = determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, artists, standings, len(winnerarray))
	time.sleep(0.02)
	s.send(str(mybidderid) + " " + str(bid))
	while(bidflag == 1):
		# print "Have sent data from ", str(mybidderid)
		data = s.recv(5024)
		x = data.split(" ")
		# print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
		if(x[0] != "Not"):
			bidflag = 0
		else:
			print("exception")
			time.sleep(2)


	resultflag = 1
	while(resultflag == 1):
		s.send(str(mybidderid))
		# print "Have sent data from ", str(mybidderid)
		data = s.recv(5024)
		x = data.split(" ")
		if (x[0] == 'wait'):
			continue
		# print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
		if len(x) >= 7 and x[7] == 'won.':
			time.sleep(4.5)
			continueflag = 0
			resultflag = 0
			print(data)
			print()
			print('game over')
		if(x[0] != "ready") and (continueflag == 1):
			#roundLength = time.time()-roundStart
			#time.sleep(max(0, 5-roundLength))
			resultflag = 0
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')
			# print x
			winnerarray.append(x[0])
			winneramount.append(int(x[5]))
			standings[x[0]]['money'] -= int(x[5])
			standings[x[0]][x[3]] += 1
			if (x[0] == mybidderid):
				moneyleft -= int(x[5])
				myTypes[itemsinauction[j]] += 1
			# update moneyleft, winnerarray
		else:
			time.sleep(2)
	j+= 1
