# Template for what a good strategy function looks like
from .common import *

# Imported 3 classes:
#
#       Choice contains 2 values: Choice.CHEAT and Choice.COOPERATE
#           Your strategy function should return a Choice value
#
#       Ruleset contains the point values for each outcome
#           both_cooperate is an integer that is awarded to both players if they cooperate
#           both_cheat is an integer that is awarded to both players if they cheat
#           one_cooperate is the result if one player cooperates and the other cheats
#               Takes the form (CHEAT, COOPERATE), where CHEAT is the points awarded to
#               the player who cheats and COOPERATE is the points awarded to the player
#               who cooperates.
#           A good strategy will change depending on what the ruleset incentivizes
#
#       History contains a list of previous choices made by you and your opponent
#           data is the only variable your code should look at
#           data takes the form of a list of tuples containing Choice values -> [(Choice, Choice), ...]
#           The tuples take the form (you, opponent)
#           Ordered from first match to last -> data[0] is your first encounter with that opponent
#           If data == [], then this is your first encounter with this opponent
#           A good strategy will adjust based on your opponent's previous actions


# Function template
def copy_last_three(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on

    h.data # The list of all decisions made by you and your opponents previously

    # Decision Logic
    #   How you actually decide whether to cooperate or cheat  
    
    # Start with cooperate and then cheat
    if len(h.data) == 0: decision = Choice.COOPERATE
    elif len(h.data) == 1: decision = Choice.CHEAT

    # Cooperate unless they cheated both of the last 2 rounds
    elif len(h.data) == 2:
        print(f"{h.data[0][1]} {h.data[1][1]}")
        if h.data[0][1] == Choice.CHEAT and h.data[1][1] == Choice.CHEAT:
            decision = Choice.CHEAT
        else: decision = Choice.COOPERATE
    
    # Choose whichever they have done more of in the last 3 rounds
    else:
        n = len(h.data) - 1 # Index of most recent round

        # Count how many times the opponent cheated in the last 3 rounds
        num_cheats = 0
        for i in range(3):
            if h.data[n-i][1] == Choice.CHEAT:
                num_cheats += 1
        
        # Choose the option they have chosen more frequently
        if num_cheats >= 2:
            decision = Choice.CHEAT
        else: decision = Choice.COOPERATE

    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
