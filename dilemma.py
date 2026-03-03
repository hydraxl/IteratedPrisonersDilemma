from enum import Enum

class Choice(Enum):
    COOPERATE = 0
    CHEAT = 1

class Ruleset():
    # Point Values gained in each outcome
    BOTH_COOPERATE = 2
    ONE_COOPERATE = (3, -1) # (CHEAT, COOPERATE)
    BOTH_CHEAT = 0

# History of previous outcomes with the same opponent
class History:
    def __init__(self, history: list[tuple[Choice, Choice]]=[], flipped: list[tuple[Choice, Choice]]=[]):
        self.history = history
        self.flipped = flipped
    
    def add(self, c1: Choice, c2: Choice):
        self.history.append( (c1, c2) )
        self.flipped.append( (c2, c1) )
    
    # Flips c1 and c2 for when history is shared with second player
    def flip(self) -> History:
        # WARNING: Returns a direct reference to the class variable.
        # Mutating the returned object will modify shared class state.
        return History(self.flipped, self.history)

# Method for deciding whether to cooperate or cheat based on match history
class Player():
    def __init__(self, strategy, score: int=0):
        self.strategy = strategy
        self.score = score

# Run two players against each other and assign points based on the decision they make
def run_dilemma(p1: Player, p2: Player, h: History) -> tuple[Choice, Choice]:
    choice1 = p1.strategy(h)
    choice2 = p2.strategy(h.flip())

    h.add(choice1, choice2)
    
    if choice1 == Choice.COOPERATE and choice2 == Choice.COOPERATE:
        result = Ruleset.BOTH_COOPERATE
        p1.score += result
        p2.score += result
    
    elif choice1 == Choice.CHEAT and choice2 == Choice.COOPERATE:
        result = Ruleset.ONE_COOPERATE
        p1.score += result[0]
        p2.score += result[1]
    
    elif choice1 == Choice.COOPERATE and choice2 == Choice.CHEAT:
        result = Ruleset.ONE_COOPERATE
        p1.score += result[1]
        p2.score += result[0]
    
    else:
        result = Ruleset.BOTH_CHEAT
        p1.score += result
        p2.score += result
    
    # Return the choices made by each player
    return choice1, choice2

def iterate_dilemma(p1: Player, p2: Player, n: int = 10):
    h = History() # History tracker

    # Repeat dilemma n times, updating history with each iteration
    for i in range(n):
        choices = run_dilemma(p1, p2, h)
        h.add(*choices)



