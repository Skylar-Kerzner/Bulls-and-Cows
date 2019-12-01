#!/usr/bin/env python
# coding: utf-8


"""Number Guessing Game a.k.a. Bulls and Cows
    Players will receive a Welcome Message, and then 
    can input a number of digits for the game.
    
    Players will guess numbers of the given length, 
    to guess the computer's randomly generated number.
    
    With each guess made by the player, 
    the computer will return a message 
    of how many digit are correct and in the right place.
    as well as how many additional instances of
    the right digit but in the wrong place.


    Players keep guessing until they get it right.
    
    Player guesses muste be in number form, or they
    will be asked to retry their guess."""

import random

play_a_round = True
#At game end, always start a new round.
while play_a_round == True:
    
    #Welcome the Player
    print(
        "Welcome to the number guessing game (also known as Bulls & Cows).\n I hope you have fun!! =))\n \n")
    
    #If the number of digits is not a number, tell the player to try again. 
    try:
        game_num_digits = int(input("Please input a number a digits for your game:"))
    except ValueError:
        print("\n \n Whoops! Please put in an integer number of digits\n \n")
        continue

    #This will be the list of digits to be guessed
    answer_list = [random.randint(0, 9) for i in range(game_num_digits)] 
    
    #Enter the same loop for each player guess, until they win and the loop breaks.
    while True:

        #Take Player guess.
        new_guess = input("please input your guess:")

        #If it's not an integer, give player instruction to change guess, and 
        try: 
            new_guess_int = int(new_guess)
        except ValueError: 
            print("\n \n Oh noo! Please put your guess digits together into a single number.\n \n")
            continue
        
        #If it's the wrong number of digits, inform the player and have them try again.
        if len(new_guess) != game_num_digits:
            print("\n \n Uh oh! That's not the right number of digits! \n \n")
            continue
        
        #The guesses are converted into a list
        new_guess_list = [int(x) for x in new_guess]
        
        #Get List of True and False for whether each digit is an exact match
        #Then add up the Trues to get total number of exact matches
        exact_matches_boolean = [new_guess_list[i] == answer_list[i] for i in range(game_num_digits)]
        num_exact_match = sum(exact_matches_boolean)
        
        #If the guess is correct, End Game and state You Win!!
        if num_exact_match == game_num_digits:
            print("You win!!\n \n")
            break
        
        #Guess list with the exact nums removed
        guess_list_removed_exact = [x for i,x in enumerate(new_guess_list) if not exact_matches_boolean[i]]
        #Answer list with the exact nums removed
        answer_list_removed_exact = [x for i,x in enumerate(answer_list) if not exact_matches_boolean[i]]
        
        #Get the number of out of place matches
        #by checking whether each remaining guess digit 
        #is in the answer, and if so adding it to a new list
        #and removing once instance of that digit from the answer list
        matches_out_of_place = []
        for digit in guess_list_removed_exact:
            if digit in answer_list_removed_exact:
                matches_out_of_place.append(digit)
                answer_list_removed_exact.remove(digit)
        
        #Get the number of out-of-place matches
        num_matches_out_of_place = len(matches_out_of_place)
        
        #Tell the player how many guesses are exact and out of place.
        print("Great! You have {} exact matches and {} other digits that are correct but out of place!\n \n".format(num_exact_match,num_matches_out_of_place))
            
        
    
        #TODO: Ask the player whether they want to play again.
        #If Yes, then go back to the beginning.
        #If No, then say goodbye!
        #For now, auto restarts a new game
    
    
