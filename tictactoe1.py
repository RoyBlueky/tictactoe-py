import random
import subprocess
import time
import string
#functions
#print board
def printboard(board):
	for i in range(0,3):
		for j in range(0,3):
			print board[i][j],
		else:
			print "\n"

#who first
def first():
	flag = True
	num = random.choice(range(2))
	guess = input("Please guess an integer between 0 and 1: ")
	if num == guess:
		flag = True
	else:
		flag = False
	#print flag
	return flag

#user
def user(board):
	print "Please enter a number between 1 and 9"
	position = input()
	while True:
		if position == 7:
			if board[0][0] =="-":
				board[0][0] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 8:
			if board[0][1] == "-":
				board[0][1] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 9:
			if board[0][2] == "-":
				board[0][2] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 4:
			if board[1][0] == "-":
				board[1][0] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 5:
			if board[1][1] == "-":
				board[1][1] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 6:
			if board[1][2] == "-":
				board[1][2] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 1:
			if board[2][0] == "-":
				board[2][0] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 2:
			if board[2][1] == "-":
				board[2][1] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		elif position == 3:
			if board[2][2] == "-":
				board[2][2] = "X"
				break
			else:
				print "Sorry, this position is not avaliable"
				print "Please enter another number: "
				position = input()
		else:
			print "Incorrect number! Please enter another number: "
			position = input()
	return board	
	
#computer	
def computer(board):
	if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="-":
		board[0][2]="O"
	elif board[0][0]=="O" and board[0][2]=="O" and board[0][1]=="-":
		board[0][1]="O"
	elif board[0][1]=="O" and board[0][2]=="O" and board[0][0]=="-":
		board[0][0]="O"
	elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="-":
		board[1][2]="O"
	elif board[1][0]=="O" and board[1][2]=="O" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="O" and board[1][2]=="O" and board[1][0]=="-":
		board[1][0]="O"		
	elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="-":
		board[2][2]="O"
	elif board[2][0]=="O" and board[2][2]=="O" and board[2][1]=="-":
		board[2][1]="O"
	elif board[2][1]=="O" and board[2][2]=="O" and board[2][0]=="-":
		board[2][0]="O"
	elif board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="-": 
		board[2][0]="O"
	elif board[0][0]=="O" and board[2][0]=="O" and board[1][0]=="-": 
		board[1][0]="O"
	elif board[1][0]=="O" and board[2][0]=="O" and board[0][0]=="-": 
		board[0][0]="O"
	elif board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="-":
		board[2][1]="O"
	elif board[1][1]=="O" and board[2][1]=="O" and board[0][1]=="-":
		board[0][1]="O"
	elif board[0][1]=="O" and board[2][1]=="O" and board[1][1]=="-":
		board[1][1]="O"
	elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="-":
		board[2][2]="O"
	elif board[0][2]=="O" and board[2][2]=="O" and board[1][2]=="-":
		board[1][2]="O"
	elif board[1][2]=="O" and board[2][2]=="O" and board[0][2]=="-":
		board[0][2]="O"
	elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="-":
		board[2][2]="O"
	elif board[0][0]=="O" and board[2][2]=="O" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="O" and board[2][2]=="O" and board[0][0]=="-":
		board[0][0]="O"
	elif board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="-":
		board[2][0]="O"
	elif board[0][2]=="O" and board[2][0]=="O" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="O" and board[2][0]=="O" and board[0][2]=="-":
		board[0][2]="O"
		
	elif board[0][1]=="X" and board[1][0]=="X" and board[0][0]=="-" and board[0][2]=="-" and board[2][0]=="-":
		board[0][0]="O"
	elif board[1][0]=="X" and board[2][1]=="X" and board[2][0]=="-" and board[0][0]=="-" and board[2][2]=="-":
		board[2][0]="O"
	elif board[0][1]=="X" and board[1][2]=="X" and board[0][0]=="-" and board[0][2]=="-" and board[2][2]=="-":
		board[0][2]="O"
	elif board[2][1]=="X" and board[1][2]=="X" and board[2][0]=="-" and board[2][2]=="-" and board[0][2]=="-":
		board[2][2]="O"
		
	elif board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="-":
		board[0][2]="O"
	elif board[0][0]=="X" and board[0][2]=="X" and board[0][1]=="-":
		board[0][1]="O"
	elif board[0][1]=="X" and board[0][2]=="X" and board[0][0]=="-":
		board[0][0]="O"
	elif board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="-":
		board[1][2]="O"
	elif board[1][0]=="X" and board[1][2]=="X" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="X" and board[1][2]=="X" and board[1][0]=="-":
		board[1][0]="O"		
	elif board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="-":
		board[2][2]="O"
	elif board[2][0]=="X" and board[2][2]=="X" and board[2][1]=="-":
		board[2][1]="O"
	elif board[2][1]=="X" and board[2][2]=="X" and board[2][0]=="-":
		board[2][0]="O"
	elif board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="-": 
		board[2][0]="O"
	elif board[0][0]=="X" and board[2][0]=="X" and board[1][0]=="-": 
		board[1][0]="O"
	elif board[1][0]=="X" and board[2][0]=="X" and board[0][0]=="-": 
		board[0][0]="O"
	elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="-":
		board[2][1]="O"
	elif board[1][1]=="X" and board[2][1]=="X" and board[0][1]=="-":
		board[0][1]="O"
	elif board[0][1]=="X" and board[2][1]=="X" and board[1][1]=="-":
		board[1][1]="O"
	elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="-":
		board[2][2]="O"
	elif board[0][2]=="X" and board[2][2]=="X" and board[1][2]=="-":
		board[1][2]="O"
	elif board[1][2]=="X" and board[2][2]=="X" and board[0][2]=="-":
		board[0][2]="O"
	elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="-":
		board[2][2]="O"
	elif board[0][0]=="X" and board[2][2]=="X" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="X" and board[2][2]=="X" and board[0][0]=="-":
		board[0][0]="O"
	elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="-":
		board[2][0]="O"
	elif board[0][2]=="X" and board[2][0]=="X" and board[1][1]=="-":
		board[1][1]="O"
	elif board[1][1]=="X" and board[2][0]=="X" and board[0][2]=="-":
		board[0][2]="O"
	elif board[1][1] == "-":
		board[1][1]="O"

	elif board[0][0] == "-":
		board[0][0] = "O"
	elif board[0][2] == "-":
		board[0][2] = "O"
	elif board[2][0] == "-":
		board[2][0] = "O"
	elif board[2][2] == "-":
		board[2][2] = "O"
		
	elif board[0][1] == "-":
		board[0][1] = "O"
	elif board[1][2] == "-":
		board[1][2] = "O"
	elif board[2][1] == "-":
		board[2][1] = "O"
	elif board[1][0] == "-":
		board[1][0] = "O"
	return board
	
def ifwin(board):
	win = 0
	if (board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X") or (board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X") or (board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X") or (board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X") or (board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X") or (board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X") or (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X") or (board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X"):      
		print "Congratulations! You win"
		win = 0
	elif (board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O") or (board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O") or (board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O") or (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O") or (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O") or (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O") or (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O") or (board[0][2]=="O" and board[1][1]=="" and board[2][0]=="O"):
		print "Sorry! Computer wins"
		win = 1
	else:
		full = True
		for i in range(0,3):
			for j in range(0,3):
				if board[i][j] == "-":
					full = False
		if full == True:
			print "It's tie!"
			win = 2
		else:
			win = 3
	return win		
			
boardmode= [[7,8,9],[4,5,6],[1,2,3]]
for i in range(0,3):
		for j in range(0,3):
			print boardmode[i][j],
		else:
			print "\n"	
board = [["-" for col in range(3)]for row in range(3)]
printboard(board)
play = "Y"
while play == "Y" or play == "y":
        if first()==True:
                print "You are right! You first!"
                while play == "Y" or play == "y":
                        step = 0
                        board = [["-" for col in range(3)]for row in range(3)]
                        while step<9:
                                user(board)
                                printboard(board)
                                step = step+1
                                win = ifwin(board)
                                if win==0 or win==1 or win==2:
                                        play = raw_input("Do you want to try again? Y or N: ")
                                        break
                                computer(board)
                                printboard(board)
                                step =step+1
                                win = ifwin(board)
                                if win==0 or win==1 or win==2:
                                        play = raw_input("Do you want to try again? Y or N: ")
                                        break
                print "Thank you for playing!"
        else:
                print "You are wrong! Computer first!"
                step = 0
                board = [["-" for col in range(3)]for row in range(3)]
                while step<9:
                        computer(board)
                        printboard(board)
                        step =step+1
                        win = ifwin(board)
                        if win==0 or win==1 or win==2:
                                play = raw_input("Do you want to try again? Y or N: ")
                                break
                        user(board)
                        printboard(board)
                        step =step+1
                        win = ifwin(board)
                        if win==0 or win==1 or win==2:
                                play = raw_input("Do you want to try again? Y or N: ")
                                break
        print "Thank you for playing!"
