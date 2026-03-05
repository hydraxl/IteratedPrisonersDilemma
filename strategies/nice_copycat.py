# Template for what a good strategy function looks like
from .common import *

# Function template
def nice_copycat(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on

    h.data # The list of all decisions made by you and your opponents previously

    if len(h.data) < 2: decision = Choice.COOPERATE # First two rounds cooperate
    else: decision = h.data[len(h.data) - 1][1] # After that, copy most recent move

    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
