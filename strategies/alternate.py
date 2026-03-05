# Template for what a good strategy function looks like
from .common import *

# Function template
def alternate(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on
 
    # Decision Logic
    #   How you actually decide whether to cooperate or cheat
   
    # Alternate between cooperating and cheating
    # Start with cheat on first round
    if len(h.data) % 2 == 0: decision = Choice.CHEAT
    else: decision = Choice.COOPERATE

    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
