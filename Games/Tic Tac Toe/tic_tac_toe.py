# Classic Tic Tac Toe Game

import os
import time
import winsound

# Function to print board
def board_print(board):
	os.system('cls')

	print(f"  {board[7]} | {board[8]} | {board[9]}  ")
	print(f"----|---|----")
	print(f"  {board[4]} | {board[5]} | {board[6]}  ")
	print(f"----|---|----")
	print(f"  {board[1]} | {board[2]} | {board[3]}  ")


# Function to mark position of player 1
def player1_mark_input(board):

	while True:
		mark = int(input("\nPlayer 1 choose your position: "))

		if board[mark] == ' ':
			board.pop(mark)
			board.insert(mark,player1)
			winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
			return board_print(board)
			break

		else:
			print('Wrong input !')
			continue

# Function to mark position of player 2
def player2_mark_input(board):

	while True:
		mark = int(input("\nPlayer 2 choose your position: "))

		if board[mark] == ' ':
			board.pop(mark)
			board.insert(mark,player2)
			winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
			return board_print(board)
			break

		else:
			print('Wrong input !')
			continue


# Function to decide mark of players
def mark_decide():

	player1 = ''
	player2 = ''

	while True:

		turn = input("\nPlayer 1 please choose your mark: X/O ")

		if turn.lower() == 'x':
			player1 = 'X'
			player2 = 'O'
			return player1,player2
			break

		elif turn.lower() == 'o':
			player1 = 'O'
			player2 = 'X'
			return player1,player2
			break

		else:
			print("\nWrong Input !")
			continue


# Function to check if any player has won the match
def win_check(board):

	if board[1] == board[2] == board[3] == 'X' or \
	   board[4] == board[5] == board[6] == 'X' or \
	   board[7] == board[8] == board[9] == 'X' or \
	   board[1] == board[4] == board[7] == 'X' or \
	   board[2] == board[5] == board[8] == 'X' or \
	   board[3] == board[6] == board[9] == 'X' or \
	   board[1] == board[5] == board[9] == 'X' or \
	   board[7] == board[5] == board[3] == 'X':
	   return True

	elif board[1] == board[2] == board[3] == 'O' or \
	   board[4] == board[5] == board[6] == 'O' or \
	   board[7] == board[8] == board[9] == 'O' or \
	   board[1] == board[4] == board[7] == 'O' or \
	   board[2] == board[5] == board[8] == 'O' or \
	   board[3] == board[6] == board[9] == 'O' or \
	   board[1] == board[5] == board[9] == 'O' or \
	   board[7] == board[5] == board[3] == 'O':
	   return True

	else:
		return False


# Function to check wheather match is draw
def draw_check(board):
	if ' ' in board:
		return False
	else:
		return True


# Function to decide wheather players want to play  match again
def replay():

	user_input = input("\nWould you like to play again? Y/N ")

	if user_input.lower() == 'y':
		return True
	else:
		return False

# Wrapping Function
while True:

	os.system('cls')

	print("Welcome to TIC TAC TOE !")

	test_board = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	player1,player2 = mark_decide()
	print(f"\nMark of Player 1: {player1}")
	print(f"Mark of player 2: {player2}")
	time.sleep(3)
	while True:
		
		board_print(test_board)

		player1_mark_input(test_board)

		if win_check(test_board):
			print("\nCongratulations Player 1, You have won the match !!")
			winsound.PlaySound('fire_crackers.wav', winsound.SND_ASYNC)
			break
		elif draw_check(test_board):
			print("\nMatch is draw !")
			winsound.PlaySound('tada.wav', winsound.SND_ASYNC)
			break

		player2_mark_input(test_board)

		if win_check(test_board):
			print('\nCongratulations Player 2, You have won the match !!')
			winsound.PlaySound('fire_crackers.wav', winsound.SND_ASYNC)
			break
		else:
			continue
		
	if replay():
		continue
	break
