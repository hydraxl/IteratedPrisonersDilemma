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
def copycat(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on
    
    h.data # The list of all decisions made by you and your opponents previously

    if len(h.data) == 0: decision = Choice.COOPERATE # First round cooperate
    else: decision = h.data[len(h.data) - 1][1] # After that, copy most recent move

    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
