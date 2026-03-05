import dilemma
import strategies

from time import sleep

def tournament(*players, num_rounds: int = 10):
    # Play all strategies against each other and sum results
    for i in range(len(players)):
        for j in range(i, len(players)):
            # Track scores before match to announce score changes
            score_i = players[i].score
            score_j = players[j].score

            # If i == j, the strategy must play against a copy of itself
            if i == j:

                # Create new player with the same strategy as player i
                # Prevents player from gaining points twice
                copy_player = dilemma.Player(players[i].strategy)
                dilemma.iterate_dilemma(players[i], dilemma.Player(players[i].strategy), num_rounds)
                
                # Announce Match Results
                print(f"{players[i].strategy.__name__} mirror match")
                print(f"    {players[i].strategy.__name__}: {players[i].score - score_i} points")
                print()
            
            # Otherwise, strategy i plays against strategy j
            else:
                dilemma.iterate_dilemma(players[i], players[j], num_rounds)                
                
                # Announce Match Results
                print(f"{players[i].strategy.__name__} vs {players[j].strategy.__name__}")
                print(f"    {players[i].strategy.__name__}: {players[i].score - score_i} points")
                print(f"    {players[j].strategy.__name__}: {players[j].score - score_j} points")
                print()
            
            # Give time to read match results
            #sleep(1)

    # Announce Final Results
    print()
    print("Final Results")
    for player in players:
        if player.score != 0:
            print(f"    {player.strategy.__name__}: {player.score}")
    print()

p1 = dilemma.Player(strategies.always_cooperate)
p2 = dilemma.Player(strategies.always_cheat)
p3 = dilemma.Player(strategies.copycat)
p4 = dilemma.Player(strategies.rand)
p5 = dilemma.Player(strategies.copy_dist)
p6 = dilemma.Player(strategies.nice_copycat)
p7 = dilemma.Player(strategies.copy_last_three)
p8 = dilemma.Player(strategies.alternate)

players = [p1, p2, p3, p4, p5, p6, p7, p8]

tournament(*players, num_rounds=1000)