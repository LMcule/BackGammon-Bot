#!/usr/bin/env python 
import sys

#Priority (set yourself)
my_blots_w=-100
enemy_bar_w=600
my_bar_w=-250
stronghold_w=150
anchor_w=150
primes_w=350

#Check validity of a move. Basic index checking.
def valid(a,ini,fin):
	if a[ini]>0 and a[fin]>=-1:
		return 1
	return 0


#Function to give all possible moves.	
def all_moves(state,d1,d2,b):
#move1 stores all first moves. move2 stores all second moves.
		move1=[]
		move2=[]
	
		for i in range(0,24):
			if valid(state,i,i+d1):
				state1=state[:]
				state1[i]-=1
				if state1[i+d1]==-1:
					state1[i+d1]+=2
				else:
					state1[i+d1]+=1
				for j in range(0,24):
					if valid(state1,j,j+d2):
						move1.append([i,i+d1])
						move2.append([j,j+d2])

		for i in range(0,24):
			if valid(state,i,i+d2):
				state1=state[:]
				state1[i]-=1
				if state1[i+d2]==-1:
					state1[i+d2]+=2
				else:
					state1[i+d2]+=1
				for j in range(0,24):
					if valid(state1,j,j+d1):
						move1.append([i,i+d2])
						move2.append([j,j+d1])

		move=[]
		move.append(move1)
		move.append(move2)
		return move
		

				
# Bearing Off Funtion
def bearingOff(state,d1,d2,b):
	normal=0
	global stronghold_w
	global primes_w
	global my_blots_w
	enemy=0
	total_enemy=0
	main_move=[]
	pass_flag=0
	for i in range(18,24):
		if state[i]<0:
			enemy=1
			total_enemy+=state[i]
	if total_enemy==-1:
		for i in range(18,24):

			if i+d1<54 and d1!=0 and state[i+d1]==-1:
				main_move.append([i,i+d1])
				state[i]-=1
				state[i+d1]+=2
				d1=0
			elif i+d2<54 and d2!=0 and state[i+d2]==-1:
				main_move.append([i,i+d1])
				main_move.append([i,i+d2])
				state[i]-=1
				state[i+d2]+=2
				d2=0
			elif i+d1+d2<54 and d1!=0 and d2!=0 and  state[i+d1+d2]==-1 and valid(state,i,i+d1):
				main_move.append([i,i+d1])
				main_move.append([i+d1,i+d1+d2])
				d1=0
				d2=0
			elif i+d1+d2<54 and d1!=0 and d2!=0 and state[i+d2+d1]==-1 and valid(state,i,i+d2):
				main_move.append([i,i+d2])
				main_move.append([i+d2,i+d2+d1])
				d1=0
				d2=0
		for i in range(18,24):
			if d2==0 and d1!=0:
				if i+d1<=24 and state[i]>0:
					main_move.append([i,i+d1])
					d1=0
					break
			if d1==0 and d2!=0:
				if i+d2<=24 and state[i]>0:
					main_move.append([i,i+d2])
					d2=0
					break

	elif total_enemy<-1 or b[1]>0:
			uti=[]
			stronghold_w=350
			my_blots_w=-300
			primes_w=550
			b=[]
			b.append(0)
			b.append(0)
			alice=all_moves(state,d1,d2,b)
			for i in range(0,len(alice[0])):
				state1=state[:]
				#for each move, change the state of the board.
				state1[alice[0][i][0]]-=1
					
				if state1[alice[0][i][1]]==-1:
					state1[alice[0][i][1]]+=2
				else:
					state1[alice[0][i][1]]+=1
		
				state1[alice[1][i][0]]-=1
				if state1[alice[1][i][1]]==-1:
					state1[alice[1][i][1]]+=2
				else:
					state1[alice[1][i][1]]+=1
				b1=[]
				b1.append(0)
				b1.append(0)
				uti.append(utility(state1,b1))
			if len(uti)==0:
				work=0
				for i in range(18,24):
					if state[i]>0 and state[i+d1]>=-1 and d1!=0:
						main_move.append([i,i+d1])
						d1=0
						work+=1
					if state[i]>0 and state[i+d2]>=-1 and d2!=0:
						main_move.append([i,i+d2])
						d2=0
						work+=1
				if work==1:
					if main_move[0][1]>23:
						main_move[0][1]="pass"
					else:
					   	main_move[0][1]+=1
					print main_move[0][0]+1 , main_move[0][1]
					print "pass"
					pass_flag=1

				elif work==0:
					print "pass"
					pass_flag=1
			else:
				ans=uti.index(max(uti))
				main_move.append([alice[0][ans][0],alice[0][ans][1]])
				main_move.append([alice[1][ans][0],alice[1][ans][1]])

	elif total_enemy==0:
			for i in range(18,24):
				if d2!=0 and d1!=0:
					if i+d1<=44 and state[i]>0:
						main_move.append([i,i+d1])
						d1=0
					if i+d2<=44 and state[i]>0:
						main_move.append([i,i+d2])
						d2=0
				if d2==0 and d1!=0:
					if i+d1<=44 and state[i]>0:
						main_move.append([i,i+d1])
						d1=0
				if d1==0 and d2!=0:
					if i+d2<=44 and state[i]>0:
						main_move.append([i,i+d2])
						d2=0
	if pass_flag==0:		
		if main_move[0][1]>=24 :
			main_move[0][1]='O'
		else:
			main_move[0][1]+=1
		if  main_move[1][1]>=24:
			main_move[1][1]='O'
		else:
			main_move[1][1]+=1

		print str(main_move[0][0]+1)+' '+str(main_move[0][1])
		print str(main_move[1][0]+1)+' '+str(main_move[1][1])
	sys.exit(0)

	
def checkBearingOff(state):
	total_sum=0
	for i in range(0,18):
		if state[i]>0:
			total_sum+=state[i]
	if total_sum==0:
		return 1
	else:
		return 0


# The utility func	    
def utility(state,b):

	# PRIMING + BLITZ
	global my_blots_w
	global enemy_bar_w
	global my_bar_w
	global stronghold_w
	global anchor_w
	global primes_w
		
	my_bar=b[0]
	enemy_bar=b[1]
	my_blots=0
	enemy_blots=0
	anchor=0
	stronghold=0
	primes=0
	for i in range(0,24):
		if state[i]==1:
			my_blots+=1
		if state[i]==-1:
			enemy_blots+=1

		if state[i]>0:
			if state[i]>=2:
				stronghold+=1
				if i<11:
					stronghold_w-=100
				if i>15:
					stronghold_w+=100
				if i >=18:
					anchor+=1
			if i>0:
				if (state[i]>=2 and state[i-1]>=2):
					primes+=1
					if i<10:
						primes_w-=100
						enemy_bar_w+=100
					if i>14:
						primes_w+=200
			if i<23:
				if (state[i]>=2 and state[i+1]>=2):
					primes+=1


	uti=0 #total utility value for the move. maximizing it.
	uti=my_blots_w*my_blots+enemy_bar_w*enemy_bar+my_bar*my_bar_w+stronghold*stronghold_w+anchor_w*anchor+primes*primes_w
	return uti
#main	
def main():

	
	#21 possible rolls	
	rolls=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
	#state is an array that contains the present state of the game.
	state=raw_input()
	state=state.split(' ')
	state=map(int,state)
	state.append(0)
	for i in range(0,20):
		state.append(0)
	#bar variables	
	bar=raw_input()
#	bar=bar.split(' ')
#	bar=map(int,bar)
	abar=bar.count("a")
	bbar=bar.count("b")
	bar=[]
	bar.append(abar)
	bar.append(bbar)

	#dice1 and dice2 are the values on the two dice.	

	dice=raw_input()
	dice=dice.split(' ')
	dice=map(int,dice)
	dice1=dice[0]
	dice2=dice[1]
	
	#	Check Bearing Off
	#	bearingOff(state,dice1,dice2)
		
	#generate all valid and possible moves for Alice.
	
	# do outside
	move=[]
	move1=[]
	move2=[]
	# if time do evaulation of both moves
	if bar[0]>=2:
		state1=state[:]
		if state1[dice1-1]>=-1:
			move1.append([25,dice1-1])
			if state1[dice2-1]>=-1:
				move2.append([25,dice2-1])
			else:
				move2.append(["pass"," "])
		elif state1[dice2-1]>=-1:
			move1.append([25,dice2-1])
			if state1[dice1-1]>=-1:
				move2.append([25,dice1-1])
			else:
				move2.append(["pass"," "])
		else:
			move1.append(["pass"," "])
			move2.append(["pass"," "])


		move.append(move1)	
		move.append(move2)
		if move[0][0][0]==25:
			move[0][0][0]='Z'
		if move[0][0][0]!="pass":
			move[0][0][1]+=1
		if move[1][0][0]==25:
			move[1][0][0]='Z'
		if move[1][0][0]!="pass":
			move[1][0][1]+=1

		print str(move[0][0][0])+ ' ' + str(move[0][0][1])
		print str(move[1][0][0])+ ' ' + str(move[1][0][1])
		
	elif bar[0]==1:
		flag=0
		state1=state[:]
		max_val=-1000000000
		b=[]
		b.append(0)
		b.append(0)
		i=0
		b1=bar[:]
		if state1[dice1-1]>=-1:
			b1[0]-=1
			if state1[dice1-1]==-1:
				state1[dice1-1]+=2
			else:
				state1[dice1-1]+=1
			for j in range(0,24):

				if valid(state1,j,j+dice2):
					if state1[j+dice2]==-1:
						state1[j+dice2]+=2
					else:
						state1[j+dice2]+=1
					
					if utility(state1,b1)>max_val:
						max_val=utility(state1,b)
						i+=1	
						move1.append([25,dice1-1])
						move2.append([j,j+dice2])
						flag=1
		if state1[dice2-1]>=-1:
			b1=bar[:]
			state1=state[:]
			if state1[dice2-1]==-1:
				state1[dice2-1]+=2
			else:
				state1[dice2-1]+=1
			b1[0]-=1
			for j in range(0,24):
				if valid(state1,j,j+dice1):
					if state1[j+dice1]==-1:
						state1[j+dice1]+=2
					else:
						state1[j+dice1]+=1
					if utility(state1,b)>max_val:
						max_val=utility(state1,b)
						i+=1	
						move1.append([25,dice2-1])
						move2.append([j,j+dice1])
						flag=1

		if i!=0:
			if move1[i-1][0]==25:
				print 'Z',move1[i-1][1]+1

			move2[i-1][0]=move2[i-1][0]+1
			move2[i-1][1]=move2[i-1][1]+1
			print move2[i-1][0], move2[i-1][1]
		
		else:
			meh=0
			state1=state[:]
			if state1[dice1-1]>=-1 and state1[dice2-1]>=-1:
				if dice2>=dice1:
					move1.append([25,dice2-1])
					meh=1
				else:
					move1.append([25,dice1-1])
					meh=1
			elif state1[dice1]>=-1:
					move1.append([25,dice1-1])
					meh=1
			elif state1[dice2]>=-1:
					move1.append([25,dice2-1])
					meh=1
			
			if meh==1:
				print move1[0][0],move1[0][1]
			else:
				print "pass"
	else:
		if checkBearingOff(state):
			bearingOff(state,dice1,dice2,bar)
		
		#end outside
		alice=all_moves(state,dice1,dice2,bar)
		val=[]
		#iterate on the moves of Alice.
		for i in range(0,len(alice[0])):
			state1=state[:]
			b1=bar[:]
			#for each move, change the state of the board.
			state1[alice[0][i][0]]-=1

			if state1[alice[0][i][1]]==-1:
				state1[alice[0][i][1]]+=2
				b1[1]+=1
			else:
				state1[alice[0][i][1]]+=1

			state1[alice[1][i][0]]-=1
			if state1[alice[1][i][1]]==-1:
				state1[alice[1][i][1]]+=2
				b1[1]+=1
			else:
				state1[alice[1][i][1]]+=1
			m=[]
			#iterate over all the 21 dice rolls.
			for j in range(0,21):	
				#reverse and negative works. please check.
				state1.reverse()
				for k in range(0,24):
					state1[k]=-1*state1[k]
				#all valid and possible moves for Bob.	
				bob=all_moves(state1,rolls[j][0],rolls[j][1],b1)
				uti=[]
				b1.reverse()
					#for all possible moves of Bob, find the utility of the move. Storing in the array uti.
				for k in range(0,len(bob[0])):
					uti.append(utility(state1,b1))
		
				# shouldnt we fin min from our perspective not maximise bob's moves
				#max of rhe array uti. Now Bob will try to 
				min_val=100000000000000
				for i in range(len(uti)):
					if min_val>uti[i]:
						min_val=uti[i]
				#bob_uti=min(min_val)
				m.append(min_val)
			p=1
			chance_val=[]
			chance_sum=0
			for i in range(0,21):
				if rolls[i][0]==rolls[i][1]:
					p=0.028 #1/36
				else:
					p=0.056
				chance_sum+=p*m[i]
			final_val=chance_sum/21
			val.append(final_val)
		if len(alice[0])==0:
			print "pass"
		else:
			ans=val.index(max(val))
			if alice[0][ans][1]==24:
				print str(alice[0][ans][0]+1)+' '+'O'
			else:
				print str(alice[0][ans][0]+1)+' '+str(alice[0][ans][1]+1)
			if alice[1][ans][1]==24:
				print str(alice[1][ans][0]+1)+' '+'O'
			else:
				print str(alice[1][ans][0]+1)+' '+str(alice[1][ans][1]+1)
	
main()

