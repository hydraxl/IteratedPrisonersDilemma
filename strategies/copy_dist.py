# Template for what a good strategy function looks like
from .common import *

import random

# Function template
def copy_dist(h: History, r: Ruleset) -> Choice:
    # Important Variables
    decision = None # What decision you're currently settled on

    h.data # The list of all decisions made by you and your opponents previously

    # Decision Logic
    #   How you actually decide whether to cooperate or cheat

    # Cooperate on first round
    if len(h.data) == 0: decision = Choice.COOPERATE
    
    # Choose randomly, weighted by opponent's past choices
    # If they have cooperated twice and cheated once 
    #     then this gives a 2/3 chance to cooperate
    else:

        # Determine weights based on count of cooperate and cheat
        num_cooperates = 0
        num_cheats = 0
        for d in h.data:
            if d[1] == Choice.COOPERATE:
                num_cooperates += 1
            else:
                num_cheats += 1

        # Randomly determine decision based on weights
        n = random.random()
        if n * (num_cooperates + num_cheats) >= num_cooperates:
            decision = Choice.CHEAT
        else: decision = Choice.COOPERATE



    # Your return value MUST be either Choice.CHEAT or Choice.COOPERATE
    return decision
    
