########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    repeat = input('Do you want to play again? Y for yes or N for no')
    while repeat != 'Y' and repeat != 'YES' and repeat != 'yes' and repeat != 'y' and repeat != 'Yes' and repeat != 'YEs' and repeat != 'yEs' and repeat != 'NO' and repeat != 'n' and repeat != 'No' and repeat != 'no' and repeat!= 'No':
        print('Invalid answer')
        repeat = input('Do you want to play again? Y for yes or N for no')
    if repeat == 'Y' or repeat == 'YES' or repeat == 'yes' or repeat == 'y' or repeat == 'Yes' or repeat == 'YEs' or repeat == 'yEs':
        return playing == True
    elif repeat == 'NO' or repeat == 'n'or repeat == 'No' or repeat == 'no' or repeat == 'N':
        return playing == False
    
     
def get_wager(bank) -> int:
    wager = int(input('How much would you like to wager?'))
    while wager <=0 or wager > bank:
        print('Invalid amount')
        wager = int(input('How much would you like to wager?'))
    return wager        

def get_slot_results() -> tuple:
    slot_1_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    slot_2_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    slot_3_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    reela = random.choice(slot_1_list)
    reelb = random.choice(slot_2_list)
    reelc = random.choice(slot_3_list)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb and reela == reelc:
        matches = 3
        return matches
    elif reela == reelb or reela == reelc or reelb == reelc:
        matches = 2
        return matches
    else:
        matches = 0
        return matches
    

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips would you like to wager? Please enter an amount between 1-100'))
    while bank <=0 or bank > 100:
        print('Please enter a valid amount.')
        bank = int(input('How many chips would you like to wager? Please enter an amount between 1-100'))
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 3:
        payout = (wager * 10) - wager
        return payout
    elif matches == 2:
        payout = (wager * 3) - wager
        return payout
    else:
        wager *= -1
        return wager 


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        init_bank = bank
        spins = 0
        new_high = init_bank

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spins += 1

            if bank > new_high:
                new_high = bank
            
           
        print("You lost all", init_bank, "in", spins, "spins")
        print("The most chips you had was", new_high)
        playing = play_again()
