"""
Name: Lucy An
Date: January 2 2018
Description: a simple single-player, grid-based game where the 
user must find 3 hidden treasures with at most 10 guesses to win
"""
import random 

def main():
    """This function defines mainline logic."""
    numGuess = 10 
    numTreasures = 0 
    opensesame = open("Winners.txt", "a")
    fame = "HALL OF FAME" 
    initial = "<--Empty!-->"
    opensesame.close()
    opensesame = open("Winners.txt", "r")
    print "WELCOME TO TREASURE HUNT!"
    print 
    print fame.center(14)
    if opensesame.readline() == "":
        print "=============="
        print initial.strip().center(13)
        print "=============="
        opensesame.close()
    else:
        opensesame = open("Winners.txt", "r")
        print "=============="
        for line in opensesame:
            print line.strip().center(13)
        print "=============="              
        opensesame.close()
    
    v3Row = input("How many rows would you like (3-10): ")
    v3Col = input("How many columns would you like (3-10): ")
    board = ""
    
    # This statement defines the game board
    board = [[' ' for _ in range(v3Col)] for _ in range(v3Row)]  
    
   
    hide_treasure(board, v3Row,v3Col)
    
    print "You have 10 guesses left and have found 0/3 treasures."    
    print 
    while numGuess > 0 and numTreasures < 3:
        display_board(board, v3Row, v3Col, show_treasure = True)
        numGuess -= 1 
        if make_user_move(board, v3Row, v3Col) == True:
            numTreasures += 1
        if numGuess != 0:
            print "You have", numGuess, "guesses left and have found", str(numTreasures) + "/3 treasures."
        
    display_board(board, v3Row, v3Col, show_treasure = True)             
    if numTreasures == 3:
        print 
        print "Congragulations! You have found ALL of the hidden treasures."
        print 
        winnerName = raw_input("What's your name stranger? ")
        newChampion = open("Winners.txt", "a")
        newChampion.write(winnerName + "\n")
        newChampion.close()
        print 
        print "*** GAME OVER ***"
    else:
        print 
        print "OH NO! You only found", str(numTreasures) + "/3 treasures."
        print 
        print "*** GAME OVER ***"
        
    

def hide_treasure(board, v3Row, v3Col):
    """This function selects six random integers as the hidden locations of 
    the treasures and checks that they are all distinct from one another. """
    status = False
    last = False
    
    while status == False:
        t1Row = random.randint(0,v3Row -1)
        t1Col = random.randint(0,v3Col -1)
        
        board[t1Row][t1Col] = "T"
        
        t2Row = random.randint(0,v3Row -1)
        t2Col = random.randint(0,v3Col -1)        
        
        if board[t2Row][t2Col] == "T":
            status = False
        else:
            board[t2Row][t2Col] = "T"
            status = True
    while last == False:
        t3Row = random.randint(0,v3Row -1)
        t3Col = random.randint(0,v3Col -1)
        if board[t3Row][t3Col] == "T":
            last = False
        else:
            board[t3Row][t3Col] = "T"
            last = True
            

def display_board(board, v3Row, v3Col, show_treasure = True):
    """This function outlines what the board will look 
    like such as the number of columns and rows.""" 
  
    if show_treasure == False:
        colstring = "  "
        newRow, newCol = 0,0
        
        for num in range(v3Col):
            colstring += str(num) + "   " 
        print colstring 
        
        for newRow in range(v3Row):
            rowstring = str(newRow) + ":"
            for newCol in range(v3Col):
                rowstring += str(board[newRow][newCol]) + " | "
            print rowstring.replace("T", " ") 
            print " " + "---+" *v3Col                 
        
    else:
        colstring = "  "
        newRow, newCol = 0,0
            
        for num in range(v3Col):
            colstring += str(num) + "   " 
        print colstring 
        
        for newRow in range(v3Row):
            rowstring = str(newRow) + ":"
            for newCol in range(v3Col):
                rowstring += str(board[newRow][newCol]) + " | "
            print rowstring
            print " " + "---+" *v3Col            
            
def make_user_move(board, v3Row, v3Col):
    """This function allows the user to make a guess and evaluates it."""
    turn = True 
    valid = False
    while turn == True: 
        while valid == False:
            try: 
                row = input("What row would you like to search?" + "(0-"  + str(v3Row) + "): ")
                col = input("What column would you like to search?" + "(0-"  + str(v3Col) + "): ")
                
                # This statement works as input validation, checking if the chosen spot is available. 
                if (row > v3Row or row < 0) or (col > v3Col or col < 0) or (col > v3Col or col < 0) and (row > v3Row or row < 0):
                    print "Sorry, invalid location. Please try again!"
                    print 
                elif board[row][col] == "X" or board[row][col] == "$" or board[row][col] == "!":
                    print "You already tried there, please pick again." 
                else:
                    valid = True 
            
            # This block of code works around input that would cause the program to crash. 
            except NameError:
                print "Integers only for row and column values. Please try again!"
                print 
        
        close = 0
        try:      
            if board[row][col] == "T":
                board[row][col] = "$"
                print "Yes! You have found a treasure."
                gain, turn = True, False    
            
            if board[row][col] == " ":
                for rowP in [row, row -1, row + 1 ]:
                    for colP in [col, col + 1, col - 1]:
                        if board[rowP][colP] == "T":
                            close += 1 
            if close > 0:
                print "Very close, treasure is near.."
                board[row][col] = "!"
                gain, turn = False, False
                               
            if close == 0:
                print "Nothing there."
                board[row][col] = "X"
                gain, turn = False, False 
            return gain
        
        # This statement deals with index errors that would cause the program to crash. 
        except IndexError:
            break
        continue
           
main()       
        
               
