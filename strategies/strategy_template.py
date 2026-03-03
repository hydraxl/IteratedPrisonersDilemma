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
def strategy_template(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on
    r.both_cheat # The points you'll obtain if you both cheat
    r.both_cooperate # The points you'll obtain if you both cooperate
    r.one_cooperate[0] # The points you'll obtain if you cheat and your opponent cooperates
    r.one_cooperate[1] # The points you'll obtain if you cooperate and your opponent cheats

    h.data # The list of all decisions made by you and your opponents previously
    first = h.data[0] # The decisions made by you and your opponent when you first met
    recent = h.data[len(h.data) - 1] # The decisions made by you and your opponent most recently
    first[0] # Your first decision
    first[1] # Your opponent's first decision
    recent[0] # Your most recent decision
    recent[1] # Your opponent's most recent decision


    # Decision Logic
    #   How you actually decide whether to cooperate or cheat
    #   Do something smarter than this    
    if r.both_cheat >= r.both_cooperate:
        decision = Choice.CHEAT
    else:
        decision = Choice.COOPERATE

    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
