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


# import statements

def get_school(card):
    if card[5] == '1':
        school1 = "School of Computing and Engineering SCE"
        return school1
    elif card[5] == '2':
        school1 = "School of Law"
        return school1
    elif card[5] == '3':
        school1 = "College of Arts and Sciences"
        return school1
    

def get_grade(card):
    if card[6] == '1':
        grade1 = "Freshman"
        return grade1
    elif card[6] == '2':
        grade1 = "Sophomore"
        return grade1
    elif card[6] == '3':
        grade1 = "Junior"
        return grade1
    elif card[6] == '4':
        grade1 = "Senior"
        return grade1
    
def character_value(val):
    x = ord(val)
    if x >= 65 or x <= 90:
        y = x - 65
        return y
    

def get_check_digit(card):
    z = 0
    for i in range (0, 5):
        x = character_value(card[i])
        z += i+1 * x
    a = int(card[5]) * 6
    b = int(card[6]) * 7
    c = int(card[7]) * 8
    d = int(card[8]) * 9
    digit = int(z + a + b + c + d) % 10
    return digit
    
def verify_check_digit(card, value):
    if len(card) != 10:
        error = "The length of the card must be 10"
        return error
    elif card[0].isdigit() == True or card[1].isdigit() == True or card[2].isdigit() == True or card[3].isdigit() == True or card[4].isdigit() == True:
        error = "The first 5 characters must be A-Z"
        return error
    elif card[7].isdigit() == False or card[8].isdigit() == False or card[9].isdigit() == False:
        error = "The last 3 characters must be 0-9"
        return error
    elif card[5] != '1' and card[5] != '2' and card[5] != '3':
        error = "The sixth character must be 1, 2 or 3"
        return error
    elif card[6] != '1' and card[6] != '2' and card[6] != '3' and card[6] != '4':
        error = "The seventh character must be 1, 2, 3 or 4"
        return error
    elif card[9] != value:
        error = "Check Digit does not match calculated value"
        return error
    

if __name__ == "__main__":

    # main program
    print("Main Program")
    running = 1
    while running == 1:

        
        card = input("Enter Library Card. Hit enter to exit==> ")

        if card == " ":
            running = 0
            
        value = get_check_digit(card)
        school = get_school(card)
        grade = get_grade(card)
        mistake = verify_check_digit(card, value)
        
        if int(card[9]) != value:
            print("Invalid Card")
            print(mistake)
        if int(card[9]) == value:
            print("The library card is valid")
            print(f'The card belongs to a student in the {school}')
            print(f'The card belongs to a {grade}')




        
        
