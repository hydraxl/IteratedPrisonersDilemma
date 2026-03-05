from enum import Enum

class Choice(Enum):
    COOPERATE = 0
    CHEAT = 1

class Ruleset:
    def __init__(self, both_cooperate: int = 2, both_cheat: int = 0, one_cooperate: tuple[int, int] = (3, -1)):
        # Point Values gained in each outcome
        self.both_cooperate = both_cooperate # default 2
        self.one_cooperate = one_cooperate # default (3, -1), format (CHEAT, COOPERATE)
        self.both_cheat = both_cheat # default 0
    
    def __str__(self):
        return ("Rules:\n" +
        f"    Both Cooperate: {self.both_cooperate} points each\n" +
        f"    Both Cheat: {self.both_cheat} points each\n"
        f"    One Cooperates: cheater earns {self.one_cooperate[0]}" + 
        f" points and cooperater earns {self.one_cooperate[1]} points\n"
        )

# History of previous outcomes with the same opponent
class History:
    def __init__(self, data: list[tuple[Choice, Choice]]=[], flipped: list[tuple[Choice, Choice]]=[]):
        # Lists are ordered such that index 0 is the oldest set of choices
        self.data = data # Follows format [(p1_choice, p2_choice), ]
        self.flipped = flipped # Follows format [(p2_choice, p1_choice), ]
    
    # Appends most recent choices to the end of the lists
    def add(self, c1: Choice, c2: Choice):
        self.data.append( (c1, c2) )
        self.flipped.append( (c2, c1) )
    
    # Flips c1 and c2 for when history is shared with second player
    def flip(self) -> History:
        # WARNING: Returns a direct reference to the class variable.
        # Mutating the returned object will modify shared class state.
        return History(self.flipped, self.data)
    
    def __str__(self):
        return self.data

# Method for deciding whether to cooperate or cheat based on match history
class Player():
    def __init__(self, strategy, score: int=0):
        self.strategy = strategy
        self.score = score

# Run two players against each other and assign points based on the decision they make
def run_dilemma(p1: Player, p2: Player, h: History, r: Ruleset):
    
    # Both players are shown history in the format [(their choice, opponent choice)]
    choice1 = p1.strategy(h, r)
    choice2 = p2.strategy(h.flip(), r)

    # Add decisions to history variable
    h.add(choice1, choice2)
    
    # Determine point changes
    if choice1 == Choice.COOPERATE and choice2 == Choice.COOPERATE:
        result = r.both_cooperate
        p1.score += result
        p2.score += result
    
    elif choice1 == Choice.CHEAT and choice2 == Choice.COOPERATE:
        result = r.one_cooperate
        p1.score += result[0]
        p2.score += result[1]
    
    elif choice1 == Choice.COOPERATE and choice2 == Choice.CHEAT:
        result = r.one_cooperate
        p1.score += result[1]
        p2.score += result[0]
    
    else:
        result = r.both_cheat
        p1.score += result
        p2.score += result

def iterate_dilemma(p1: Player, p2: Player, n: int = 10, r: Ruleset = Ruleset()):
    h = History() # History tracker
    r = Ruleset() # Default ruleset

    # Repeat dilemma n times, updating history with each iteration
    for i in range(n):
        run_dilemma(p1, p2, h, r)



